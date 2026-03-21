from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('product_type', models.CharField(choices=[('template','CV Template'),('theme','Website Theme'),('ebook','E-Book'),('service','Service'),('bundle','Bundle'),('other','Other')], default='template', max_length=20)),
                ('emoji', models.CharField(default='📄', max_length=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='shop/products/')),
                ('file', models.FileField(blank=True, null=True, upload_to='shop/files/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('download_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(choices=[('pending','Pending'),('paid','Paid'),('cancelled','Cancelled')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
