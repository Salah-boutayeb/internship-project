from django.urls import path 
from .views import *



urlpatterns=[
    
    path('',show),
    path('stage/taches/<int:id>',stage_taches),
    path('stage/<int:id>',get_stage_details),
    path('stage/demande/',demande_stage),
    
    
]