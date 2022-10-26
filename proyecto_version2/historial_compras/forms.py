from django import forms


class HistCompForm(forms.Form):
    nombre = forms.CharField(label="Nombre:", required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)

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
