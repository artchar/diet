from django.shortcuts import render
from django.template import RequestContext, loader

from django.http import HttpResponse


def account_creation(request):
	template = loader.get_template('account_creation.html')
	output = template.render()
	return HttpResponse(output)

def homepage(request):
	template = loader.get_template('index.html')
	output = template.render()
	return HttpResponse(output)

