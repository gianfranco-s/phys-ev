from django.urls import path
from . import views

app_name = 'usuarios'


urlpatterns = [
    path('signup',views.signup_view,name="crear"),
    path('login',views.login_view,name="ingreso"),
    path('logout',views.logout_view,name="salir")
]