
from django.shortcuts import render, redirect
from .forms import ArticuloForm, AutorForm


# Create your views here.
def home(request):
   return render(request, 'Blog/home.html')


def crearAutor(request):
    if request.method == 'GET':
        return render(request, 'Blog/crearAutor.html',{'form': AutorForm()})
    else:
        try:
            form = AutorForm(request.POST)
            new_autor = form.save(commit=False)
            new_autor.save()
            return redirect('/Blog')
        except ValueError:
            return render(request, 'Blog/crearAutor.html',{'form': AutorForm(),'error':'datos incorrectos, intente de nuevo'})


def crearArticulo(request):
    if request.method == 'GET':
        return render(request, 'Blog/crearArticulo.html',{'form': ArticuloForm()})
    else:
        try:
            form = ArticuloForm(request.POST)
            new_articulo = form.save(commit=False)
            new_articulo.save()
            return redirect('/Blog')
        except ValueError:
            return render(request, 'Blog/crearArticulo.html',{'form': ArticuloForm(),'error':'datos incorrectos, intente de nuevo'})


