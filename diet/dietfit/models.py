from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.

# class Food(models.Model):

def validate_weight(weight):
	if weight < 60 or weight > 999:
		raise ValidationError("Invalid weight")

def validate_age(age):
	if age < 14 or age > 99:
		raise ValidationError("Invalid age")

def validate_height_ft(ft):
	if ft < 4 or ft > 7:
		raise ValidationError("Invalid height ft")

def validate_height_inch(inch):
	if inch < 0 or inch > 12:
		raise ValidationError("Invalid height inch")

def validate_positive(value):
	if value < 0:
		raise ValidationError("Invalid value")

class Food(models.Model):
	name = models.CharField(max_length = 30, default="food")
	calories = models.FloatField(validators=[validate_positive])
	fat = models.FloatField(validators=[validate_positive])
	carbs = models.FloatField(validators=[validate_positive])
	protein = models.FloatField(validators=[validate_positive])
	ourfood = models.BooleanField(default=False)

	def __str__(self):
		return self.name



class MealPlan(models.Model):
	foods = models.ManyToManyField(Food, unique=False)
	owner = models.CharField(max_length=14, default= "")

	def __str__(self):
		return "mealplan of " + self.owner

	@property
	def totalcals(self):
	    sum = self.foods.aggregate(models.Sum('calories'))['calories__sum']
	    if sum == None:
	    	return 0
	    return sum

	@property
	def totalfat(self):
	    sum = self.foods.aggregate(models.Sum('fat'))['fat__sum']
	    if sum == None:
	    	return 0
	    return sum

	@property
	def totalcarbs(self):
	    sum = self.foods.aggregate(models.Sum('carbs'))['carbs__sum']
	    if sum == None:
	    	return 0
	    return sum

	@property
	def totalprotein(self):
	    sum = self.foods.aggregate(models.Sum('protein'))['protein__sum']
	    if sum == None:
	    	return 0
	    return sum
	



class UserProfile(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female')
		)
	user = models.OneToOneField(User, default=1)
	age = models.IntegerField(validators=[validate_age], default=18)
	gender = models.CharField(max_length=1, choices = GENDER_CHOICES, default='M')
	height_ft = models.IntegerField(validators=[validate_height_ft], default=5)
	height_inch = models.IntegerField(validators=[validate_height_inch], default=9)
	weight = models.IntegerField(validators=[validate_weight], default=150)
	calorie_goal = models.IntegerField(validators=[validate_positive], default=1500)
	mealplan = models.OneToOneField(MealPlan)
	loss_goal = models.IntegerField(validators=[validate_positive], default=0)

	@property
	def deficit(self):
		return self.calorie_goal - self.mealplan.totalcals




