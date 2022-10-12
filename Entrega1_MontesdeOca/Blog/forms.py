
from django.forms import ModelForm
from .models import Autor, Articulo, Lector, Reseña

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellido','profesion']

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo','texto','autor','fecha']



class LectorForm(ModelForm):
    class Meta:
        model = Lector
        fields = ['nombre','apellido','profesion']

class ReseñaForm(ModelForm):
    class Meta:
        model = Reseña
        fields = ['lector','articulo','reseña']

