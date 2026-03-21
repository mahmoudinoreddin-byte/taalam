from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    TYPE_CHOICES = [
        ('template', 'CV Template'),
        ('theme', 'Website Theme'),
        ('ebook', 'E-Book'),
        ('service', 'Service'),
        ('bundle', 'Bundle'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    product_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='template')
    emoji = models.CharField(max_length=5, default='📄')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    original_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='shop/products/', blank=True, null=True)
    file = models.FileField(upload_to='shop/files/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    download_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def discount_percent(self):
        if self.original_price and self.original_price > self.price:
            return int((1 - self.price / self.original_price) * 100)
        return 0


class Order(models.Model):
    STATUS_CHOICES = [('pending','Pending'),('paid','Paid'),('cancelled','Cancelled')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.pk} — {self.user.username}'
