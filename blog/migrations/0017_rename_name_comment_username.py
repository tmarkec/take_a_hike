# Generated by Django 3.2.18 on 2023-03-31 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_comment_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='username',
        ),
    ]
