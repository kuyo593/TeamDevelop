# Generated by Django 3.2.7 on 2021-09-10 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_img', to='main.user'),
        ),
    ]
