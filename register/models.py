from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class LoginForm(AbstractUser):
    name = models.CharField(max_length = 100)
    login = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    confirm_password = models.CharField(max_length = 100)
    age = models.IntegerField(max_length = 100)
    work = models.CharField(max_length = 100)
    hobby = models.CharField(max_length = 100)






