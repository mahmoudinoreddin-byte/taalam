from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('create/', views.create_post, name='create_post'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('u/<str:username>/', views.user_blog, name='user_blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]
