from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.login_page),
    path('logout/',views.logout_user),
    path('formateur_register/',views.formateur_register.as_view(), name='formateur_register'),
    path('stagiaire_register/',views.stagiare_register.as_view(), name='stagiaire_register'),
    
]