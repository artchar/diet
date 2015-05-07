from django.shortcuts import *
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.http import *
from dietfit.forms import *


class calorie_calculate:
	def __init__(self, gender=None):
		if gender:
			self.calculate = gender
	def calculate(self):
		pass

def male_calculate(height_ft, height_inch, weight, age):
	combined_height = int(height_ft)*12 + int(height_inch)
	return int(66.47 +(13.75*(int(weight)/2.2)) + (5*(combined_height * 2.54)) - (6.75 * int(age)))

def female_calculate(height_ft, height_inch, weight, age):
	combined_height = int(height_ft)*12 + int(height_inch)
	return int(665.09 + (9.56*(int(weight)/2.2)) + (1.84*(combined_height * 2.54)) - (4.67 * int(age)))


def account_creation(request):
	return render_to_response("account_creation.html", context_instance=RequestContext(request))

def index(request):
	return render_to_response("index.html", context_instance=RequestContext(request))

def register(request):
	if request.method == 'POST':
		userprofileform = RegistrationForm(request.POST)
		baseuserform = UserForm(request.POST)
		if userprofileform.is_valid() and baseuserform.is_valid():
			gender = request.POST['gender']
			height_ft = request.POST['height_ft']
			height_inch = request.POST['height_inch']
			age = request.POST['age']
			weight = request.POST['weight']

			if gender == 'M':
				caloriecalculator = calorie_calculate(male_calculate(height_ft, height_inch, weight, age))
				calories = caloriecalculator.calculate
			else:
				caloriecalculator = calorie_calculate(female_calculate(height_ft, height_inch, weight, age))
				calories = caloriecalculator.calculate

			useracc = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
			userprofile = UserProfile.objects.create(calorie_goal=calories, user=useracc, age=request.POST['age'], gender=request.POST['gender'], height_ft=request.POST['height_ft'], height_inch=request.POST['height_inch'], weight=request.POST['weight'])
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
