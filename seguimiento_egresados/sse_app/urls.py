from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from seguimiento_egresados import settings

urlpatterns =[
    path("%salumno" % settings.PATH_PREFIX, views.alumno, name="alumno"),
    path("%sseleccion_carrera"% settings.PATH_PREFIX, views.seleccion_carrera, name="seleccion_carrera"),
    path("%slicenciatura"% settings.PATH_PREFIX, views.licenciatura, name="licenciatura"),
    path("%scontinuacion_estudios"% settings.PATH_PREFIX, views.continuacion_estudios, name="continuacion_estudios"),
    path("%sempleo_durante_estudios"% settings.PATH_PREFIX, views.empleo_durante_estudios, name="empleo_durante_estudios"),
    path("%sbusqueda_empleo"% settings.PATH_PREFIX, views.busqueda_empleo, name="busqueda_empleo"),
    path("%sempleo_inmediato"% settings.PATH_PREFIX, views.empleo_inmediato, name="empleo_inmediato"),
    path("%sempleo_actual"% settings.PATH_PREFIX, views.empleo_actual, name="empleo_actual"),
    path("%srecomendaciones"% settings.PATH_PREFIX, views.recomendaciones, name="recomendaciones"),
    path("%slogout/"% settings.PATH_PREFIX, auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name="logout")

]