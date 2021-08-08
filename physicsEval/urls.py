"""physicsEval URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views                     # from . -> importar de este mismo directorio

urlpatterns = [
    path('admin/', admin.site.urls),    # Cuando "ve" /admin, nos lleva a admin.site.urls
    path('ejercicios/', include('ejercicios.urls')),  # Incluye los url presentes en la app ejercicios
    path('about/',views.about),         # Envía al usuario a la función about, que se encuentra en views.py
    path('',views.inicio),              # Envía al usuario a la función inicio, que se encuentra en views.py
    path('accounts/',include('usuarios.urls')),  # Envía al navegador a buscar todas las posibilidades de urls que haya en usuarios.urls
]
