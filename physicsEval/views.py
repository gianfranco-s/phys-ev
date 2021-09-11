from django.http import HttpResponse
from django.shortcuts import render,redirect

def inicio(request):  # El usuario llegó directamente desde el www
    
    if request.user.is_authenticated:
        username = request.user.username
        #   print(username)
        #,{'username':username}
        return render(request,'inicio.html',{'username':username})
    
    return render(request,'inicio.html')
    

def about(request):  # El usuario vino desde urls, con /about
    return render(request, 'about.html')