# Sirve para convertir los modelos a formato JSON

from rest_framework import serializers
from .models import Ejercicio

class serializarEjercicio(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        # fields = ['id','titulo','tema','slug','enunciado']
        fields = "__all__"