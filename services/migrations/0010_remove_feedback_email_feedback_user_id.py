# Generated by Django 5.1.7 on 2025-03-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_remove_feedback_user_id_feedback_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='email',
        ),
        migrations.AddField(
            model_name='feedback',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
