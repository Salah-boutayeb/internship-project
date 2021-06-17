from accounts.models import User 
from formateurs.models import Formateur
from stagiaire.models import Document, Stagiaire
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction



class StagiaireSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    cv = forms.FileInput()

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_stagiaire = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        stagiaire = Stagiaire.objects.create(user=user)
        stagiaire.phone_number=self.cleaned_data.get('phone_number')
        stagiaire.save()
        print(self.cleaned_data.get('cv'))
        Document(stagiaire=stagiaire,cv=self.cleaned_data.get('cv'))
        return user
    
class FormateurSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    
	
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_formateur = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        formateur = Formateur.objects.create(user=user)
        formateur.phone_number=self.cleaned_data.get('phone_number')
        formateur.departement=self.cleaned_data.get('departement')
        formateur.save()
        return user
