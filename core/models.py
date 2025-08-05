from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomuserManager



class RoleChoices(models.TextChoices):
      GOLD='gold','Gold',
      SILVER='silver','Silver',
      BRONZE='bronze','Bronze'
      GUEST='guest','Guest'

class CustomUser(AbstractUser):
    username = None 
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    
    role=models.CharField(max_length=10,choices=RoleChoices.choices ,default=RoleChoices.GUEST)


    USERNAME_FIELD = 'email'         
    REQUIRED_FIELDS = ['name']      

    objects=CustomuserManager() 

    def __str__(self):
        return self.email
