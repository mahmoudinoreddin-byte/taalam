from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_type', 'price', 'is_active', 'is_featured', 'download_count']
    list_filter = ['product_type', 'is_active', 'is_featured']
    search_fields = ['title']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'product', 'amount', 'status', 'created_at']
    list_filter = ['status']
