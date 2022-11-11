
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
#from .models import Cargo
from django import forms
from django.views import View
from django.views.generic import ListView

####importacion de los forms de ejemplo####
from usuarios.forms import FormularioFiltrado

#def index(request):
     #codigo
#     return HttpResponse("soy el index")

def usuariosform(request):
    if request.method == 'POST':
        usuariosform = UsuariosForm(request.POST)
    else:
        usuariosform = UsuariosForm()
    return render(request, 'usuarios/usuariosform.html', {'usuariosform': usuariosform})

def resultadofiltro(request):
    # ejemplo basado en pildoras informaticas
    if request.method == 'POST':
         usuariosform = UsuariosForm(request.POST)
         if usuariosform.is_valid():
            nombre = request.POST["nombre"]
            apellido = request.POST["apellido"]
            email = request.POST["email"]
            usuarios=Usuario.objects.filter(nombre__icontains=nombre,apellido__icontains=apellido,email__icontains=email) #icontains seria LIKE en sql
    return render(request, "usuarios/resultadofiltro.html",{"usuarios":usuarios,"query":nombre,"usuariosform":usuariosform})
    
    # ejemplo visto en clase aun no logro hacerlo funcionar
    #               usuariosform = Usuario.objects.all().order_by('id') 
    #       return render(request, "usuarios/resultadofiltro.html",{"usuariosform":usuariosform})

def altausuarioform(request): 
    if request.method == 'POST':
        altausuarioform = AltaUsuarioForm(request.POST)
        if altausuarioform.is_valid():
            nombre = altausuarioform.cleaned_data['nombre']
            apellido = altausuarioform.cleaned_data['apellido']
            email = altausuarioform.cleaned_data['email']
            password = altausuarioform.cleaned_data['password']
    #       cargo = altausuarioform.cleaned_data['cargo']
            nuevo_usuario = Usuario(nombre=nombre,apellido=apellido,email=email,password=password)
            try:
                nuevo_usuario.save()
            except ValueError as ve:
                altausuarioform.add_error('apellido', str(ve))
            else:
                return redirect('altausuarioform')
    else:
        altausuarioform = AltaUsuarioForm()
        return render(request, 'usuarios/altausuarioform.html', {'altausuarioform': altausuarioform})


def bajausuarioform(request): 
    if request.method == 'POST':
        bajausuarioform = BajaUsuarioForm(request.POST)
        if bajausuarioform.is_valid():
            email = bajausuarioform.cleaned_data['email']
            password = bajausuarioform.cleaned_data['password']
    #       cargo = altausuarioform.cleaned_data['cargo']
            usuario_a_borrar= Usuario.objects.get(email=email,password=password)
            try:
                usuario_a_borrar.delete()
            except ValueError as ve:
                bajausuarioform.add_error('email', str(ve))
            else:
                return redirect('bajausuarioform')
    else:
        bajausuarioform = BajaUsuarioForm()
        return render(request, 'usuarios/bajausuarioform.html', {'bajausuarioform': bajausuarioform})





#Ejemplo visto en clase con boton y parametrizado
# def bajausuarioform(request,email_usuario): 
# #id_usuario):
#      try:
#          usuario=Usuario.objects.get(email=email_usuario)
#      except Usuario.DoesNotExist:
#          return render(request, "usuarios/404.html")

#      try:
#          usuario.delete()
#      except ValueError as ve:
#          messages.error(request=request,
#                         message="No se puede borrar al Gerente")
#      return redirect('usuariosform')    




##########EN EL FUTURO LOS FORMULARIOS DEBEN REDIRIGIR ACA ###########


def resultadoalta(request):
        mensaje = "Se dio de alta a %r" %request.POST["nombre"]
        return HttpResponse(mensaje)

def resultadobaja(request):
        mensaje="Se dio de baja a %r" %request.POST["nombre"]
        return HttpResponse(mensaje)




#######Ejemplo formulario 1

# def busqueda_productos(request):
#         return render(request, 'usuarios/busqueda_productos.html')

# def buscar(request):
#         mensaje="Se dio de alta a %r" %request.GET["prd"]
#         return HttpResponse(mensaje)


#######Ejemplo formulario 2 (con base de datos)###########

#def busqueda_productos(request):
#         return render(request, 'usuarios/busqueda_productos.html')

#def buscar(request):
#     if request.GET["prd"]:
#         #mensaje="Se dio de alta a %r" %request.GET["prd"]
#         producto = request.GET["prd"]
#         articulos=Articulos.objects.filter(nombre__icontains=producto) #icontains seria LIKE en sql
#         return render(request, "usuarios/resultados_busqueda.html",{"articulos":articulos,"query":producto})
#     else:
#         mensaje="no has introducido nada"
#     return HttpResponse(mensaje)

#######Ejemplo formulario 3 (con base de datos)###########

def busqueda_productos(request):
#         if request.method == 'POST':
#             miFormulario = FormularioFiltrado(request.GET)
#         else:
#             miFormulario = FormularioFiltrado()
         return render(request, 'usuarios/busqueda_productos.html',{'miFormulario':miFormulario})


def buscar(request):
     if request.method=="GET":
#         miFormulario=FormularioFiltrado(request.GET)

#         if miFormulario.is_valid():
#           producto = request.GET["nombre"]
#           articulos=Articulos.objects.filter(nombre__icontains=producto) #icontains seria LIKE en sql
           return render(request, "usuarios/resultados_busqueda.html",{"articulos":articulos,"query":producto,"miFormulario":miFormulario})

     else:
         miFormulario=FormularioFiltrado()    




