from stages.models import Formateur, Stagiaire
from .models import ProfileFormateur

from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save,sender=Formateur)
def post_save_create_profile_formateur(sender, instance, created ,*args,**kwargs):
    print(sender)
    print(instance)
    print(created)
    if created :
        ProfileFormateur.objects.create(user=instance)        