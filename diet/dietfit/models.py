from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

# class Food(models.Model):

def validate_weight(weight):
	if weight < 60 or weight > 999:
		raise ValidationError("Invalid weight")

class UserProfile(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female')
		)
	#user = models.OneToOneField(User)
	gender = models.CharField(max_length=1, choices = GENDER_CHOICES)
	weight = models.IntegerField(validators=[validate_weight])



