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
	if value < 1:
		raise ValidationError("Invalid value")


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


class Food(models.Model):
	name = models.CharField(max_length = 30, default="food")
	calories = models.IntegerField(validators=[validate_positive])
	fat = models.IntegerField(validators=[validate_positive])
	carbs = models.IntegerField(validators=[validate_positive])
	protein = models.IntegerField(validators=[validate_positive])

	def __str__(self):
		return self.name

class MealPlan(models.Model):
	foods = models.ManyToManyField(Food)


