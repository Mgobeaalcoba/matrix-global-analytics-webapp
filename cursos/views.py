from django.shortcuts import render
from .models import Curso

# Create your views here.
def cursos(request):
    cursos = Curso.objects.all()
    for curso in cursos:
        descripcion_list = curso.descripcion.split("|")
        curso.descripcion = descripcion_list
    context = {
        'cursos': cursos
    }
    return render(request, 'cursos/cursos.html', context)