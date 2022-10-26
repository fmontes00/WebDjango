
from django.shortcuts import render, redirect
from .forms import ArticuloForm, AutorForm, LectorForm, ReseñaForm
from .models import Articulo, Autor, Lector, Reseña


# Create your views here.
def home(request):
    return render(request, "Blog/home.html")


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


def articulos(request):
    articulos = Articulo.objects.all()
    return render(request, "Blog/articulos.html", {"articulos": articulos})


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


def reseñas(request):
    reseñas = Reseña.objects.all()
    return render(request, "Blog/reseñas.html", {"reseñas": reseñas})


###################### Modificar ########################


def buscar(request):

    nombre_a_buscar = request.GET.get("nombre")
    autores = Autor.objects.filter(nombre=nombre_a_buscar)

    contexto = {"nombre": nombre_a_buscar, "autores_encontrados": autores}

    return render(request, "Blog/busqueda.html", contexto)
