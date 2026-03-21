from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [('profiles', '0001_initial')]
    operations = [
        migrations.AddField(model_name='profile', name='phone', field=models.CharField(blank=True, max_length=30)),
        migrations.AddField(model_name='profile', name='contact_email', field=models.EmailField(blank=True)),
        migrations.AddField(model_name='sociallink', name='custom_label', field=models.CharField(blank=True, max_length=100)),
        migrations.AddField(model_name='project', name='doc_url', field=models.URLField(blank=True)),
        migrations.AddField(model_name='tool', name='doc_url', field=models.URLField(blank=True)),
    ]
