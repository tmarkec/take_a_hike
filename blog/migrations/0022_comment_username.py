# Generated by Django 3.2.18 on 2023-03-31 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_remove_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='default_username', max_length=80),
        ),
    ]
