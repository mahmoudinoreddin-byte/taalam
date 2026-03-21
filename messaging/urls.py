from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('conversation/<int:conv_id>/', views.conversation, name='conversation'),
    path('start/<str:username>/', views.start_conversation, name='start_conversation'),
    path('delete/<int:conv_id>/', views.delete_conversation, name='delete_conversation'),
]
