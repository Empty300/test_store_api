from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    country = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    telephone = models.CharField(max_length=256, null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)
