# Generated by Django 3.2.7 on 2021-09-12 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_userr'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='画像')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_img', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
