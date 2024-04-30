from django.shortcuts import render
from .models import PorfolioItem, Employee, Experience, NewProject

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
    new_projects = NewProject.objects.all()
    context = {
        'new_projects': new_projects
    }
    return render(request, 'trabajos/ultimos_proyectos.html', context)

def marcas(request):
    return render(request, 'trabajos/marcas.html')
