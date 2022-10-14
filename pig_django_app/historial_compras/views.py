
from django.shortcuts import render #CLASE 12 necesario para usar las plantillas
from django.template import loader #CLASE 12 necesario para usar las plantillas
from django.http import HttpResponse #CLASE 12 necesario para usar las plantillas
from datetime import datetime 

# Create your views here.

from django.http import HttpResponse # segun clase 10

#def index(request):
     #codigo
#     return HttpResponse("soy el index")

def historial_compras(request):                                                #asi se cargan los templates
    template = loader.get_template('historial_compras/historial-compras.html')   #crea objeto template que trae a index.html
    context = {"hoy":datetime.now}                                 #creo context que es un diccionario
    return HttpResponse(template.render(context,request))


