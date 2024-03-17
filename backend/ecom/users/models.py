from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
