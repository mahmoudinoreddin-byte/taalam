from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Order

def shop_home(request):
    products = Product.objects.filter(is_active=True).order_by('-is_featured', 'price')
    featured = products.filter(is_featured=True).first()
    return render(request, 'shop/shop.html', {'products': products, 'featured': featured})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def purchase(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user, product=product, amount=product.price, status='paid')
        messages.success(request, f'Purchase successful! You can now download "{product.title}".')
        return redirect('order_success', pk=order.pk)
    return render(request, 'shop/checkout.html', {'product': product})

@login_required
def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'shop/order_success.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user, status='paid').select_related('product').order_by('-created_at')
    return render(request, 'shop/my_orders.html', {'orders': orders})
