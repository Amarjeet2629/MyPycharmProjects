from django.db import models
from django.urls import reverse
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=264)
    roll = models.PositiveIntegerField()
    dept = models.ForeignKey('Department', related_name='students', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('Register:student_create_view')

    def __str__(self):
        return self.name
