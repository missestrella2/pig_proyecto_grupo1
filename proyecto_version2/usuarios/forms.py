from django import forms


class UsuariosForm(forms.Form):

	CARGO_CHOICES = (
	(1,"Gerente"),
	(2,"Encargado"),
	(3,"Empleado de salon"),
	)

	nombre = forms.CharField(label="nombre", required=True)
	apellido = forms.CharField(label="apellido", required=True)
	email = forms.EmailField(required=True)
	#password = forms.PasswordInput(required=True)
	cargo = forms.ChoiceField(label="cargo", choices=CARGO_CHOICES)

	fecha_inicial =  forms.DateField(widget=forms.SelectDateWidget(years=['2020','2021','2022']))
	fecha_final =  forms.DateField(widget=forms.SelectDateWidget(years=['2020','2021','2022']))

class BajaUsuarioForm(forms.Form):
	CARGO_CHOICES = (
				(1,"Gerente"),
				(2,"Encargado"),
				(3,"Empleado de salon"),
	)

	nombre = forms.CharField(label="nombre", required=True)
	apellido = forms.CharField(label="apellido", required=True)
	email = forms.EmailField(required=True)
	#password = forms.PasswordInput(required=True)
	cargo = forms.ChoiceField(label="cargo", choices=CARGO_CHOICES)

class AltaUsuarioForm(forms.Form):
	CARGO_CHOICES = (
		(1,"Gerente"),
		(2,"Encargado"),
		(3,"Empleado de salon"),
	)

	nombre = forms.CharField(label="nombre", required=True)
	apellido = forms.CharField(label="apellido", required=True)
	email = forms.EmailField(required=True)
	#password = forms.PasswordInput(required=True)
	cargo = forms.ChoiceField(label="cargo", choices=CARGO_CHOICES)


	


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
