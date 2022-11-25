from ast import Index
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect  # segun la clase de forms
from django.shortcuts import render  # segun la clase de forms
from .forms import IndexForm  # segun la clase de forms
from django import forms

from django.contrib.auth.forms import AuthenticationForm


# def index(request):
#     context = {"hoy": datetime.now}
#     marca = 'Pig Crm'

#     return render(request, 'login/index.html', {"marca": marca, "context": context})

def indexform(request):
    if request.method == 'POST':
        indexform = IndexForm(request.POST)
        # if login_form.is_valid():
        #     messages.info(request, "Info importante")
    else:
        indexform =IndexForm()
    return render(request, 'login/indexform.html', {'indexform': indexform})

def index(request):
    form=AuthenticationForm()
    return render(request,'login/index.html',{"form":form})
