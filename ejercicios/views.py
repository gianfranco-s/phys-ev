from django.shortcuts import render
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