
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from stages.models import *
# Create your views here.


def my_stage(request):
    if  request.user.is_authenticated and request.user.is_stagiaire and request.user.stagiaire.is_active:
               
        stage = Stage.objects.get(stagiaire_id=request.user.id)
        axe_taches={}
        axes=Axe.objects.filter(cahierCharge_id=stage.id)
        for axe in axes:
            axe_taches[axe.title]=[]
            taches = Tache.objects.filter(axe=axe)
            if taches:
                for tache in taches:
                    axe_taches[axe.title].append(tache)
        return render(request,'stage_details.html',context={'stage':stage,'cahiercharge':stage.cahiercharge.cahierCharge,"axes":axe_taches})    
               
    else:
        return redirect('/login')  

def create_tache(request):
    if request.POST and request.user.is_stagiaire and request.user.stagiaire.is_active:
        obj=request.POST
        print(obj)     
        stage = Stage.objects.get(stagiaire_id=request.user.id)
        axe=Axe.objects.filter(cahierCharge_id=stage.id).get(title=obj['axe'])
        for tache in obj:
            if tache != 'csrfmiddlewaretoken' and tache != 'axe' and obj[tache] != '':
                Tache.objects.create(descrptionTache=obj[tache],axe_id=axe.id)
        
        return redirect('/mon_stage/')

def create_axes(request):
    if request.POST and request.user.is_stagiaire and request.user.stagiaire.is_active:
        obj=request.POST
        print(obj)
        stage = Stage.objects.get(stagiaire_id=request.user.id)
        for key in request.POST:
            if key != 'csrfmiddlewaretoken' and obj[key]!='':
                if len(Axe.objects.filter(title=obj[key]))!=0: 
                    print('already in or not an axe')
                else:
                    print('eeeeeeee')
                    Axe.objects.create(title=obj[key],cahierCharge_id=stage.id)
        return redirect('/mon_stage/')        