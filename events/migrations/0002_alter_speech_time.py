# Generated by Django 4.1.6 on 2023-12-21 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speech',
            name='time',
            field=models.TimeField(blank=True),
        ),
    ]