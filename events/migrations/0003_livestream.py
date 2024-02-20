# Generated by Django 4.1.6 on 2024-01-22 10:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_speech_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_url', models.URLField()),
                ('start_time', models.DateTimeField(default=datetime.datetime(2024, 1, 22, 10, 6, 36, 631004, tzinfo=datetime.timezone.utc))),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]
