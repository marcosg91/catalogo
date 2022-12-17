from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):
    first_name = forms.CharField(label="nombre", widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="apellido", widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(label="correo electronico", widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="usuario", widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="contraseña", widget=forms.TextInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="repetir contraseña", widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model= Usuario 
        fields=["first_name", "last_name", "email", "username", "password1", "password2"] 