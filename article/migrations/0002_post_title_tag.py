# Generated by Django 5.0.6 on 2024-06-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Article Management System', max_length=255),
        ),
    ]