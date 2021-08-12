from django.shortcuts import render, redirect, get_object_or_404
from .models import Pelicula, Genero
from .forms import ContactoForm, PeliculaForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import PeliculaSerializer, GeneroSerializer

class GeneroViewset(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class PeliculaViewset(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

    def get_queryset(self):
        pelicula = Pelicula.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            pelicula = pelicula.filter(nombre__contains=nombre)

        return pelicula


def home(request):
    peliculas = Pelicula.objects.all()
    data = {
        'peliculas': peliculas
    }
    
    return render(request, 'app/home.html', data)

def peliculas(request):
    return render(request, 'app/peliculas.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

@permission_required('appmovies.add_pelicula')
def agregar_pelicula(request):

    data = {
        'form': PeliculaForm()
    }

    if request.method == 'POST':
        formulario = PeliculaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Pelicula Registrada")
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

@permission_required('appmovies.view_pelicula')
def listar_pelicula(request):

    peliculas = Pelicula.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(peliculas, 7)
        pelicula = paginator.page(page)

    except:
        raise Http404

    data = {
        'entity': pelicula,
        'paginator': paginator
    }

    return render(request, 'app/producto/listar.html', data)

@permission_required('appmovies.change_pelicula')
def modificar_pelicula(request, id):

    pelicula = get_object_or_404(Pelicula, id=id)

    data = {
        'form': PeliculaForm(instance=pelicula)
    }

    if request.method == 'POST':
        formulario = PeliculaForm(data=request.POST, instance=pelicula, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_pelicula")

        else:
            data["form"] = formulario

    return render(request, 'app/producto/modificar.html', data)

@permission_required('appmovies.delete_pelicula')
def eliminar_pelicula(request, id):

    pelicula = get_object_or_404(Pelicula, id=id)
    pelicula.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_pelicula")

def registro(request):
    data = {
        'form': CustomUserCreationForm()

    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "El registro fue exitoso")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

@login_required
def admin(request):
    return render(request, 'http://127.0.0.1:8000/admin')