from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm

User = get_user_model()

def feed(request):
    """Global feed - all published posts from all users"""
    posts = Post.objects.filter(status='published').select_related('author', 'author__profile').order_by('-created_at')
    post_type = request.GET.get('type', '')
    if post_type:
        posts = posts.filter(post_type=post_type)
    return render(request, 'blog/feed.html', {'posts': posts, 'post_type': post_type})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    # Increment views
    Post.objects.filter(pk=post.pk).update(views=post.views + 1)
    post.refresh_from_db()

    comments = post.comments.filter(is_approved=True)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added!')
            return redirect('post_detail', slug=slug)

    # Related posts from same author
    related = Post.objects.filter(author=post.author, status='published').exclude(pk=post.pk)[:3]

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
        'related': related,
        'profile': getattr(post.author, 'profile', None),
    })

def user_blog(request, username):
    """All posts by a specific user"""
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author, status='published').order_by('-created_at')
    return render(request, 'blog/user_blog.html', {
        'author': author,
        'posts': posts,
        'profile': getattr(author, 'profile', None),
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post published!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Create'})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'post': post, 'action': 'Edit'})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    post.delete()
    messages.success(request, 'Post deleted.')
    return redirect('user_blog', username=request.user.username)

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/my_posts.html', {'posts': posts})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.post.author or request.user.is_staff:
        comment.delete()
    return redirect('post_detail', slug=comment.post.slug)
