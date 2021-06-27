from stages.models import Stagiaire
from .models import ProfileStagiaire

from django.db.models.signals import post_save
from django.dispatch import receiver





@receiver(post_save,sender=Stagiaire)
def post_save_create_profile_stagiaire(sender, instance, created ,*args,**kwargs):
    print(sender)
    print(instance)
    print(created)
    if created :
        ProfileStagiaire.objects.create(user=instance)
