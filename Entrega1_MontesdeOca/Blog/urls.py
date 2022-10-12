from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('crearAutor', views.crearAutor, name='crearAutor'),
    path('crearArticulo', views.crearArticulo, name='crearArticulo'),

]