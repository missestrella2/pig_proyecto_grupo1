from django.db import models

class Usuario(models.Model):
    nombre= models.CharField(max_length=100, verbose_name='Nombre')
    apellido= models.CharField(max_length=100, verbose_name='Apellido',null=True)
    email= models.EmailField(max_length=150, verbose_name='Email')
    dni= models.IntegerField(verbose_name='DNI')
    password= models.CharField(max_length=50, verbose_name='Password')
    

