from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenido al inventario")


from django.shortcuts import render, redirect
from .forms import ProductoForm

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige después de guardar
    else:
        form = ProductoForm()

    return render(request, 'productos/agregar_producto.html', {'form': form})

from django.shortcuts import render

def nuevo_dispositivo(request):
    return render(request, 'productos/nuevo_dispositivo.html')
