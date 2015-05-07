from django.shortcuts import *
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.http import *
from dietfit.forms import *


def account_creation(request):
	return render_to_response("account_creation.html", context_instance=RequestContext(request))

def index(request):
	return render_to_response("index.html", context_instance=RequestContext(request))

def register(request):
	if request.method == 'POST':
		userprofileform = RegistrationForm(request.POST)
		baseuserform = UserForm(request.POST)
		if userprofileform.is_valid() and baseuserform.is_valid():
			useracc = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
			userprofile = UserProfile.objects.create(user=useracc, age=request.POST['age'], gender=request.POST['gender'], height_ft=request.POST['height_ft'], height_inch=request.POST['height_inch'], weight=request.POST['weight'])
			userprofile.save()
		return HttpResponseRedirect('/register_success')
	else:
		return HttpResponseRedirect('/')

def register_success(request):
		return render_to_response("register_success.html")

def loginuser(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect("/home")
			else:
				return HttpResponseRedirect("/")
		else:
			return HttpResponseRedirect("/")
	else:
		return HttpResponse("invalid")

def home(request):
	return render_to_response("home.html", context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")
