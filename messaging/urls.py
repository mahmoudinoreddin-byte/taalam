from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('message/<int:pk>/', views.message_detail, name='message_detail'),
    path('compose/', views.send_message, name='compose'),
    path('compose/<str:username>/', views.send_message, name='compose_to'),
    path('delete/<int:pk>/', views.delete_message, name='delete_message'),
]
