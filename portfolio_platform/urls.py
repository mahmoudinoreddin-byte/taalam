from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('profiles/', include('profiles.urls')),
    path('shop/', include('shop.urls')),
    path('lms/', include('lms.urls')),
    path('messages/', include('messaging.urls')),
    # Public profile URL: /p/username/
    path('p/', include('profiles.public_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
