"""
URL configuration for MatrixGlobalAnalytics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as home_views
from contacto import views as contacto_views
from legal import views as legal_views
from trabajos import views as trabajos_views
from faq import views as faq_views
from precios import views as precios_views
from cursos import views as cursos_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_views.home, name='home'),
    path('contacto/', contacto_views.formulario_contacto, name="formulario_contacto"),
    path('terminos-de-uso/', legal_views.terminos_de_uso, name='terminos_de_uso'),
    path('politica-de-privacidad/', legal_views.politica_de_privacidad, name='politica_de_privacidad'),
    path('quienes-somos/', trabajos_views.quienes_somos, name='quienes_somos'),
    path('nuestro-porfolio/', trabajos_views.nuestro_porfolio, name='nuestro_porfolio'),
    path('ultimos-proyectos/', trabajos_views.ultimos_proyectos, name='ultimos_proyectos'),
    path('marcas/', trabajos_views.marcas, name='marcas'),
    path('preguntas-frecuentes/', faq_views.faq_view, name='preguntas_frecuentes'),
    path('precios/', precios_views.precios, name='precios'),
    path('cursos/', cursos_views.cursos, name='cursos'),
]
