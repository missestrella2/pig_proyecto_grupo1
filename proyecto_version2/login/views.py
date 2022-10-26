from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect  # segun la clase de forms
from django.shortcuts import render  # segun la clase de forms
from .forms import LoginForm  # segun la clase de forms
from django import forms


def index(request):
    context = {"hoy": datetime.now}
    marca = 'Pig Crm'
    return render(request, 'login/index.html', {"marca": marca, "context": context})

def login_form(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        # if login_form.is_valid():
        #     messages.info(request, "Info importante")
    else:
        login_form =LoginForm()
    return render(request, 'login/login-form.html', {'login_form': login_form})
