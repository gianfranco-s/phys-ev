from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout

def signup_view(request):
    '''
    Método POST: crear un usuario con los datos del formulario.
        Si son válidos los datos, salvar al usuario
        Si no son válidos, devolver un formulario en blanco
    Método GET: cuando el usuario llega por primera vez a la página, mostrarle un formulario en blanco
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)           # Trae los datos del formulario, crea el objeto
        if form.is_valid():                             # Valida al objeto
            # form.save()                                 # Guarda los datos, si son válidos
            
            # loguear al usuario
            user = form.save()
            login(request,user)

            # return redirect('/ejercicios')
            return redirect('ejercicios:ejerAleat') 
    else:                                               # Si se trata de un método GET
        form = UserCreationForm()    
    
    contexto = {
        'form':form,
    }
    return render(request,'usuarios/signup.html',contexto)


from django.contrib.auth.forms import UserCreationForm
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)    # AuthenticationForm toma otros parámetros, por eso "fuerzo" a enviarle únicamente data
        if form.is_valid():
            # loguear al usuario
            user = form.get_user()
            login(request,user)

            # return redirect('/ejercicios')
            # return redirect('ejercicios:ejerAleat') 
            return redirect('paginaInicio')

    else:                                               # Si se trata de un método GET
        form = AuthenticationForm()  
    
    contexto = {
        'form':form,
    }
    return render(request,'usuarios/login.html',contexto)

def logout_view(request):
    # if request.method == 'POST':
    logout(request)
    # return redirect('ejercicios:ejerAleat')
    return redirect('paginaInicio')
