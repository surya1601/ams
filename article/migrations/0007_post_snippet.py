# Generated by Django 5.0.6 on 2024-06-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the above link to read the article', max_length=255),
        ),
    ]