from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',views.login_page),
    path('logout/',views.logout_user),
    path('formateur_register/',views.formateur_register.as_view(), name='formateur_register'),
    path('stagiaire_register/',views.stagiare_register.as_view(), name='stagiaire_register'),
    path('profile/<str:name>',views.profiles, name='user_profile'),
    path('edite/profile/',views.edite),
# reset password routes 
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),   
]