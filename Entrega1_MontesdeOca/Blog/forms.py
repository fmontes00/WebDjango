from django.forms import ModelForm
from .models import Autor, Articulo


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "apellido", "profesion"]


class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ["titulo", "texto", "user", "fecha"]

