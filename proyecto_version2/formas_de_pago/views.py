
from django.shortcuts import render #CLASE 12 necesario para usar las plantillas
from django.template import loader #CLASE 12 necesario para usar las plantillas
from django.http import HttpResponse #CLASE 12 necesario para usar las plantillas
from datetime import datetime 

# Create your views here.

from django.http import HttpResponse # segun clase 10

#def index(request):
     #codigo
#     return HttpResponse("soy el index")

def formas_de_pago(request):                                                
    template = loader.get_template('formas_de_pago/formas-de-pago.html')   
    context = {"hoy":datetime.now}                                 
    return HttpResponse(template.render(context,request))

def alta_medio_de_pago(request):                                                
    template = loader.get_template('formas_de_pago/altamediodepago.html')   
    context = {}                                                        
    return HttpResponse(template.render(context,request))  


def baja_medio_de_pago(request):                                                
    template = loader.get_template('formas_de_pago/bajamediodepago.html')   
    context = {}                                                        
    return HttpResponse(template.render(context,request))  
