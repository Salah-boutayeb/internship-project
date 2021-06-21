from django.urls import path 
from .views import *



urlpatterns=[
    
    path('create_axes/',create_axes),
    path('create_tache/',create_tache),
    path('mon_stage/',my_stage),
    
]