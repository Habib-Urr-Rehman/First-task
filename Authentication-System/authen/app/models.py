from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    contact_number = models.CharField(max_length=15, blank=True,unique=True)
    years_of_experience = models.IntegerField(default=0)
    university_name = models.CharField(max_length=100, blank=True)
    degree_name = models.CharField(max_length=100, blank=True)

