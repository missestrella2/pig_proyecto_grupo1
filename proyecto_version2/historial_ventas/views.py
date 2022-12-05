
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect  # segun la clase de forms
from django.shortcuts import render  # segun la clase de forms


#def index(request):
     #codigo
#     return HttpResponse("soy el index")

def historial_ventas(request):                                                #asi se cargan los templates
    template = loader.get_template('historial_ventas/historial-ventas.html')   #crea objeto template que trae a index.html
    context = {"hoy":datetime.now}                                 #creo context que es un diccionario
    return HttpResponse(template.render(context,request))
