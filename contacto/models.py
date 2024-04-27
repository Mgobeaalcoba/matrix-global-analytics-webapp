from django.db import models

class Email(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    consulta = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
