from django.urls import path 
from .views import *



urlpatterns=[
    
    path('demandes/',show_demande),
    path('stagiaires/',show_stagiaires),
    path('create_stage/',create_stage),
    path('update_stage/<int:id>',update_stage),
    path('delete_stage/<int:id>',delete_stage),
    path('mes_stages/',mes_stages),
    
    
]