from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class RegistroUsuarioForm(UserCreationForm):
    
    username = forms.CharField()
    username.label = 'Usuario:'
    username.help_text = 'El nombre de usuario deber ser tu matrícula en formato: s12345678'

    password1= forms.CharField(widget=forms.PasswordInput())
    password1.label= 'Contraseña:'

    password2 = forms.CharField(widget=forms.PasswordInput())
    password2.label = 'Confirmar contraseña:'
    
    email = forms.EmailField()
    email.label = 'Correo electrónico:'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label= 'Usuario:', max_length=254)
    password = forms.CharField(label=("Contraseña:"), widget=forms.PasswordInput)