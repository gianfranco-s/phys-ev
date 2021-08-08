from django.db import models

# Un modelo se representa por medio de una clase
class Ejercicio(models.Model):
    # Usar models hará que sea un poco más fácil la generación 
    titulo = models.CharField(max_length=50)   # 50 caracteres máximo
    tema = models.CharField(max_length=50)     # 50 caracteres máximo
    slug = models.SlugField()                  # Es una URL para el ejercicio
    enunciado = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    # Agregar autor

    def __str__(self):
        return self.titulo      # Representación en string
        