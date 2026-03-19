from django.urls import path
from .public_views import public_profile

urlpatterns = [
    path('<slug:slug>/', public_profile, name='public_profile'),
]
