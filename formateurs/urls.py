from django.urls import path 
from .views import *



urlpatterns=[
    
    path('demandes/',show_demande),
    path('stagiaires/',show_stagiaires),
    path('create_stage/',create_stage)
    
    
    
]