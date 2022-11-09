
from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect
from django.urls import reverse

from django.template import loader
from django.contrib import messages

from django.views import View
from django.views.generic import ListView
from .forms import UsuariosForm  # segun la clase de forms
from .forms import AltaUsuarioForm
from .forms import BajaUsuarioForm
from .models import Articulos, Usuario
from .models import Cargo
from django import forms

####importacion de los forms de ejemplo####
##???????###


#def index(request):
     #codigo
#     return HttpResponse("soy el index")

def usuariosform(request):
    if request.method == 'POST':
        usuariosform = UsuariosForm(request.POST)
    else:
        usuariosform = UsuariosForm()
    return render(request, 'usuarios/usuariosform.html', {'usuariosform': usuariosform})

def altausuarioform(request): 
    #  if request.method == 'POST':
    #     altausuarioform = AltaUsuarioForm(request.POST)
    #     if altausuarioform.is_valid():
    #         nombre = altausuarioform.cleaned_data['nombre']
    #         apellido = altausuarioform.cleaned_data['apellido']
    #         email = altausuarioform.cleaned_data['email']
    #         password = altausuarioform.cleaned_data['password']
    #         cargo = altausuarioform.cleaned_data['cargo']
    #         nuevo_usuario = Usuario(nombre=nombre,apellido=apellido,email=email,password=password,cargo=cargo)
    #         nuevo_usuario.save()
    #         return redirect('usuariosform')
    #  else:
    #      altausuarioform = AltaUsuarioForm()
     return render(request, 'usuarios/altausuarioform.html', {'altausuarioform': altausuarioform})

def bajausuarioform(request):
    if request.method == 'POST':
        bajausuarioform = BajaUsuarioForm(request.GET)
    else:
        bajausuarioform = BajaUsuarioForm()
    return render(request, 'usuarios/bajausuarioform.html', {'bajausuarioform': bajausuarioform})

def resultadoalta(request):
        mensaje = "Se dio de alta a %r" %request.GET["nombre"]
        return HttpResponse(mensaje)

def resultadobaja(request):
        mensaje=""
        return HttpResponse(mensaje, 'usuarios/resultadobaja.html')

def resultadofiltro(request):
        mensaje=""
        return HttpResponse(mensaje, 'usuarios/resultadofiltro.html')



#######Ejemplo formulario 1

# def busqueda_productos(request):
#         return render(request, 'usuarios/busqueda_productos.html')

# def buscar(request):
#         mensaje="Se dio de alta a %r" %request.GET["prd"]
#         return HttpResponse(mensaje)


#######Ejemplo formulario 2 (con base de datos)###########

def busqueda_productos(request):
        return render(request, 'usuarios/busqueda_productos.html')

def buscar(request):
    if request.GET["prd"]:
        #mensaje="Se dio de alta a %r" %request.GET["prd"]
        producto = request.GET["prd"]
        articulos=Articulos.objects.filter(nombre__icontains=producto) #icontains seria LIKE en sql
        return render(request, "usuarios/resultados_busqueda.html",{"articulos":articulos,"query":producto})
    else:
        mensaje="no has introducido nada"
    return HttpResponse(mensaje)

