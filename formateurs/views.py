from django.contrib import messages
from django.core.mail import send_mail
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from stages.models import *

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



# Create your views here.
login_required='/accounts/login/'
def show_demande(request):
    if request.user.is_authenticated and request.user.is_formateur:
        if request.POST:
            formateur=Formateur.objects.get(user_id=request.user.id)
            demande=Demande.objects.get(pk=request.POST['id'])
            stagiaire=demande.stagiaire
            stagiaire.is_active=True
            stage=demande.stage
            stage.stagiaire=stagiaire
            stage.occupe=True
            stagiaire.departement=formateur.specialite.departement
            stagiaire.formateur_id= request.user.id
            stagiaire.save()
            stage.save()
            demande.delete()
            
            send_mail('Acceptation de votre demande stage',
            f"\t\t Bonjour {stagiaire.user.last_name} {stagiaire.user.first_name}.\n Congratulation vous étes accepté(e) pour passer le stage '{stage.sujet}' , vous pouvez maintenant consulter le cahier des charges sur notre site\n Pour plus d'information n'hésitez pas de nous contacter , votre formateur(e) {request.user.formateur.user.last_name} {request.user.formateur.user.first_name}: {request.user.formateur.user.email}.\n BON CHANCE.",
            User.objects.get(id=request.user.id).email,
            [ stagiaire.user.email ],
            fail_silently=False,
            )
            redirect('/formateur/demandes/')
        demandes=[]
        for demande in Demande.objects.all():
            if demande.stage.formateur_id == request.user.id:
                demandes.append(demande)
        return render(request,'demande.html',context={'demandes':demandes})
    else:
        return redirect(login_required)

def show_stagiaires(request):
    if request.user.is_authenticated and request.user.is_formateur:
        data=[]
      
        stages=Stage.objects.filter(formateur_id=request.user.id)
        for stage in stages:
            if stage.occupe:
                data.append(stage)
        context={'stages':data}         
        
        return render(request,'stagiaires.html',context)
    else:
        return redirect(login_required)

def create_stage(request):
    if request.user.is_authenticated and request.user.is_formateur :
        if request.POST:
            owner_name= request.user
            obj=request.POST
            if obj['stage_sujet'] and obj['description-stage'] and obj['cahiercharge-stage'] and obj['stage_type'] and obj['duree'] and obj['Nombre_du_stagiaires'] and obj['remunere']:
                formateur =Formateur.objects.get(user=owner_name)
                if obj['remunere'] =='False':
                    stage=Stage(sujet=obj['stage_sujet'],description_du_stage=obj['description-stage'],duree=obj['duree'],remunere=False,nombre_de_stagiaire=obj['Nombre_du_stagiaires'],type_de_stage=obj['stage_type'],formateur=formateur)
                    stage.save()
                else:
                    stage=Stage(sujet=obj['stage_sujet'],description_du_stage=obj['description-stage'],duree=obj['duree'],remunere=True,nombre_de_stagiaire=obj['Nombre_du_stagiaires'],type_de_stage=obj['stage_type'],formateur=formateur)
                    stage.save()
                charges=CahierCharge(stage=stage,cahierCharge=obj['cahiercharge-stage'])
                charges.save()
                return redirect('/')
                # return render(request,'stages/create_taches.html',context={'charges':charges})
            else:
                messages.info(request, "s'il vous plait ajouter un stage !!!")
        return render(request,'create_stage.html')
    else:
        return redirect(login_required) 
def update_stage(request,id):
    if request.user.is_authenticated and request.user.is_formateur :    
        if request.POST:
            obj = request.POST
            stage = Stage.objects.get(id=id)
            charges=CahierCharge.objects.get(stage_id=stage.id)
            if obj['remunere'] =='False':
                stage.sujet=obj['stage_sujet']
                stage.description_du_stage=obj['description-stage']
                stage.duree=obj['duree']
                stage.remunere=False
                stage.nombre_de_stagiaire=obj['Nombre_du_stagiaires']
                stage.type_de_stage=obj['stage_type']
                charges.cahierCharge=obj['cahiercharge-stage']
                print(1,charges.cahierCharge,stage.cahiercharge.cahierCharge)
                stage.cahiercharge.cahierCharge=obj['cahiercharge-stage']
                stage.save()
                charges.save()
            else:
                stage.sujet=obj['stage_sujet']
                stage.description_du_stage=obj['description-stage']
                stage.duree=obj['duree']
                stage.remunere=True
                stage.nombre_de_stagiaire=obj['Nombre_du_stagiaires']
                stage.type_de_stage=obj['stage_type']
                charges.cahierCharge=obj['cahiercharge-stage']
                stage.cahiercharge.cahierCharge=obj['cahiercharge-stage']               
                stage.save()
                charges.save()
        return redirect('/formateur/mes_stages/')      

def delete_stage(request,id):
    if request.user.is_authenticated and request.user.is_formateur :    
        if request.POST:
           stage= Stage.objects.get(id=id)  
           stagiaire=stage.stagiaire
           stagiaire.is_active=False
           stagiaire.formateur_id=None
           stagiaire.score=0
           stagiaire.save()
           stage.delete()          
        return redirect('/formateur/mes_stages/')        

def mes_stages(request):
    if request.user.is_authenticated and request.user.is_formateur:   
        stages = Stage.objects.filter(formateur_id=request.user.id)    
        return render(request,'update_stage.html',context={'stages':stages})         
def delete_stagiaire(request):
     if request.user.is_authenticated and request.user.is_formateur and request.POST :   
        stage=Stage.objects.get(stagiaire_id=request.POST['id'])
        stage.cahiercharge.axe_set.all().delete()

        stagiaire=stage.stagiaire
        stage.occupe=False
        stage.stagiaire=None
        
        stagiaire.is_active=False
        stagiaire.formateur_id=None
        stagiaire.score=0
        stagiaire.save()
        stage.save()
        send_mail("notifications d'exclusion",
            f"\t\t Bonjour {stagiaire.user.last_name} {stagiaire.user.first_name}.\n nous excusons  de vous informer que vous étes exclus du stage '{stage.sujet}' , vu que vous n'avez pas encore commencer votre project,ainsi que vous n'avez pas respecter la date pour nous envoyer votre rapport  .\n BON CHANCE.",
            User.objects.get(id=request.user.id).email,
            [ stagiaire.user.email ],
            fail_silently=False,
            )
        return redirect('/formateur/stagiaires/')
def delete_demande(request):
     if request.user.is_authenticated and request.user.is_formateur and request.POST :   
        Demande.objects.get(id=request.POST['id']).delete()
        
        return redirect('/formateur/stagiaires/')        


def stagiaireprogress(request,id):
    done=0
    not_done=100
    if request.user.is_authenticated  and request.is_ajax():
       
        totale=0
        stage = Stage.objects.get(stagiaire_id=id)
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
            stagiaire = Stagiaire.objects.get(user_id=id)
            stagiaire.score=done
            stagiaire.save()                       
        return JsonResponse({'data':{'progress':[{'done':done},{'not done':not_done}],'done':done}})
    else:
        return JsonResponse({'data':{'progress':[{'done':done},{'not done':not_done}]},'id':id})    


def send_attestation(request):
    if request.user.is_authenticated and request.user.is_formateur and request.POST:
        if request.FILES.get("attestation") is not None:
            attestation=request.FILES['attestation']
            stag_id = request.POST['id']
            doc=Document.objects.get(stagiaire_id=stag_id)
            doc.attestation=attestation
            doc.save()
        return redirect('/formateur/stagiaires')    
    else:
        return redirect('/')    