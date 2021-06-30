from django.db import models
from accounts.models import User

class Departement(models.Model): 
    nom_departement= models.CharField(max_length=255)  
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.nom_departement

class Specialite(models.Model): 
    departement=models.OneToOneField(Departement,null=True,on_delete=models.SET_NULL)
    nom_specialite= models.CharField(max_length=255)  
    created = models.DateTimeField(auto_now_add=True) 
    def __str__(self) :
        return self.nom_specialite  

class Formateur(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    updated= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    specialite = models.ForeignKey(Specialite , null=True,on_delete=models.SET_NULL)
    def __str__(self) -> str:
        return self.user.username

class Stagiaire(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)    
    phone_number = models.CharField(max_length=20)
    specialite = models.ForeignKey(Specialite ,  null=True,on_delete=models.SET_NULL)
    score=models.PositiveBigIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    formateur = models.ForeignKey(Formateur, blank=True,null=True ,on_delete = models.CASCADE)
    def __str__(self) -> str:
        return self.user.username

class Document(models.Model):
    stagiaire= models.OneToOneField(Stagiaire,on_delete=models.CASCADE ,primary_key = True)
    cv= models.FileField( blank=True,upload_to='cvs')
    rapport = models.FileField( blank=True,upload_to='rapports')

    attestation = models.FileField( blank=True,upload_to='attestation')
    def __str__(self):
        return self.stagiaire.user.username + ": documents "        

class Stage(models.Model):
    sujet = models.CharField(max_length=100)
    description_du_stage=models.TextField()
    duree = models.CharField(max_length=100)
    type_de_stage=models.CharField(max_length=100)
    remunere=models.BooleanField()
    nombre_de_stagiaire=models.IntegerField()
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE)
    stagiaire=models.ForeignKey(Stagiaire,on_delete=models.CASCADE ,null=True)
    occupe=models.BooleanField(default=False)
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
        return self.axe.title