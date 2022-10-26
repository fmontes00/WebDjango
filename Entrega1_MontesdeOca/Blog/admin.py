from django.contrib import admin
from Blog.models import Articulo, Autor, Lector

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Autor)
admin.site.register(Lector)
