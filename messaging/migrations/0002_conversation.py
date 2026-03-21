from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('messaging', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('participants', models.ManyToManyField(related_name='conversations', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['created_at']},
        ),
        migrations.RemoveField(model_name='message', name='recipient'),
        migrations.RemoveField(model_name='message', name='subject'),
        migrations.RemoveField(model_name='message', name='is_read'),
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='messages',
                to='messaging.conversation',
                null=True,
            ),
        ),
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
