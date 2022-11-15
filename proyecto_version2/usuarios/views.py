from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from usuarios.forms import UsuariosForm, AltaUsuarioForm, BajaUsuarioForm
from django.contrib import messages

from usuarios.models import Usuario
from django.views import View
from django.views.generic import ListView

class ListaDeUsuarios(ListView):
    model = Usuario 
    context_object_name = 'usuarios'
    template_name = 'usuarios/listadeusuarios.html'
    ordering =['id']

def usuarioeditar(request, id_usuario):
    try:
        usuario = Usuario.objects.get(id=id_usuario)
    except Usuario.DoesNotExist:
        return render(request, 'usuarios/404.html')
    
    if request.method == "POST":
        formulario = UsuariosForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect('listadeusuarios')
    else:
        formulario = UsuariosForm(instance=usuario)

    return render(request, 'usuarios/usuarioeditar.html', {'formulario': formulario, 'id_usuario': id_usuario})


def usuarioeliminar(request, id_usuario):
    try:
        usuario = Usuario.objects.get(id=id_usuario)
    except Usuario.DoesNotExist:
        return render(request, 'usuarios/404.html')
    
    try:
        usuario.delete()
    except ValueError as ve:
        messages.error(request=request, message="no se puede borrar")
    return redirect('listadeusuarios')


# def resultadofiltro(request):
#     # ejemplo basado en pildoras informaticas
#     if request.method == 'POST':
#          usuariosform = UsuariosForm(request.POST)
#          if usuariosform.is_valid():
#             nombre = request.POST["nombre"]
#             apellido = request.POST["apellido"]
#             email = request.POST["email"]
#             usuarios=Usuario.objects.filter(nombre__icontains=nombre,apellido__icontains=apellido,email__icontains=email) #icontains seria LIKE en sql
#     return render(request, "usuarios/resultadofiltro.html",{"usuarios":usuarios,"query":nombre,"usuariosform":usuariosform})
    
#     # ejemplo visto en clase aun no logro hacerlo funcionar
#     #               usuariosform = Usuario.objects.all().order_by('id') 
#     #       return render(request, "usuarios/resultadofiltro.html",{"usuariosform":usuariosform})

class altausuarioform(View):
    form_class = AltaUsuarioForm
    template_name = 'usuarios/altausuarioform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadeusuarios')

        return render(request, self.template_name, {'formulario': form})

class bajausuarioform(View):
    form_class = BajaUsuarioForm
    template_name = 'usuarios/bajausuarioform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadeusuarios')

        return render(request, self.template_name, {'formulario': form})

# def altausuarioform(request): 
#      if request.method == 'POST':
#          altausuarioform = AltaUsuarioForm(request.POST)
#          if altausuarioform.is_valid():
#              nombre = altausuarioform.cleaned_data['nombre']
#              apellido = altausuarioform.cleaned_data['apellido']
#              email = altausuarioform.cleaned_data['email']
#              password = altausuarioform.cleaned_data['password']
#      #       cargo = altausuarioform.cleaned_data['cargo']
#              nuevo_usuario = Usuario(nombre=nombre,apellido=apellido,email=email,password=password)
#              try:
#                  nuevo_usuario.save()
#              except ValueError as ve:
#                  altausuarioform.add_error('apellido', str(ve))
#              else:
#                  return redirect('altausuarioform')
#      else:
#          altausuarioform = AltaUsuarioForm()
#          return render(request, 'usuarios/altausuarioform.html', {'altausuarioform': altausuarioform})


# def bajausuarioform(request): 
#      if request.method == 'POST':
#          bajausuarioform = BajaUsuarioForm(request.POST)
#          if bajausuarioform.is_valid():
#              email = bajausuarioform.cleaned_data['email']
#              password = bajausuarioform.cleaned_data['password']
#      #       cargo = altausuarioform.cleaned_data['cargo']
#              try:
#                  usuario_a_borrar= Usuario.objects.get(email=email,password=password)
#              except Usuario.DoesNotExist:
#                  return render(request, "usuarios/404.html")

#              try:
#                  usuario_a_borrar.delete()
#              except ValueError as ve:
#                  bajausuarioform.add_error('email', str(ve))
#              else:
#                  return redirect('bajausuarioform')
#      else:
#          bajausuarioform = BajaUsuarioForm()
#          return render(request, 'usuarios/bajausuarioform.html', {'bajausuarioform': bajausuarioform})
