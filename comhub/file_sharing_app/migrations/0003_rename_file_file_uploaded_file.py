# Generated by Django 3.2.15 on 2022-08-28 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_sharing_app', '0002_file_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file',
            new_name='uploaded_file',
        ),
    ]
