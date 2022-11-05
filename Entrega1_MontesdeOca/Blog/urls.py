from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("crearAutor", views.crearAutor, name="crearAutor"),
    path("crearArticulo", views.crearArticulo, name="crearArticulo"),
    path("articulos", views.articulos, name="articulos"),
    path("crearLector", views.crearLector, name="crearLector"),
    path("reseñas", views.reseñas, name="reseñas"),
    path("crearReseña", views.crearReseña, name="crearReseña"),
    path("buscar", views.buscar, name="buscar"),

    #Authentication
    path('signup/', views.signupuser, name= 'signupuser'),
    path('logout/', views.logoutuser, name= 'logoutuser'),
    path('login/', views.loginuser, name= 'loginuser'),
]
