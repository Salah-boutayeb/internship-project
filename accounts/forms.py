from accounts.models import User 
from stages.models import *

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction



class StagiaireSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    specialite = forms.CharField(required=True)
    
    

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        spec=Specialite.objects.create(nom_specialite=self.cleaned_data.get('specialite'))
        user.is_stagiaire = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        stagiaire = Stagiaire.objects.create(user=user)
        stagiaire.specialite=spec

        stagiaire.phone_number=self.cleaned_data.get('phone_number')
        stagiaire.save()
        Document.objects.create(stagiaire=stagiaire)
        
        return user
    
class FormateurSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    specialite = forms.CharField(required=True)
    departement = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        depart=Departement.objects.create(nom_departement=self.cleaned_data.get('departement'))
        spec=Specialite.objects.create(departement_id=depart.id,nom_specialite=self.cleaned_data.get('specialite'))
        user.is_formateur = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        formateur = Formateur.objects.create(user=user)
        formateur.specialite = spec
        formateur.phone_number=self.cleaned_data.get('phone_number')
        formateur.departement=self.cleaned_data.get('departement')
        formateur.save()
        return user
