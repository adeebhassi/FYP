# Generated by Django 4.1.6 on 2023-12-26 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_file',
        ),
    ]
