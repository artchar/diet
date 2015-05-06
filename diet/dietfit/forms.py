from django.forms import ModelForm
from dietfit.models import UserProfile

class RegistrationForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['user', 'age', 'gender', 'height_ft', 'height_inch', 'weight']
		
