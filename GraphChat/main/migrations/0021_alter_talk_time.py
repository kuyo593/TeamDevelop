# Generated by Django 3.2.7 on 2021-10-02 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_talk_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]