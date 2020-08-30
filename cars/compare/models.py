from django.db import models
from django.contrib.auth.models import User

class bike(models.Model):
    Name = models.CharField(max_length=100)
    Emission = models.CharField(max_length=100, blank=True)
    Engine = models.CharField(max_length=100, blank=True)
    cylinder = models.CharField(max_length=100, blank=True)
    Mileage = models.CharField(max_length=100, blank=True)
    Power = models.CharField(max_length=100, blank=True)
    speed = models.CharField(max_length=100, blank=True)
    Gear = models.CharField(max_length=100, blank=True)
    ABS = models.CharField(max_length=100, blank=True)
    Price = models.CharField(max_length=100, blank=True)






