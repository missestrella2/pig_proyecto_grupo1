from django.shortcuts import render

# Create your views here.

from django.template import loader #CLASE 12 necesario para usar las plantillas
from django.http import HttpResponse #CLASE 12 necesario para usar las plantillas
from datetime import datetime 
from django.http import HttpResponse # segun clase 10

def clientes(request):                                                #asi se cargan los templates
    template = loader.get_template('clientes/clientes.html')   #crea objeto template que trae a clientes.html
    context = {"hoy":datetime.now, 
               "nombre": "Bienvenido/a %r" %request.GET["elnombre"] }                                 #creo context que es un diccionario
            #aca dentro de context crear un diccionario que despues voy a  llamar desde la template usando las llaves
    return HttpResponse(template.render(context,request))

def altaclientes(request):                                                
    template = loader.get_template('clientes/altaclientes.html')   
    context = {}                                                        
    return HttpResponse(template.render(context,request))  

def bajaclientes(request):                                                
    template = loader.get_template('clientes/bajaclientes.html')   
    context = {}                                                        
    return HttpResponse(template.render(context,request))  



def clientes_listado_completo(request):                                                
    template = loader.get_template('clientes/clientes-listado-completo.html')   
    context = {}                                                        
    return HttpResponse(template.render(context,request))  



def clientes_por_anio_de_alta(request,anio):
   template = loader.get_template('clientes/clientes-por-anio-de-alta.html')  
   context = {}                                                        
   return HttpResponse(template.render(context,request))  

                                          

