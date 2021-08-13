from django.urls import path
from . import views                     # from . -> importar de este mismo directorio
from .views import listado_view

app_name = 'ejercicios'


# Si el usuario llega a <página.com>/ejercicios, views nos enviará a ejercicio
# Este comportamiento debe configurarse incluyendo el presente urls.py en physicsEval/physicsEval/urls.py
urlpatterns = [
    path('',views.ejercicios,name="ejerAleat"),
    path('ver-listado',views.verListado),
    path('mostrarListado',listado_view.as_view()),
    path('mostrarListado/<int:pk>',listado_view.as_view()),  # Para capturar IDs
]