from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ['author', 'guest_name', 'created_at']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'post_type', 'status', 'views', 'created_at']
    list_filter = ['status', 'post_type']
    search_fields = ['title', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'post', 'is_approved', 'created_at']
    list_filter = ['is_approved']
    actions = ['approve', 'disapprove']
    def approve(self, request, qs): qs.update(is_approved=True)
    def disapprove(self, request, qs): qs.update(is_approved=False)
