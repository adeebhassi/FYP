from django.db import models

# Create your models here.
class NationalSpeaker(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='speakers/national_speakers/')
    designation=models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class InterNationalSpeaker(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='speakers/national_speakers/')
    designation=models.CharField(max_length=300)

    def __str__(self):
        return self.name