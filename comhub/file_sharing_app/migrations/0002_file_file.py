# Generated by Django 3.2.15 on 2022-08-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_sharing_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default=1, upload_to='uploads', verbose_name='File'),
            preserve_default=False,
        ),
    ]
