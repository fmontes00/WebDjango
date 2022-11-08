from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return self.apellido


class Articulo(models.Model):
    titulo = models.CharField(max_length=60)
    texto = models.TextField()
    fecha = models.DateField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

