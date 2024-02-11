from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    bio = models.TextField(max_length=150, blank=True)
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=12,blank=True,null=True)
    location = models.CharField(max_length=50, blank=True)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    