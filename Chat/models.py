from django.db import models
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Message(models.Model):
    value =models.CharField(max_length=1000000)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user= models.CharField(max_length=100000) 
    room = models.CharField(max_length=1000000)
    
    def __str__(self):
        return self.value

# Create your models here.
