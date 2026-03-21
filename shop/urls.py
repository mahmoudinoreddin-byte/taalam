from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_home, name='shop'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('purchase/<int:pk>/', views.purchase, name='purchase'),
    path('order/<int:pk>/success/', views.order_success, name='order_success'),
    path('my-orders/', views.my_orders, name='my_orders'),
]
