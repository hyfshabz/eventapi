from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
     eventname = models.CharField(max_length=200)
     location = models.CharField(max_length=200)
     eventdate = models.DateField()
     description = models.TextField()

     def __str__(self):
         return self.eventname

