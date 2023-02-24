from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label= 'Usuario:', max_length=254)
    password = forms.CharField(label=("Contraseña:"), widget=forms.PasswordInput)