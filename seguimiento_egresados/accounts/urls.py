from re import template
from django.urls import path
from . import views
from .views import CustomLoginView, aviso_privacidad
from seguimiento_egresados import settings

urlpatterns =[
    path(settings.PATH_PREFIX, CustomLoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('%sregistro/' % settings.PATH_PREFIX, views.registro, name="registro"),
    path('%saviso_privacidad/' % settings.PATH_PREFIX, views.aviso_privacidad, name="aviso_privacidad"),
    path('%slogin_coordinador/' % settings.PATH_PREFIX, views.login_coordinador, name="login_coordinador")
]