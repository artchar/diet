from django.shortcuts import render
from django.template import RequestContext, loader

from django.http import *
from dietfit.forms import *


def account_creation(request):
	template = loader.get_template('account_creation.html')
	output = template.render(request)
	return HttpResponse(output)

def homepage(request):
	template = loader.get_template('index.html')
	output = template.render()
	return HttpResponse(output)

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			return render('/', {'form': form}, context_instance=RequestContext(request))
	else:
		return render('/', {'form': form}, context_instance=RequestContext(request))

