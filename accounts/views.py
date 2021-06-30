from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from .forms import *
from formateurs.models import ProfileFormateur
from stagiaire.models import ProfileStagiaire
from django.contrib.auth.forms import AuthenticationForm
from .models import User
# Create your views here.
def login_page(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/accounts/profile/'+request.user.username)
			else:
				messages.info(request, 'Username OR password is incorrect')
		context = {}
        
		return render(request,'login.html',context)
def logout_user(request):
	logout(request)
	return redirect('/')    

class formateur_register(CreateView):
    model = User
    form_class = FormateurSignUpForm
    template_name = 'registration/formateur_registre.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/profile/'+self.request.user.username)

class stagiare_register(CreateView):
    model = User
    form_class = StagiaireSignUpForm
    template_name = 'registration/stagiaire_registre.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/profile/'+self.request.user.username)

def profiles(request,name):
	if request.user.is_authenticated:
		user=User.objects.get(username=name)
		if user.is_stagiaire:
			profile=ProfileStagiaire.objects.get(user_id=user.id)
			axe_taches={}
			if  profile.user.user.stagiaire.is_active:
				stage = Stage.objects.get(stagiaire_id=user.id)
				axes=Axe.objects.filter(cahierCharge_id=stage.id)
				for axe in axes:
					axe_taches[axe]=[]
					taches = Tache.objects.filter(axe=axe)
					if taches:
						for tache in taches:
							axe_taches[axe].append(tache)
				return render(request,'profile.html',context={"profile":profile,"stage":stage ,"axes":axe_taches})	
		else:
			profile=ProfileFormateur.objects.get(user_id=user.id)	
			stages = Stage.objects.filter(formateur_id=user.id)  
			return render(request,'profile.html',context={"profile":profile,"stages":stages})				
		return render(request,'profile.html',context={"profile":profile})	
	else :
		return redirect('/accounts/login')

def edite(request):
	if request.user.is_authenticated:
		
		if request.POST:
			obj=request.POST
			user=User.objects.get(id=request.user.id)
			user.first_name=obj['first_name']
			user.last_name=obj['last_name']
			user.email=obj['email']
			user.save()
			if request.user.is_stagiaire:
				stagiare=user.stagiaire
				stagiare.phone_number=obj['telephone']
				stagiare.save()
				prof=stagiare.profilestagiaire
				prof.linkedin=obj['linkedin']
				if request.FILES.get("docs") is not None:	
					doc=stagiare.document
					doc.cv=request.FILES['docs']
					doc.save()
				if request.FILES.get("avatar") is not None:	
					prof.avatar=request.FILES["avatar"]
				prof.bio=obj['bio']	
				prof.save()	
			else:
				formateure=user.formateur
				formateure.phone_number=obj['telephone']
				formateure.save()
				prof=formateure.profileformateur
				prof.linkedin=obj['linkedin']
				if request.FILES:
					prof.avatar=request.FILES['avatar']
					prof.bio=obj['bio']
					prof.save()
		
		
		return redirect('/accounts/profile/'+request.user.username)		