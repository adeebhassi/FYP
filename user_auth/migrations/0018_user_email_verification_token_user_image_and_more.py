# Generated by Django 4.2.7 on 2024-02-11 05:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0017_remove_profile_email_remove_profile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verification_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Profile/Profile_images/'),
        ),
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
