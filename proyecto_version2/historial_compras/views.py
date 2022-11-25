
from django.shortcuts import render #CLASE 12 necesario para usar las plantillas
from django.template import loader #CLASE 12 necesario para usar las plantillas
from django.http import HttpResponse #CLASE 12 necesario para usar las plantillas
from datetime import datetime 

# Create your views here.

from django.http import HttpResponse 

def historial_compras(request):                                                
    template = loader.get_template('historial_compras/historial-compras.html')   
    context = {"hoy":datetime.now}                                 
    return HttpResponse(template.render(context,request))



