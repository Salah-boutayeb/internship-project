from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from stages.models import *
# Create your views here.

def my_stage(request):
    if  request.user.is_authenticated and request.user.is_stagiaire and request.user.stagiaire.is_active:
               
        stage = Stage.objects.get(stagiaire_id=request.user.id)
        axe_taches={}
        if stage:
            axes=Axe.objects.filter(cahierCharge_id=stage.id)
            for axe in axes:
                axe_taches[axe]=[]
                taches = Tache.objects.filter(axe=axe)
                if taches:
                    for tache in taches:
                        axe_taches[axe].append(tache)
            return render(request,'stage_details.html',context={'stage':stage,'cahiercharge':stage.cahiercharge.cahierCharge,"axes":axe_taches})    
        return redirect('/')       
    else:
        return redirect('/accounts/login')  

""" def create_tache(request):
    if request.POST and request.user.is_stagiaire and request.user.stagiaire.is_active:
        obj=request.POST     
        stage = Stage.objects.get(stagiaire_id=request.user.id)
        axe=Axe.objects.filter(cahierCharge_id=stage.id).get(title=obj['axe'])
        print(axe)
        for tache in obj:
            if tache != 'csrfmiddlewaretoken' and tache != 'axe' and obj[tache] != '':
                Tache.objects.create(descrptionTache=obj[tache],axe_id=axe.id)
        
        return redirect('/stagiaire/mon_stage/') """
def create_tache(request):
    if request.POST and request.user.is_stagiaire and request.user.stagiaire.is_active:
        obj=request.POST     
        stage = Stage.objects.get(stagiaire_id=request.user.id)
        axes=Axe.objects.filter(cahierCharge_id=stage.id)
        for axe in axes: 
            if axe.title==obj['axe']:
                for tache in obj:
                    if tache != 'csrfmiddlewaretoken' and tache != 'axe' and obj[tache] != '':
                        Tache.objects.create(descrptionTache=obj[tache],axe_id=axe.id)
        
        return redirect('/stagiaire/mon_stage/')
def create_axes(request):
    if request.POST and request.user.is_stagiaire and request.user.stagiaire.is_active:
        obj=request.POST

        stage = Stage.objects.get(stagiaire_id=request.user.id)
        for key in request.POST:
            if key != 'csrfmiddlewaretoken' and obj[key]!='':
                if len(Axe.objects.filter(title=obj[key]))!=0: 
                    print('already in or not an axe')
                else:
                    print('eeeeeeee')
                    Axe.objects.create(title=obj[key],cahierCharge_id=stage.id)
        return redirect('/stagiaire/mon_stage/')    

def getprogress(request):
    if request.user.is_authenticated and request.user.is_stagiaire and request.is_ajax():
        done=0
        not_done=100
        totale=0
        stage = Stage.objects.get(stagiaire_id=request.user.id)
        axes=stage.cahiercharge.axe_set.all()
        if axes:
            for axe in axes :
                totale+=axe.tache_set.all().count()
                taches=axe.tache_set.all()
                if taches:
                    for tache in taches:
                        if tache.is_done:
                            done=done+1
            if totale==0:
                totale=1                
            done=(done/totale)*100
            not_done-=done 
            stagiaire = Stagiaire.objects.get(user_id=request.user.id)
            stagiaire.score=done
            stagiaire.save()                       
        return JsonResponse({'data':{'progress':[{'done':done},{'not done':not_done}],
        'done':done}})

def validate_tache(request,id):
    if request.POST and request.is_ajax() and request.user.is_stagiaire and request.user.stagiaire.is_active:
        tache=Tache.objects.get(id=id)
        
        if tache.is_done:
            tache.is_done=False
        else:
            tache.is_done=True
        tache.save()    
        return JsonResponse({'data':id}) 

def update_tache(request,id):
    if  request.POST and request.user.is_stagiaire and request.user.stagiaire.is_active:
        tache =Tache.objects.get(id=id)
        tache.descrptionTache=request.POST['tache']
        tache.save
        return redirect('/stagiaire/mon_stage/')

def delete_tache(request,id):
    if  request.POST and request.is_ajax() and request.user.is_stagiaire and request.user.stagiaire.is_active:
        tache =Tache.objects.get(id=id)
        tache.delete()
        return JsonResponse({'data':'tache deleted successfully'})

def update_axe(request,id):
    if  request.POST  and request.user.is_stagiaire and request.user.stagiaire.is_active:
        axe=Axe.objects.get(id=id)
        axe.title=request.POST['axe']
        axe.save()
        return redirect('/stagiaire/mon_stage/')

def delete_axe(request,id):
    if  request.POST and request.is_ajax() and request.user.is_stagiaire and request.user.stagiaire.is_active:
        axe=Axe.objects.get(id=id)
        axe.delete()
        return JsonResponse({'data':'axe deleted'})
def get_rapport(request):
     if request.POST and request.user.is_stagiaire and request.user.stagiaire.is_active:
        satgiaire=Stagiaire.objects.get(user_id=request.user.id)
        doc=satgiaire.document
        doc.rapport=request.FILES["rapport"]
        doc.save()
        return redirect('/stagiaire/mon_stage/')
