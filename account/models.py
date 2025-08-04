from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name})"
