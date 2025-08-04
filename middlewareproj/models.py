from django.db import models
from django.utils import timezone

class BlockedIP(models.Model):
    ip_address = models.CharField(max_length=30, unique=True)
    count = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.ip_address
