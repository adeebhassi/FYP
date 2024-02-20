# Generated by Django 5.0.1 on 2024-01-30 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_remove_eventregistration_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='abstract_category',
            field=models.CharField(choices=[('Oral Presentation', 'Oral Presentation'), ('Poster Presentation', 'Poster Presentation')], max_length=50),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='abstract_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='faculty_designation',
            field=models.CharField(choices=[('Lecturer', 'Lecturer'), ('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Professor', 'Professor')], max_length=255),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='fee_receipt',
            field=models.FileField(blank=True, null=True, upload_to='fee_receipts'),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='keywords',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='poster_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 30, 17, 9, 23, 300979, tzinfo=datetime.timezone.utc)),
        ),
    ]