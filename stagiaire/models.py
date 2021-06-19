from django.db import models

from accounts.models import User
from formateurs.models import Formateur
# Create your models here.


class Stagiaire(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)    
    phone_number = models.CharField(max_length=20)
    specialite = models.CharField(max_length=20 ,null=True )
    is_active = models.BooleanField(default=False)
    formateur = models.ForeignKey(Formateur, null=True ,on_delete = models.CASCADE)
    def __str__(self) -> str:
        return self.user.username

class Document(models.Model):
    stagiaire= models.OneToOneField(Stagiaire,on_delete=models.CASCADE ,primary_key = True)
    cv= models.FileField( blank=True)
    rapport = models.FileField( blank=True)
    def __str__(self):
        return self.stagiaire.user.username + ": documents "