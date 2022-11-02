from accounts.forms import RegistroUsuarioForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from sse_app.models import Alumno

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            alumno = Alumno(matricula=form.cleaned_data.get('username'))
            if Alumno.objects.filter(matricula=form.cleaned_data.get('username')):
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Usuario registrado con éxito. Ahora puedes iniciar sesión.')
                return redirect ('accounts:login')
            else:
                form.save()
                alumno.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Usuario registrado con éxito. Ahora puedes iniciar sesión.')
                return redirect ('accounts:login')

    else:
        form = RegistroUsuarioForm()

    return render (request, 'accounts/registro.html', {'form':form})

def aviso_privacidad(request):
    return render(request, 'accounts/aviso_privacidad.html')