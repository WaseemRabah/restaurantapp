from django.db import models
from datetime import datetime, time
from django.shortcuts import render

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    num_people = models.PositiveIntegerField(default=1)
    date = models.DateTimeField()
    time = models.TimeField()
    OCCASION_CHOICES = [
        ('1', 'Enjoy my self'),
        ('2', 'Date'),
        ('3', 'Birthday'),
        ('4', 'Anniversary'),
        ('5', 'Party'),
    ]
    occasion = models.CharField(max_length=1, choices=OCCASION_CHOICES, default='1')
    def __str__ (self):
        return self.name