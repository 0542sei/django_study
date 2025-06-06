# Generated by Django 5.2.1 on 2025-05-30 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='users/profile', verbose_name='프로필 이미지'),
        ),
        migrations.AddField(
            model_name='user',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='소개글'),
        ),
    ]
