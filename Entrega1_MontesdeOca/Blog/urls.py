from django.urls import path
from . import views
from .views import busqueda

urlpatterns = [

    path('', views.home, name='home'),
    path('crearAutor', views.crearAutor, name='crearAutor'),
    path('crearArticulo', views.crearArticulo, name='crearArticulo'),
    path('articulos', views.articulos, name='articulos'),
    path('crearLector', views.crearLector, name='crearLector'),
    path('reseñas', views.reseñas, name='reseñas'),
    path('crearReseña', views.crearReseña, name='crearReseña'),
    path('busqueda', busqueda.as_view(), name='busqueda'),

]