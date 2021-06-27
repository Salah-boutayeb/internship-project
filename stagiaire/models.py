from django.db import models
from stages.models import Stagiaire
class ProfileStagiaire(models.Model):
    user = models.OneToOneField(Stagiaire, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(default='user.png', upload_to='avatars')
    linkedin = models.URLField(blank=True)
    updated= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return "profile of the user "+self.user.user.username        




