from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Ejercicio
from .serializers import serializarEjercicio
from django.contrib.auth.decorators import login_required
import random



def ejercicios(request):
    # Elección aleatoria de un ejercicio
    cantEjer = len(Ejercicio.objects.all())
    indiceAleat = random.randint(0,cantEjer-1)
    unEjer = Ejercicio.objects.all()[indiceAleat]
    
    contexto = {
        'ejercicio':unEjer,
    }

    # Para cuando se implemente la funcionalidad de cálculo y reemplazo de variables
    consigna = unEjer.redactar()
    print(consigna)
    contexto = {
        'ejercicio':unEjer,
        'consigna':consigna
    }

    return render(request,'ejercicios/ejercicios.html',contexto)


class listado_view(APIView):
    
    
    def get_object(self, pk):
        try:
            return Ejercicio.objects.get(pk=pk)
        except Ejercicio.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Ejercicio.objects.all()
            
        serializer = serializarEjercicio(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = serializarEjercicio(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Ejercicio creado',
            # 'data': serializer.data
        }

        return response
    
    # @action(methods=['put'], detail=True)
    def put(self, request, pk=None, format=None):
        actualizar_ejercicio = Ejercicio.objects.get(pk=pk)
        serializer = serializarEjercicio(instance=actualizar_ejercicio,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Ejecicio actualizado',
            # 'data': serializer.data
        }

        return response

    # @action(methods=['delete'], detail=True)
    def delete(self, request, pk, format=None):
        borrar_ejercicio =  Ejercicio.objects.get(pk=pk)

        borrar_ejercicio.delete()

        return Response({
            'message': 'Ejercicio borrado'
        })


def verListado(request):
    '''
    Muestra un html que tiene un script que hace AJAX
    '''
    
    return render(request,'ejercicios/ver-listado.html')
