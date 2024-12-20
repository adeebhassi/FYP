# Generated by Django 5.0.1 on 2024-01-31 05:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_purpose_alter_livestream_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventregistration',
            name='abstract_category',
        ),
        migrations.RemoveField(
            model_name='eventregistration',
            name='abstract_terms',
        ),
        migrations.RemoveField(
            model_name='eventregistration',
            name='abstract_title',
        ),
        migrations.RemoveField(
            model_name='eventregistration',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='eventregistration',
            name='poster_terms',
        ),
        migrations.RemoveField(
            model_name='eventregistration',
            name='poster_title',
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='purpose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.purpose'),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 5, 17, 16, 711879, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='PurposeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.purpose')),
            ],
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='purposetype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.purposetype'),
        ),
    ]
