from django.shortcuts import *
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.db.models import Sum
from dietfit.forms import *
from dietfit.models import *
import random

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
			loss_goal = request.POST['loss_goal']

			if gender == 'M':
				caloriecalculator = calorie_calculate(male_calculate(height_ft, height_inch, weight, age))
				calories = caloriecalculator.calculate
			else:
				caloriecalculator = calorie_calculate(female_calculate(height_ft, height_inch, weight, age))
				calories = caloriecalculator.calculate

			if loss_goal == '1':
				calories = calories - 250
			elif loss_goal == '2':
				calories = calories- 500

			useracc = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
			mealplanobj = MealPlan.objects.create(owner = request.POST['username'])
			mealplanobj.save()
			exerciseplanobj = ExercisePlan.objects.create(owner= request.POST['username'])
			userprofile = UserProfile.objects.create(mealplan=mealplanobj, calorie_goal=calories, user=useracc, age=request.POST['age'], gender=request.POST['gender'], height_ft=request.POST['height_ft'], height_inch=request.POST['height_inch'], weight=request.POST['weight'], loss_goal=request.POST['loss_goal'], exerciseplan=exerciseplanobj)
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
	return render_to_response("home.html", {"exercisebase": ExerciseBase.objects.all()}, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def addmeal(request):
	return render_to_response("addmeal.html", context_instance=RequestContext(request))

def mealadded_view(request):
	if request.method == 'POST':
		foodform = FoodForm(request.POST)
		if foodform.is_valid():
			serving = str(request.POST['servingsize'] + ' ' + request.POST['servingunit'])
			newfood = Food.objects.create(ourfood=False, name=request.POST['name'], calories=request.POST['calories'], fat=request.POST['fat'], carbs=request.POST['carbs'], protein=request.POST['protein'], servingsize=serving)
			newfood.save()
			request.user.userprofile.mealplan.foods.add(newfood)
			return HttpResponseRedirect("/home")
		else:
			return HttpResponseRedirect("/home")

def exerciseadded_view(request):
	base_exercise = ExerciseBase.objects.get(id=request.POST['exerciseid'])
	new_user_exercise = UserExercise.objects.create(exercisebase=base_exercise, duration=request.POST['exerciseduration'])
	new_user_exercise.save()
	request.user.userprofile.exerciseplan.exercises.add(new_user_exercise)
	return HttpResponseRedirect("/home")


def generate_view(request):
	deficit = request.user.userprofile.deficit
	ourfoods = Food.objects.filter(ourfood=True)
	while deficit > 0:
	 	rand = int(random.random()*len(ourfoods))
	 	if deficit - ourfoods[rand].calories > -150:
	 		request.user.userprofile.mealplan.foods.add(ourfoods[rand])
	 		deficit = deficit - ourfoods[rand].calories
	return HttpResponseRedirect("/home")

def reset_food(request):
	request.user.userprofile.mealplan.delete()
	mealplanobj = MealPlan.objects.create(owner = request.user.username)
	mealplanobj.save()
	request.user.userprofile.mealplan = mealplanobj
	request.user.userprofile.save()
	return HttpResponseRedirect("/home")
	
# def reset_exercise(request):
# 	request.user.userprofile.exerciseplan.delete()
# 	exerciseplanobj = ExercisePlan.objects.create(owner = request.user.username)
# 	exerciseplanobj.save()
# 	request.user.userprofile.exerciseplan