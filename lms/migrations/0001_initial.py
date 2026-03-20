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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('emoji', models.CharField(default='📚', max_length=5)),
                ('level', models.CharField(choices=[('beginner','Beginner'),('intermediate','Intermediate'),('advanced','Advanced')], default='beginner', max_length=20)),
                ('is_free', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('is_published', models.BooleanField(default=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='lms/courses/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('video_url', models.URLField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('duration_minutes', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='lms.course')),
            ],
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('enrolled_at', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='lms.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to=settings.AUTH_USER_MODEL)),
            ],
            options={'unique_together': {('user', 'course')}},
        ),
        migrations.CreateModel(
            name='LessonProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='lms.enrollment')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.lesson')),
            ],
            options={'unique_together': {('enrollment', 'lesson')}},
        ),
    ]
