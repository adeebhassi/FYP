# Generated by Django 5.0.1 on 2024-01-30 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_livestream_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventregistration',
            name='approved',
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='abstract_category',
            field=models.CharField(blank=True, choices=[('Oral Presentation', 'Oral Presentation'), ('Poster Presentation', 'Poster Presentation')], max_length=50),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='abstract_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='keywords',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='poster_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='status',
            field=models.CharField(choices=[('Approved for Submission', 'Approved for Submission'), ('Approved for Presentation', 'Approved for Presentation'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 30, 17, 2, 29, 350964, tzinfo=datetime.timezone.utc)),
        ),
    ]