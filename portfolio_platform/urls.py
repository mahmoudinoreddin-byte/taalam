from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def home_view(request):
    try:
        from blog.models import Post
        recent_posts = Post.objects.filter(status='published').select_related('author', 'author__profile').order_by('-created_at')[:6]
    except Exception:
        recent_posts = []
    return render(request, 'home.html', {'recent_posts': recent_posts})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('accounts/', include('accounts.urls')),
    path('profiles/', include('profiles.urls')),
    path('shop/', include('shop.urls')),
    path('lms/', include('lms.urls')),
    path('messages/', include('messaging.urls')),
    path('blog/', include('blog.urls')),
    path('p/', include('profiles.public_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
