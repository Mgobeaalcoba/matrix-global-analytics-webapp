from django.shortcuts import render
from .models import PorfolioItem, Employee, Experience

def quienes_somos(request):
    empleados = Employee.objects.all()
    for empleado in empleados:
        description_split = empleado.description.split('|')
        empleado.description = description_split
    context = {
        'empleados': empleados
    }
    return render(request, 'trabajos/quienes_somos.html', context)

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
