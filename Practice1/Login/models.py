from django.db import models


class user(models.Model):
    first = models.CharField(max_length=264)
    last = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        return self.first + " " + self.last



