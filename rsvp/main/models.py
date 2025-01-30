from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=50)

class User(models.Model):
    invite_code = models.CharField(max_length=16)
    attending = models.BooleanField(default=False)
    guests = models.ManyToManyField(Guest, blank=True)
    code_used = models.BooleanField(default=False)



# Create your models here.
