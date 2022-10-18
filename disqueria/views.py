from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DateDetailView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from .models import  Formato, Album, Discografica, Genero, Interprete, Tema


def home(request):
    return render(request,'index.html')


class About(TemplateView):
    template_name = "about.html"


class Contacto(TemplateView):
    template_name = "contacto.html"


class ProyectoIntegrador(TemplateView):
    template_name = "crud/proyecto.html"


def buscar_album(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_album_list = Album.objects.filter(Q(nombre__icontains=q)).order_by('nombre',
        Q(genero__icontains=q)).order_by('genero'), (Q(interprete__icontains=q)).order_by('interprete')
    else:
        all_album_list = Album.objects.all().order_by('nombre')
        all_album_list = Album.objects.all().order_by('genero')
        all_album_list = Album.objects.all().order_by('interprete')

    return render(request, 'buscar_album.html', {"album":all_album_list})


class CrearAlbum(CreateView):        
    model = Album
    template_name = "crud/crear_album.html"
    success_url = 'proyecto'
    fields = ['nombre','interprete','genero','cant_temas', 'discografica', 'formato', 'fec_lanzamiento', 'precio', 'cantidad']


class ListarAlbum(ListView):
    model = Album
    template_name = "crud/listar_album.html"


class EditarAlbum(UpdateView):
    model = Album
    template_name ='crud/editar_album.html'
    success_url = reverse_lazy('listar_albums')
    fields = ['nombre','interprete','genero','cant_temas', 'discografica', 'formato', 'fec_lanzamiento', 'precio', 'cantidad'] 


class EliminarAlbum(DeleteView):
    model = Album
    template_name = "crud/eliminar_album.html"
    success_url = reverse_lazy('listar_album')


class MostrarAlbum(DetailView):
    model = Album
    template_name = 'crud/mostrar_album.html'


class CrearFormato(CreateView):
    model = Formato
    template_name = "integrador/crear_formato.html"
    success_url = 'proyecto'
    fields = ['tipo']

class ListarFormato(ListView):
    model = Formato
    template_name = "integrador/listar_formato.html"


class EditarFormato(UpdateView):
    model = Formato
    template_name ='integrador/editar_formato.html'
    success_url = reverse_lazy('listar_formato')
    fields = ['tipo'] 


class EliminarFormato(DeleteView):
    model =  Formato
    template_name = "integrador/eliminar_formato.html"
    success_url = reverse_lazy('listar_formato')



class MostrarFormato(DetailView):
    model = Formato
    template_name = 'integrador/mostrar_formato.html'



class CrearTema(CreateView):        
    model = Tema
    template_name = "crud/crear_tema.html"
    success_url = 'proyecto'
    fields = ['titulo', 'duracion', 'autor', 'compositor', 'cod_album', 'interprete']

class ListarTema(ListView):
    model = Tema
    template_name = "crud/listar_tema.html"


class EditarTema(UpdateView):
    model = Tema
    template_name ='crud/editar_tema.html'
    success_url = reverse_lazy('listar_tema')
    fields = ['titulo','duracion','autor','compositor', 'cod_album', 'interprete'] 


class EliminarTema(DeleteView):
    model = Tema
    template_name = "crud/eliminar_tema.html"
    success_url = reverse_lazy('listar_tema')


class MostrarTema(DetailView):
    model = Tema
    template_name = 'mostrar_tema.html'


class CrearInterprete(CreateView):        
    model = Interprete
    template_name = "crud/crear_interprete.html"
    success_url = 'proyecto'
    fields = ['nombre', 'foto']


class ListarInterprete(ListView):
    model = Interprete
    template_name = "crud/listar_interprete.html"


class EditarInterprete(UpdateView):
    model = Interprete
    template_name ='crud/editar_interprete.html'
    success_url = reverse_lazy('listar_interprete')
    fields = ['nombre', 'foto'] 


class EliminarInterprete(DeleteView):
    model = Interprete
    template_name = "crud/eliminar_interprete.html"
    success_url = reverse_lazy('listar_interprete')


class MostrarInterprete(DetailView):
    model = Interprete
    template_name = 'crud/mostrar_interprete.html'



class CrearGenero(CreateView):        
    pass # a completar por lizbeth


class ListarGenero(ListView):
    pass # a completar por lizbeth


class EditarGenero(UpdateView):
    pass # a completar por lizbeth 


class EliminarGenero(DeleteView):
    pass # a completar por lizbeth


class MostrarGenero(DetailView):
    pass # a completar por lizbeth


class CrearDiscografica(CreateView):        
    pass #a completar por joaquin


class ListarDiscografica(ListView):
    pass #a completar por joaquin


class EditarDiscografica(UpdateView):
    pass #a completar por joaquin


class EliminarDiscografica(DeleteView):
    pass #a completar por joaquin


class MostrarDiscografica(DetailView):
    pass #a completar por joaquin