# Generated by Django 5.0.6 on 2024-06-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_post_date_created_alter_post_title_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Uncategorised', max_length=255),
        ),
    ]