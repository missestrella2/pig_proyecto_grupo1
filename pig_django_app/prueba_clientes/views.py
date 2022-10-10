from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse # segun clase 10

def index(request):
     #codigo
     return HttpResponse("los clientes")
