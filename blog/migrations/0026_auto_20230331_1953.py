# Generated by Django 3.2.18 on 2023-03-31 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_rename_username_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_img',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]