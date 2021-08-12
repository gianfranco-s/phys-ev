# Sirve para convertir los modelos a formato JSON
# https://www.youtube.com/watch?v=263xt_4mBNc


from rest_framework import serializers
from .models import Ejercicio

class serializarEjercicio(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = ('id','titulo','tema','slug','enunciado')