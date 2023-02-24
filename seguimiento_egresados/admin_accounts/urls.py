from re import template
from django.urls import path
from . import views
from .views import CustomLoginView, aviso_privacidad
from seguimiento_egresados import settings

app_name='admin_accounts'
urlpatterns = [
    path(settings.PATH_PREFIX, CustomLoginView.as_view(template_name="admin_accounts/login_admin.html"), name="login_admin"),
    path('%saviso_privacidad/' % settings.PATH_PREFIX, views.aviso_privacidad, name="aviso_privacidad")
]