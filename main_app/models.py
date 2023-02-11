from django.db import models
from django.urls import reverse
from datetime import date

from django.contrib.auth.models import User

# Create your models here.

class Station(models.Model): 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    availability = models.TextField(max_length=250)
    connectors = models.TextField(max_length=100)
    reviews = models.TextField(max_length=200)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"station_id": self.id})
    
class Vehicle(models.Model):
    TYPES = (
        ('BEV', 'Battery Electric Vehicle'),
        ('PHEV', 'Plug-In Hybrid Electric Vehicle'),
        ('HEV', 'Hybrid Electric Vehicle'),
        ('FCEV', 'Fuel Cell Electric Vehicle')
    )
    type = models.CharField(max_length=4, choices=TYPES, default=TYPES[0][0], verbose_name="EV Type")
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    batterysize = models.IntegerField(verbose_name="Battery Size")

