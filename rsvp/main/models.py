from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=50)



# Create your models here.
