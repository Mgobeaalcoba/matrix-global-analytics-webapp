from django.shortcuts import render

def terminos_de_uso(request):
    return render(request, 'legal/terminos_de_uso.html')

def politica_de_privacidad(request):
    return render(request, 'legal/politica_de_privacidad.html')
