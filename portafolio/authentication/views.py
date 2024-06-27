from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SigninForm, SignupForm
from .models import Perfil

# Create your views here.
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Inicio de sesión exitoso')
                    return redirect('home')  # Cambia 'home' por el nombre de tu vista de inicio
                else:
                    messages.error(request, 'Esta cuenta está inactiva.')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = SigninForm()

    return render(request, 'authentication/signin.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear el perfil asociado al usuario
            fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
            Perfil.objects.create(
                usuario=user,
                fecha_nacimiento=fecha_nacimiento
            )
            login(request, user)
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('home')  # Cambia 'home' por el nombre de tu vista de inicio
    else:
        form = SignupForm()

    return render(request, 'authentication/signup.html', {'form': form})

@login_required
def signout(request):
    logout(request)
    return redirect('home')  # Redirige a la página principal o cualquier otra vista después de cerrar sesión