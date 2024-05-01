from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.CharField(max_length=200, default="../../../static/i/logo.jpg")  # Ruta de la imagen

    def __str__(self):
        return self.titulo
