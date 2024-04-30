from django.db import models

class Paquete(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    caracteristicas = models.TextField()

    def __str__(self):
        return self.titulo
