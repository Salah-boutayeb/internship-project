from django.urls import path 
from .views import *



urlpatterns=[ 
    path('create_axes/',create_axes),
    path('create_tache/',create_tache),
    path('mon_stage/',my_stage),
    path('my_progress/',getprogress),
    path('my_progress/<int:id>',validate_tache),
    path('update_tache/<int:id>',update_tache),
    path('delete_tache/<int:id>',delete_tache),
    path('update_axe/<int:id>',update_axe),
    path('delete_axe/<int:id>',delete_axe),
    path('rapport/',get_rapport),    
]