from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import uuid

User = get_user_model()

class Post(models.Model):
    STATUS = [('draft', 'Draft'), ('published', 'Published')]
    TYPE = [('post', 'Post'), ('article', 'Article'), ('project_doc', 'Project Doc'), ('tool_doc', 'Tool Doc')]

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=350, unique=True, blank=True)
    excerpt = models.TextField(max_length=500, blank=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blog/covers/', blank=True, null=True)
    post_type = models.CharField(max_length=20, choices=TYPE, default='post')
    status = models.CharField(max_length=20, choices=STATUS, default='published')
    # Link to project or tool (optional)
    project = models.OneToOneField('profiles.Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='documentation')
    tool = models.OneToOneField('profiles.Tool', on_delete=models.SET_NULL, null=True, blank=True, related_name='documentation')
    tags = models.CharField(max_length=300, blank=True, help_text='Comma separated tags')
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            n = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_detail', kwargs={'slug': self.slug})

    @property
    def tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    @property
    def comment_count(self):
        return self.comments.filter(is_approved=True).count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    guest_name = models.CharField(max_length=100, blank=True)
    guest_email = models.EmailField(blank=True)
    body = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    @property
    def display_name(self):
        if self.author:
            return self.author.get_full_name() or self.author.username
        return self.guest_name or 'Anonymous'

    def __str__(self):
        return f'{self.display_name} on {self.post.title[:30]}'
