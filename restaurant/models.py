from django.db import models
from datetime import datetime, time
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
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
    def __str__(self):
        return f"Booking for {self.user.username}"
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject