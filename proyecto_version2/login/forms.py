from django import forms


class IndexForm(forms.Form):
    nombre = forms.CharField(label="Nombre:", required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)