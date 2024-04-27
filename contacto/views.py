from django.shortcuts import render

def formulario_contacto(request):
    return render(request, 'contacto/formulario_contacto.html')
