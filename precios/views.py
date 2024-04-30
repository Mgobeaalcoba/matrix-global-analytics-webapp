from django.shortcuts import render
from .models import Paquete

# Create your views here.
def precios(request):
    paquetes = Paquete.objects.all()
    for paquete in paquetes:
        int_precio = int(paquete.precio)
        paquete.precio = int_precio
        caracter_list = paquete.caracteristicas.split("|")
        paquete.caracteristicas = caracter_list
    context = {
        'paquetes': paquetes
    }
    return render(request, 'precios/precios.html', context)