from django import forms
from django.forms import ValidationError
from .models import Usuario
from .models import Cargo


class UsuariosForm(forms.Form):

	CARGO_CHOICES = (
	(1,"Gerente"),
	(2,"Encargado"),
	(3,"Empleado de salon"),
	)

	nombre = forms.CharField(label="Nombre")
	apellido = forms.CharField(label="Apellido")
	email = forms.EmailField(label="Email")
	cargo = forms.ChoiceField(label="Cargo", choices=CARGO_CHOICES)
	#fecha_inicial = forms.DateField(label="Fecha de Alta (a partir de)", widget=forms.SelectDateWidget(years=['2020','2021','2022']))
	#fecha_final =  forms.DateField(label="Fecha de Alta",widget=forms.SelectDateWidget(years=['2020','2021','2022']))

class BajaUsuarioForm(forms.Form):
	email = forms.EmailField(label="Email",required=True)
	password = forms.CharField(label="Password",required=True,widget=forms.PasswordInput())


class AltaUsuarioForm(forms.Form):
	CARGO_CHOICES = (
		(1,"Gerente"),
		(2,"Encargado"),
		(3,"Empleado de salon"),
	)

	nombre = forms.CharField(label="Nombre", required=True)
	apellido = forms.CharField(label="Apellido", required=True)
	email = forms.EmailField(required=True)
	password = forms.CharField(label="Password",required=True,widget=forms.PasswordInput()) # por que no me deja ponerle label y required entre los parentesis??
	cargo = forms.ChoiceField(label="Cargo",required=True, choices=CARGO_CHOICES)
	#fechaalta = forms.DateField(label="Fecha de Alta", widget=forms.SelectDateWidget(years=['2020','2021','2022']))

	def __str__(self):
		return f"{self.nombre}{self.apellido}{self.email}{self.password}{self.cargo}"

	
	def save(self,*args,**kwargs):
		super().save(*args, **kwargs)	


	#EJEMPLO DE FORMULARIO
	# class ContactoForm(forms,Form):
	# 	TORNEO_CHOICES = (
	# 	(1,"opcion 1"),
	# 	(2,"opcion 2"),
	# 	(3,"opcion 3"),
	# 	)
	# 	nombre = forms.CharField(label="Nombre de contacto", required=True)
	# 	apellido = forms.CharField(label="Apellido de contacto",required=True)
	# 	email = forms.EmailField(required=True)
	# 	sitio_favorito = forms.URLField(label="sitio favorito")
	# 	nacimiento =  forms.DateField(widget=forms.SelectDateWidget(years['2020','2021','2022']))
	# 	torneo_favorito = forms.ChoiceField(label="Torneo Favorito", choices=TORNEO_CHOICES)



########### ejeMplo ####################

class FormularioFiltrado(forms.Form):
	nombre = forms.CharField(label="Nombre",required=False)
	seccion = forms.CharField(label="Seccion",required=False)
	precio = forms.IntegerField(label="Precio",required=False)
