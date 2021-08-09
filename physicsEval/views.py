from django.http import HttpResponse
from django.shortcuts import render,redirect

def inicio(request):  # El usuario llegó directamente desde el www
    # Redireccionar al signup, que estará dentro de physicsEval/usuarios
    # return redirect('accounts/signup')

    return render(request,'inicio.html')
    

def about(request):  # El usuario vino desde urls, con /about
    return render(request, 'about.html')