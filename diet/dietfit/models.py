from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Food(models.Model):

class UserProfile(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female')
		)
	user = models.OneToOneField(User)
	gender = models.CharField(max_length=1)
