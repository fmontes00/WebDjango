
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticuloForm, AutorForm, LectorForm, ReseñaForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Articulo, Autor, Lector, Reseña


# Create your views here.
def home(request):
    return render(request, "Blog/home.html")


def signupuser(request):
    if request.method == 'GET':
        return render(request, "Blog/signupuser.html",{'form':UserCreationForm()})
    else:
        if request.POST['password1']== request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect("/")
            except IntegrityError:
                return render(request, 'Blog/signupuser.html', {'form':UserCreationForm(), 'error': "username alredy taken, select a new one"})
        else: #mismatch password
            return render(request, 'Blog/signupuser.html', {'form':UserCreationForm(), 'error': "passwords did not match"})


def loginuser(request):
    if request.method == 'GET': 
        return render(request, 'Blog/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username =request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'Blog/loginuser.html', {'form':AuthenticationForm(), 'error': "username and password did not match"})
        else:
            login(request, user)
            return redirect('/')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def crearAutor(request):
    if request.method == "GET":
        return render(request, "Blog/crearAutor.html", {"form": AutorForm()})
    else:
        try:
            form = AutorForm(request.POST)
            new_autor = form.save(commit=False)
            new_autor.save()
            return redirect("/")
        except ValueError:
            return render(
                request,
                "Blog/crearAutor.html",
                {"form": AutorForm(), "error": "datos incorrectos, intente de nuevo"},
            )

@login_required
def crearArticulo(request):
    if request.method == "GET":
        return render(request, "Blog/crearArticulo.html", {"form": ArticuloForm()})
    else:
        try:
            form = ArticuloForm(request.POST)
            new_articulo = form.save(commit=False)
            new_articulo.save()
            return redirect("/")
        except ValueError:
            return render(
                request,
                "Blog/crearArticulo.html",
                {
                    "form": ArticuloForm(),
                    "error": "datos incorrectos, intente de nuevo",
                },
            )

@login_required
def articulos(request):
    articulos = Articulo.objects.all()
    return render(request, "Blog/articulos.html", {"articulos": articulos})

@login_required
def crearLector(request):
    if request.method == "GET":
        return render(request, "Blog/crearLector.html", {"form": LectorForm()})
    else:
        try:
            form = LectorForm(request.POST)
            new_lector = form.save(commit=False)
            new_lector.save()
            return redirect("/")
        except ValueError:
            return render(
                request,
                "Blog/crearLector.html",
                {"form": LectorForm(), "error": "datos incorrectos, intente de nuevo"},
            )

@login_required
def crearReseña(request):
    if request.method == "GET":
        return render(request, "Blog/crearLector.html", {"form": ReseñaForm()})
    else:
        try:
            form = ReseñaForm(request.POST)
            new_reseña = form.save(commit=False)
            new_reseña.save()
            return redirect("/")
        except ValueError:
            return render(
                request,
                "Blog/crearLector.html",
                {"form": ReseñaForm(), "error": "datos incorrectos, intente de nuevo"},
            )

@login_required
def reseñas(request):
    reseñas = Reseña.objects.all()
    return render(request, "Blog/reseñas.html", {"reseñas": reseñas})


###################### Modificar ########################

@login_required
def buscar(request):

    nombre_a_buscar = request.GET.get("nombre")
    autores = Autor.objects.filter(nombre=nombre_a_buscar)

    contexto = {"nombre": nombre_a_buscar, "autores_encontrados": autores}

    return render(request, "Blog/busqueda.html", contexto)
