from django import forms
from .models import Post, Comment

INPUT = 'w-full bg-bg2 border border-white/10 rounded-xl px-4 py-3 text-text placeholder-muted focus:outline-none focus:border-accent/50 text-sm'
TEXTAREA = 'w-full bg-bg2 border border-white/10 rounded-xl px-4 py-3 text-text placeholder-muted focus:outline-none focus:border-accent/50 text-sm resize-none'
SELECT = 'w-full bg-bg2 border border-white/10 rounded-xl px-4 py-3 text-text focus:outline-none focus:border-accent/50 text-sm'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'cover_image', 'post_type', 'status', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'Post title...'}),
            'excerpt': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 2, 'placeholder': 'Short summary (shown in feed)...'}),
            'content': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 16, 'placeholder': 'Write your content here... (supports HTML)'}),
            'post_type': forms.Select(attrs={'class': SELECT}),
            'status': forms.Select(attrs={'class': SELECT}),
            'tags': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'django, tutorial, career...'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'guest_name', 'guest_email']
        widgets = {
            'body': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 3, 'placeholder': 'Write a comment...'}),
            'guest_name': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'Your name'}),
            'guest_email': forms.EmailInput(attrs={'class': INPUT, 'placeholder': 'Your email (optional)'}),
        }
