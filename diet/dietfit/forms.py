from django import forms

class RegistrationForm(forms.Form):
	username = forms.CharField(label='username', max_length=10)
	email = forms.EmailField()
	password = forms.CharField(label='password')
