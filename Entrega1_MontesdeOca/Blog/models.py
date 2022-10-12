from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    profesion = models.CharField(max_length = 40)

    def __str__(self):
        return self.apellido


class Articulo(models.Model):
    titulo = models.CharField(max_length = 60)
    texto = models.CharField(max_length = 500)
    fecha = models.DateField(null = False)

    def __str__(self):
        return self.titulo

class Seccion(models.Model):
    nombre = models.CharField(max_length = 40)

    def __str__(self):
        return self.nombre