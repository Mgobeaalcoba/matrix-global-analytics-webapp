from django.shortcuts import render
from .models import FAQ

# Create your views here.
def faq_view(request):
    faq_items = FAQ.objects.all()
    context = {
        'faq_items': faq_items
    }
    return render(request, 'faq/preguntas_frecuentes.html', context)
