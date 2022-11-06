from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect  # segun la clase de forms
from django.shortcuts import render  # segun la clase de forms
from .forms import UsuariosForm  # segun la clase de forms
from .forms import AltaUsuarioForm
from .forms import BajaUsuarioForm
from django import forms

#def index(request):
     #codigo
#     return HttpResponse("soy el index")

def usuarios(request):                                                
    template = loader.get_template('usuarios/usuarios.html')   
    context = {"hoy":datetime.now}                                 
    return HttpResponse(template.render(context,request))

def usuariosform(request):
    if request.method == 'POST':
        usuariosform = UsuariosForm(request.POST)
        # if login_form.is_valid():
        #     messages.info(request, "Info importante")
    else:
        usuariosform = UsuariosForm()
    return render(request, 'usuarios/usuariosform.html', {'usuariosform': usuariosform})

def altausuarioform(request): 
     if request.method == 'POST':
         altausuarioform = AltaUsuarioForm(request.POST)
        #  if login_form.is_valid():
        #       messages.info(request, "Info importante")
     else:
         altausuarioform = AltaUsuarioForm()
     return render(request, 'usuarios/altausuarioform.html', {'altausuarioform': altausuarioform})

def bajausuarioform(request):
    if request.method == 'POST':
        bajausuarioform = BajaUsuarioForm(request.POST)
        # if login_form.is_valid():
        #     messages.info(request, "Info importante")
    else:
        bajausuarioform = BajaUsuarioForm()
    return render(request, 'usuarios/bajausuarioform.html', {'bajausuarioform': bajausuarioform})