from django.db import models

# Create your models here.


class user(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.first_name+" "+self.last_name