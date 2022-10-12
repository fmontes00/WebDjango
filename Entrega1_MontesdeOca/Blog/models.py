from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    profesion = models.CharField(max_length = 40)


class Articulo(models.Model):
    titulo = models.CharField(max_length = 60)
    texto = models.CharField(max_lenght = 500)
    fecha = models.DateField(null = False)

class Seccion(models.model):
    nombre = models.CharField(max_length = 40)