# Generated by Django 3.2.7 on 2021-11-10 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_talk_child_talk_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='talk_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='talk_from_topicmodel', to='main.user'),
        ),
    ]
