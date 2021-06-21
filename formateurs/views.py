from django.shortcuts import redirect, render
from stagiaire.models import Document, Stagiaire
from .models import *
from stages.models import *
from django.contrib import messages
# Create your views here.
login_required='/login/'
def show_demande(request):
    if request.user.is_authenticated and request.user.is_formateur:
        if request.POST:
            demande=Demande.objects.get(pk=request.POST['id'])
            stagiaire=demande.stagiaire
            stagiaire.is_active=True
            stage=demande.stage
            stage.stagiaire=stagiaire
            stagiaire.save()
            stage.save()
            demande.delete()
            redirect('/formateur/demandes/')
        demandes=Demande.objects.all()
        return render(request,'demande.html',context={'demandes':demandes})
    else:
        return redirect(login_required)

def show_stagiaires(request):
    if request.user.is_authenticated and request.user.is_formateur:
        data=[]
        stagiaires=Stagiaire.objects.all()
        for stagiaire in stagiaires:
            if stagiaire.is_active:
                stg={}
                stg['id']=stagiaire.user_id
                stages=stagiaire.stage_set.all()
                for stage in stages:
                        stg['stage']=stage.sujet
                stg["name"]=stagiaire.user
                if Document.objects.all():
                    document=Document.objects.get(stagiaire_id=stagiaire.user_id)
                    stg["cv"]=document.cv      
                data.append(stg)   
        context={'stagiaires':data}         
        print(context)
        return render(request,'stagiaires.html',context)
    else:
        return redirect(login_required)

def create_stage(request):
    if request.user.is_authenticated and request.user.is_formateur :
        if request.POST:
            owner_name= request.user
            obj=request.POST
            if obj['stage_title'] and obj['description-stage'] and obj['cahiercharge-stage']:
                formateur =Formateur.objects.get(user=owner_name)
                
                stage=Stage(sujet=obj['stage_title'],description_du_stage=obj['description-stage'].replace('\n',' '),formateure=formateur)
                stage.save()
                
                charges=CahierCharge(stage=stage,cahierCharge=obj['cahiercharge-stage'].replace('\n',' '))
                charges.save()
                return redirect('/')
                # return render(request,'stages/create_taches.html',context={'charges':charges})
            else:
                messages.info(request, "s'il vous plait ajouter un stage !!!")
        return render(request,'create_stage.html')
    else:
        return redirect(login_required) 