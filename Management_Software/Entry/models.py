from django.db import models
from phone_field import PhoneField
from datetime import datetime
# Create your models here.


class Host(models.Model):
    name = models.CharField(max_length=256, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=10)
    time_stamp = models.TimeField(blank=True)

    def __str__(self):
        return self.name


class Visitor(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=10)
    host_name = models.ForeignKey(Host, on_delete=models.CASCADE)
    checkin_time = models.TimeField(blank=True)
    checkout_time = models.TimeField(blank=True)

    def __str__(self):
        return self.name

