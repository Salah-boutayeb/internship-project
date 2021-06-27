from django.shortcuts import redirect, render

from stages.models import *
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.


login_required='/accounts/login/'

def show(request):
    stages=Stage.objects.all()   
    return render(request,'stages/show.html',{'stages':stages})


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
            #return render(request,'stages/create_taches.html',context={'charges':charges})
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
    print(stage.formateur.user.username)
    
    
    context={'stage':stage,}
    return render(request,'stages/stage_details.html',context )


def demande_stage(request):
    if  request.user.is_authenticated and request.user.is_stagiaire :
        if request.POST and not request.is_ajax():
            if request.FILES.get("cv") is not None:
                stagiaire=Stagiaire.objects.get(user=request.user)
                
                stage=Stage.objects.get(pk=request.POST['id'])
                
                document=Document()
                document.stagiaire=stagiaire
                document.cv=request.FILES["cv"]
                document.save()
                demande=Demande(stagiaire=stagiaire,stage=stage)
                demande.save()
                send_mail(
                '',
                f"\t Bonjour {stagiaire.user.last_name} {stagiaire.user.first_name} \n Vous avez postulé à l'annonce {stage.sujet} le {demande.created.strftime('%b %d %Y %H:%M:%S')}",
                User.objects.get(username='admin').email,
                [ request.user.email ],
                fail_silently=False,
                )
            return redirect('/')
        elif request.POST and request.is_ajax():
            stagiaire=Stagiaire.objects.get(user=request.user)
            stage=Stage.objects.get(pk=request.POST['id']) 
            doc=Demande.objects.filter(stagiaire_id=stagiaire.user_id ,stage_id=stage.id)
            print(doc,"hhhhhhhhhhhhhhhhhhhhhhhhh")
            if len(doc)>0:
                return JsonResponse({'data':'vous avez déjà postulé à ce stage '+stage.sujet}) 
            demande=Demande(stagiaire=stagiaire,stage=stage)
            demande.save()
            
            send_mail(
            '',
            f"\t Bonjour {stagiaire.user.last_name} {stagiaire.user.first_name}. \n Vous avez postulé à l'annonce {stage.sujet} ,le {demande.created.strftime('%b %d %Y %H:%M:%S')}",
            User.objects.get(username='admin').email,
            [ request.user.email ],
            fail_silently=False,
            )
            return JsonResponse({'data':'votre demande est en cours de traitment'})  
    else:
        return redirect(login_required) 


