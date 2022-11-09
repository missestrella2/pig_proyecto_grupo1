from django.db import models
from ast import mod
from email.policy import default
from tabnanny import verbose
from django.db import models

class Cargo(models.Model):
    nombre= models.CharField(max_length=100,default=" ", verbose_name='Nombre')
    baja=models.BooleanField(default=False)

class Usuario(models.Model):
    nombre= models.CharField(max_length=100, default=" ", verbose_name='Nombre')
    apellido= models.CharField(max_length=100, null=True, verbose_name='Apellido')
    email= models.EmailField(max_length=150, verbose_name='Email')
    password= models.CharField(max_length=50, verbose_name='Password')
    fechadealta=models.DateField(verbose_name='Fecha de Alta')
    cargo = models.ForeignKey(Cargo,default="",on_delete=models.CASCADE)


##############Ejemplo###########

class Clientes(models.Model):
    nombre= models.CharField(max_length=100, default=" ", verbose_name='Nombre')
    direccion= models.CharField(max_length=100, null=True, verbose_name='Direccion')
    email= models.EmailField(max_length=150, verbose_name='Email')

class Articulos(models.Model):
    nombre= models.CharField(max_length=100, default=" ", verbose_name='Nombre')
    seccion= models.CharField(max_length=100, default=" ", verbose_name='Seccion')
    precio=models.IntegerField()

#luego de hacer makemigration y migrate, ingrese articulos entrando a terminal
#escribi python manage.py shell_plus
#>>> art=Articulos(nombre="mesa",seccion="deco",precio=90) 
#>>> art.save()
#>>> art2=Articulos(nombre="camisa",seccion="ropa",precio=50)    
#>>> art2.save() 

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

