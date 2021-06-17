from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from .forms import *
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
				return redirect('/')
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
        return redirect('/')

class stagiare_register(CreateView):
    model = User
    form_class = StagiaireSignUpForm
    template_name = 'registration/stagiaire_registre.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

