from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField
from formateurs.models import Formateur
from stagiaire.models import Stagiaire
class Stage(models.Model):
    sujet = models.CharField(max_length=100)
    description_du_stage=models.TextField()

    formateure = models.ForeignKey(Formateur, on_delete=models.CASCADE)
    stagiaire=models.ForeignKey(Stagiaire,on_delete=models.CASCADE ,null=True)
    updated= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.sujet

    class Meta:
        ordering = ("-created",)
        
class Demande(models.Model):
    stagiaire=models.ForeignKey(Stagiaire,on_delete=models.CASCADE)
    stage=models.ForeignKey(Stage,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.stagiaire.user.username

class CahierCharge(models.Model):
    
    stage = models.OneToOneField(Stage,on_delete=models.CASCADE,primary_key=True)
    cahierCharge=models.TextField(default='empty...')

    updated= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.stage.sujet
    
class Axe(models.Model):
    title=models.CharField(max_length=100)
    cahierCharge= models.ForeignKey(CahierCharge, on_delete=models.CASCADE)
    is_completed=models.BooleanField(default=False)
    updated= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.title

class Tache(models.Model):
    
    axe= models.ForeignKey(Axe, on_delete=models.CASCADE )
    descrptionTache=models.TextField()
    is_done=models.BooleanField(default=False)
    updated= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.title