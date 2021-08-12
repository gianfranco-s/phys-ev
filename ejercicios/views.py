from django.http.response import JsonResponse
from django.shortcuts import render
from dotenv.main import rewrite
from .models import Ejercicio           # Importo el objeto "Ejercicio"
from .serializers import serializarEjercicio
from rest_framework import viewsets
import random

def ejercicios(request):
    cantEjer = len(Ejercicio.objects.all())
    indiceAleat = random.randint(0,cantEjer-1)
    unEjer = Ejercicio.objects.all()[indiceAleat]
    
    contexto = {
        'ejercicio':unEjer
    }
    
    return render(request,'ejercicios/ejercicios.html',contexto)


def verListado(request):
    '''
    Muestra un html que tiene un script que hace AJAX
    '''
    
    return render(request,'ejercicios/ver-listado.html')

class mostrarListado(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all().order_by('tema')
    serializer_class = serializarEjercicio