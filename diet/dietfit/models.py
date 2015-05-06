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



