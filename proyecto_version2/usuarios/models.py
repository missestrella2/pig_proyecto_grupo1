from django.db import models

class Usuario(models.Model):
    nombre= models.CharField(max_length=100, verbose_name='Nombre')
    apellido= models.CharField(max_length=100, verbose_name='Apellido')
    email= models.EmailField(max_length=150, verbose_name='Email')
    password= models.CharField(max_length=50, verbose_name='Password')
    fechadealta=models.DateField(verbose_name='Fecha de Alta')

class Cargo(models.Model):
    cargo= models.CharField(max_length=100, verbose_name='Cargo')
