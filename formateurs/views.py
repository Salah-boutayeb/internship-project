from django.shortcuts import redirect, render
from stagiaire.models import Stagiaire
from .models import *
from stages.models import *
# Create your views here.
login_required='/login/'
def show_demande(request):
    if request.user.is_authenticated and request.user.is_formateur:
        if request.POST:
            print(request.POST['id'])
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
        # if request.POST:
        #     formateur=Formateur.objects.get(user=request.user)
        #     stages=formateur.stage_set.all()
        #     print(stages)
        #     redirect('/formateur/stagiaires/')
        data=[]
        
        stagiaires=Stagiaire.objects.all()
        for stagiaire in stagiaires:
            stg={}
            stg['id']=stagiaire.user_id
            stages=stagiaire.stage_set.all()
            for stage in stages:
                    stg['stage']=stage.sujet
            stg["name"]=stagiaire.user
            documents=stagiaire.document_set.all()
            for document in documents:
                    stg['cv']=document.cv
            data.append(stg)   
        context={'stagiaires':data}         
        print(context)
        return render(request,'stagiaires.html',context)
    else:
        return redirect(login_required)
