from django.shortcuts import render

def quienes_somos(request):
    return render(request, 'trabajos/quienes_somos.html')

def nuestro_porfolio(request):
    return render(request, 'trabajos/nuestro_porfolio.html')

def ultimos_proyectos(request):
    return render(request, 'trabajos/ultimos_proyectos.html')

def marcas(request):
    return render(request, 'trabajos/marcas.html')
