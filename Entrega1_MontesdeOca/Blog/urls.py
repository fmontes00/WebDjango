from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("crearAutor", views.crearAutor, name="crearAutor"),
    path("crearArticulo", views.crearArticulo, name="crearArticulo"),
    path("articulos", views.articulos, name="articulos"),
    path("user_articulos", views.user_articulos, name="user_articulos"),
    path("view_article", views.view_article, name="view_article"),
    path("delete_articulo", views.delete_article, name="delete_articulo"),

    path("",views.landing_page,name="landing_page"),

    #Authentication
    path('signup/', views.signupuser, name= 'signupuser'),
    path('logout/', views.logoutuser, name= 'logoutuser'),
    path('login/', views.loginuser, name= 'loginuser'),
]
