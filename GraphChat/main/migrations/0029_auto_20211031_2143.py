# Generated by Django 3.2.7 on 2021-10-31 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20211031_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk',
            name='child_talk_id',
        ),
        migrations.RemoveField(
            model_name='talk',
            name='talk_from',
        ),
        migrations.RemoveField(
            model_name='talk',
            name='talk_to',
        ),
        migrations.AddField(
            model_name='talk',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
