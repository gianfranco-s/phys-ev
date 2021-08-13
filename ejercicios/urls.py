from django.urls import path, include
from . import views                     # from . -> importar de este mismo directorio
from rest_framework import routers

app_name = 'ejercicios'

router = routers.DefaultRouter()
router.register('ejercicios',views.mostrarListado)

# Si el usuario llega a <página.com>/ejercicios, views nos enviará a ejercicio
# Este comportamiento debe configurarse incluyendo el presente urls.py en physicsEval/physicsEval/urls.py
urlpatterns = [
    path('',views.ejercicios,name="ejerAleat"),
    path('ver-listado',views.verListado),         # Dirección para mostrar una lista de todos los ejercicios
    path('mostrarListado',include(router.urls)),  # Dirección para mostrar una lista de todos los ejercicios
    path('redactar',views.redactarEjer,name="redactar"),

]