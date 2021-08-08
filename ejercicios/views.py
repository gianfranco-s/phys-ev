from django.shortcuts import render
from .models import Ejercicio           # Importo el objeto "Ejercicio"

def ejercicios(request):
    los_ejercicios = Ejercicio.objects.all().order_by('tema')     # Trae todos los objetos de la tabla, ordenados por tema
    a = 14;
    b = "Un string"
    contexto = {
        'los_ejercicios':los_ejercicios,
    }             
    return render(request,'ejercicios/ejercicios.html',contexto)

