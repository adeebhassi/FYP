# Generated by Django 4.2.7 on 2024-02-11 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0027_alter_livestream_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestream',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 11, 5, 45, 58, 303030, tzinfo=datetime.timezone.utc)),
        ),
    ]