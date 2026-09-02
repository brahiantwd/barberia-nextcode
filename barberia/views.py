from django.shortcuts import render


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

        print(nombre)
        print(correo)
        print(telefono)

    return render(request, 'barberia/clientes.html')