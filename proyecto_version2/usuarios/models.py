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
