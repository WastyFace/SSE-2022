from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from sse_app.models import Coordinador

# Create your views here.

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

class CustomLoginAdminView(LoginView):
    authentication_form = CustomAuthenticationForm

def admin_login(request):
    return render(request, 'admin_accounts/admin_login.html')

def aviso_privacidad(request):
    return render(request, 'admin_accounts/aviso_privacidad.html')