from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    profesion = models.CharField(max_length = 40)

    def __str__(self):
        return self.apellido


class Articulo(models.Model):
    titulo = models.CharField(max_length = 60)
    texto = models.TextField()
    fecha = models.DateField(null = False)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Seccion(models.Model):
    nombre = models.CharField(max_length = 40)

    def __str__(self):
        return self.nombre

class Lector(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    articulo = models.ForeignKey(Articulo,on_delete=models.CASCADE)
    reseña = models.TextField()

    def __str__(self):
        return self.nombre