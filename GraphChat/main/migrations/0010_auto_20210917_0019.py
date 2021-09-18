# Generated by Django 3.2.7 on 2021-09-16 15:19

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_talk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
            ],
        ),
        migrations.AlterField(
            model_name='talk',
            name='child_talk_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='talk',
            name='talk',
            field=models.CharField(max_length=500),
        ),
        migrations.CreateModel(
            name='GroupImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='画像')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='group_img', to='main.group')),
            ],
        ),
    ]
