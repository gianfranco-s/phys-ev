from django.http.response import JsonResponse
from django.shortcuts import render
from dotenv.main import rewrite
from .models import Ejercicio           # Importo el objeto "Ejercicio"
import random

def ejercicios(request):
    cantEjer = len(Ejercicio.objects.all())
    indiceAleat = random.randint(0,cantEjer-1)
    unEjer = Ejercicio.objects.all()[indiceAleat]
    
    contexto = {
        'ejercicio':unEjer
    }
    
    return render(request,'ejercicios/ejercicios.html',contexto)


def listado(request):
    la_lista = list(Ejercicio.objects.values().order_by('tema'))
    
    print(type(print(JsonResponse(la_lista,safe=False))))
    print(JsonResponse(la_lista,safe=False))
    print('--------------------')
    # return JsonResponse(la_lista,safe=False)

    contexto = {
        'la_lista' : la_lista
    }
    return render(request,'ejercicios/listado.html',contexto)


def verListado(request):
    la_lista = list(Ejercicio.objects.values().order_by('tema'))
    
    print(type(print(JsonResponse(la_lista,safe=False))))
    print(JsonResponse(la_lista,safe=False))
    print('--------------------')
    # return JsonResponse(la_lista,safe=False)

    contexto = {
        'la_lista' : la_lista
    }
    return render(request,'ejercicios/ver-listado.html',contexto)