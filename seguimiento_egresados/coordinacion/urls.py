from django.urls import path

from . import views

urlpatterns = [
    path('coordinacion/', views.index) # seguimiento-egresadosfeiuv.com/coordinacion
]