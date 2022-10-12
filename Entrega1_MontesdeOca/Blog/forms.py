from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Autor, Articulo, Lector, Seccion

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellido','profesion']

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo','texto','autor','fecha']

class SeccionForm(ModelForm):
    class Meta:
        model = Seccion
        fields = ['nombre']

class LectorForm(ModelForm):
    class Meta:
        model = Lector
        fields = ['nombre','apellido','articulo','reseña']

