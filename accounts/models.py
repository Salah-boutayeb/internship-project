from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_formateur = models.BooleanField(default=False)
    is_stagiaire = models.BooleanField(default=False)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    updated= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    