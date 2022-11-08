
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticuloForm, AutorForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Articulo, Autor


# Create your views here.

def landing_page(request):
    return render(request,"Blog/landing_page.html")

@login_required
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
                return redirect('/home')
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
            return redirect('/home')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')


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
            return redirect('/home')
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
def user_articulos(request):
    user_articles = Articulo.objects.filter(user = request.user)
    return render (request, 'Blog/user_articulos.html',{'user_articles': user_articles})

# @login_required
# def edit_article(request, article_pk):
#     article = get_object_or_404(Articulo, pk = article_pk, user = request.user)
#     if request.method == 'POST':
#         article.save()
#         return redirect('/home')

@login_required
def delete_article(request, article_pk):
    article = get_object_or_404(Articulo, pk = article_pk, user = request.user)
    if request.method == 'POST':
        article.delete()
        return redirect('/home')


@login_required
def view_article(request, article_pk):
    article = get_object_or_404(Articulo, pk = article_pk, user = request.user)
    if request.method == 'GET':
        form = ArticuloForm(instance= article)
        return render(request, 'Blog/view_article.html', {'article': article, 'form': form})
    else:
        try:
            form = ArticuloForm(request.POST, instance= article)
            form.save()
            return redirect('/home')
        except ValueError:
            return redirect(request, 'Blog/view_article.html', {'article': article, 'error': 'wrong data'})




