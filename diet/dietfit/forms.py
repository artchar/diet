from django.forms import ModelForm
from django.contrib.auth.models import User
from dietfit.models import UserProfile

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email']

class RegistrationForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['age', 'gender', 'height_ft', 'height_inch', 'weight']

