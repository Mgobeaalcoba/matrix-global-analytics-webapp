from django.shortcuts import render
from .models import PorfolioItem

def quienes_somos(request):
    return render(request, 'trabajos/quienes_somos.html')

def nuestro_porfolio(request):
    porfolio_items = PorfolioItem.objects.all()
    context = {
        'porfolio_items': porfolio_items
    }
    return render(request, 'trabajos/nuestro_porfolio.html', context)

def ultimos_proyectos(request):
    return render(request, 'trabajos/ultimos_proyectos.html')

def marcas(request):
    return render(request, 'trabajos/marcas.html')
