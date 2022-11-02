from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Alumno)
admin.site.register(SeleccionCarrera)
admin.site.register(Licenciatura)
admin.site.register(ContinuacionEstudios)
admin.site.register(BusquedaEmpleo)
admin.site.register(EmpleoDuranteEstudios)
admin.site.register(EmpleoInmediato)
admin.site.register(Empresa)

