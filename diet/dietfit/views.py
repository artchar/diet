from django.shortcuts import *
from django.template import RequestContext, loader

from django.http import *
from dietfit.forms import *


def account_creation(request):
	template = loader.get_template('account_creation.html')
	output = template.render(request)
	return render_to_response("account_creation.html", context_instance=RequestContext(request))

def homepage(request):
	template = loader.get_template('index.html')
	output = template.render()
	return HttpResponse(output)

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

