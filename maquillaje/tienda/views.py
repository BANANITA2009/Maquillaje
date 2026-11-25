from django.shortcuts import render


def inicio(request):
    return render(request, 'tienda/inicio.html')


def productos(request):
    return render(request, 'tienda/productos.html')


def contacto(request):
    return render(request, 'tienda/contacto.html')