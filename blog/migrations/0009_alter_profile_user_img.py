# Generated by Django 3.2.18 on 2023-03-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_profile_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='image'),
        ),
    ]
