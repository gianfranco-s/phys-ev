from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def signup(request):
    '''
    Método POST: crear un usuario con los datos del formulario.
        Si son válidos los datos, salvar al usuario
        Si no son válidos, devolver un formulario en blanco
    Método GET: cuando el usuario llega por primera vez a la página, mostrarle un formulario en blanco
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)           # Trae los datos del formulario, crea el objeto
        if form.is_valid():                             # Valida al objeto
            form.save()                                 # Guarda los datos, si son válidos
            # loguear al usuario
            return redirect('/ejercicios')
    else:                                               # Si se trata de un método GET
        form = UserCreationForm()    
    
    contexto = {
        'form':form,
    }
    return render(request,'usuarios/signup.html',contexto)

from django.contrib.auth.forms import UserCreationForm
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)    # AuthenticationForm toma otros parámetros, por eso "fuerzo" a enviarle únicamente data
        if form.is_valid():
            # loguear al usuario
            return redirect('/ejercicios')

    else:                                               # Si se trata de un método GET
        form = AuthenticationForm()  
    
    contexto = {
        'form':form,
    }
    return render(request,'usuarios/login.html',contexto)