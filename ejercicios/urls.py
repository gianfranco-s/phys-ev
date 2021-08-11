from django.urls import path
from . import views                     # from . -> importar de este mismo directorio


# Si el usuario llega a <página.com>/ejercicios, views nos enviará a ejercicio
# Este comportamiento debe configurarse incluyendo el presente urls.py en physicsEval/physicsEval/urls.py
urlpatterns = [
    path('',views.ejercicios),
    path('ver-listado',views.verListado),  # Dirección para mostrar una lista de todos los ejercicios
    path('listado',views.listado),  # Dirección para mostrar una lista de todos los ejercicios
]