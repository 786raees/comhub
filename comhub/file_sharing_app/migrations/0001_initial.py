# Generated by Django 3.2.15 on 2022-08-28 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title for the File')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note or Reminder')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to=settings.AUTH_USER_MODEL, verbose_name='assigned_to')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploader', to=settings.AUTH_USER_MODEL, verbose_name='uploader')),
            ],
        ),
    ]
