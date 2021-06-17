

from django.shortcuts import redirect, render
from .models import *
from formateurs.models import Formateur

from stagiaire.models import Stagiaire
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.


login_required='/login/'

def show(request):
    stages=Stage.objects.all()
       
    return render(request,'stages/show.html',{'stages':stages})

def create_stage(request):
    if request.user.is_authenticated:
	
        if request.POST:

            owner_name= request.user
            obj=request.POST
            if obj['stage_title'] and obj['description-stage'] and obj['cahiercharge-stage']:
                formateur =Formateur.objects.get(user=owner_name)
                
                stage=Stage(sujet=obj['stage_title'],description_du_stage=obj['description-stage'].replace('\n',' '),formateure=formateur)
                stage.save()
                
                charges=CahierCharge(stage=stage,cahierCharge=obj['cahiercharge-stage'].replace('\n',' '))
                charges.save()
            else:
                messages.info(request, "s'il vous plait ajouter un stage !!!")
                print('empty')
            return render(request,'stages/create_taches.html',context={'charges':charges})
        return render(request,'stages/create_stage.html')
    else:
        return redirect(login_required)    

def create_axe_tache(request):
    if request.user.is_authenticated:
        if request.POST:

             owner_name= request.user
             obj=request.POST
             if obj['stage_title'] and obj['description-stage'] and obj['cahiercharge-stage']:
                formateur =Formateur.objects.get(user=owner_name)
            
                stage=Stage(sujet=obj['stage_title'],description_du_stage=obj['description-stage'].replace('\n',' '),formateure=formateur)
                stage.save()
                
                charges=CahierCharge(stage=stage,cahierCharge=obj['cahiercharge-stage'].replace('\n',' '))
                charges.save()
        else:
            messages.info(request, "s'il vous plait ajouter un stage !!!")
            print('empty')
            return render(request,'stages/create_taches.html',context={'charges':charges})
        return render(request,'stages/create_stage.html')
    else:
        return redirect(login_required)    



def stage_taches(request,id):
    if request.user.is_authenticated:
        stage=Stage.objects.get(pk=id)
        cahiercharges=CahierCharge.objects.get(stage=stage)
        axe_taches={}
        axes=Axe.objects.filter(cahierCharge=cahiercharges)
        for axe in axes:
            taches = Tache.objects.filter(axe=axe)
            if taches:
                axe_taches[axe.title]=[]
                for tache in taches:
                    
                    axe_taches[axe.title].append(tache)
        context={'stages':axe_taches}    
    
        return render(request,'stages/stage_taches.html' ,context)
    else:
        return redirect(login_required)       

def get_stage_details(request,id):
    stage=Stage.objects.get(pk=id)
    cahiercharge=stage.cahiercharge
    
    context={'stage':stage,'charge':cahiercharge}
    return render(request,'stages/stage_details.html',context )
def demande_stage(request):
    if request.user.is_authenticated:
        
        stagiaire=Stagiaire.objects.get(user=request.user)
        stage=Stage.objects.get(pk=request.POST['id'])
        
        demande=Demande(stagiaire=stagiaire,stage=stage)
        demande.save()
        return redirect('/')
    else:
        return redirect(login_required) 