# Generated by Django 3.2.7 on 2021-11-11 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_group_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupimage',
            old_name='user',
            new_name='group',
        ),
    ]