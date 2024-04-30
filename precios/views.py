from django.shortcuts import render

# Create your views here.
def precios(request):
    return render(request, 'precios/precios.html')