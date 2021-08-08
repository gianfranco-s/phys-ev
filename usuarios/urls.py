from django.urls import path
from . import views

# Si el usuario llega a <página.com>/signup, 
urlpatterns = [
    path('signup',views.signup),
    path('login',views.login),
]