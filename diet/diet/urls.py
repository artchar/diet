"""diet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from dietfit.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create_account/', account_creation),
    url(r'^register/', register),
    url(r'^register_success/', register_success),
    url(r'^home/', home),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'index.html'}),
    url(r'^addmeal/', addmeal),
    url(r'^logout/', logout_view),
    url(r'^mealadded/', mealadded_view),
    url(r'^generate/', generate_view),
    url(r'^resetfood/', reset_food),
    url(r'^exerciseadded/', exerciseadded_view),
    url(r'^weightadded/', weightadded_view),
    url(r'^resetexercise/', reset_exercise),
    url(r'^changeminutes/', changeminutes),
    url(r'^changeintensity/', changeintensity),
    url(r'^resetweight/', reset_weight)

    #url(r'^resetexercise/', reset_exercise)

]
