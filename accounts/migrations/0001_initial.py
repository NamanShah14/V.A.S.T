# Generated by Django 5.1.7 on 2025-03-09 11:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('otp', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('feedback', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
