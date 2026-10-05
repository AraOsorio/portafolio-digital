from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path(
        'proyectos/arriendo/',
        views.proyecto_arriendo,
        name='proyecto_arriendo'
    ),
]