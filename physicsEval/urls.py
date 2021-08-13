from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views                     # from . -> importar de este mismo directorio

urlpatterns = [
    path('admin/', admin.site.urls),    # Cuando "ve" /admin, nos lleva a admin.site.urls
    path('ejercicios/', include('ejercicios.urls')),  # Incluye los url presentes en la app ejercicios
    path('about/',views.about),         # Envía al usuario a la función about, que se encuentra en views.py
    path('',views.inicio,name='paginaInicio'),              # Envía al usuario a la función inicio, que se encuentra en views.py
    path('accounts/',include('usuarios.urls')),  # Envía al navegador a buscar todas las posibilidades de urls que haya en usuarios.urls
]


# Para traer archivos static (CSS, imágenes, etc)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()