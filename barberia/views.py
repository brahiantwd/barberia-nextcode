from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def inicio(request):
    return render(request, 'barberia/inicio.html')

def servicios(request):
    return render(request, 'barberia/servicios.html')

def base(request):
    return render(request, 'barberia/base.html')

def clientes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')

        print(f"Registro: {nombre} - {correo} - {telefono}")
        

    return render(request, 'barberia/clientes.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST.get('username')
        contraseña = request.POST.get('password')
        
        print(f"Intento de login: {correo}")
        

    return render(request, 'barberia/login.html')
