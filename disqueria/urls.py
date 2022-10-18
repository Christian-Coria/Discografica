from django.contrib import admin
from django.urls import path
from .views import (home, Contacto, About, ProyectoIntegrador, CrearFormato, EliminarFormato, EditarFormato, ListarFormato ,MostrarFormato,
CrearAlbum, EliminarAlbum ,EditarAlbum , ListarAlbum, MostrarAlbum, CrearTema, EliminarTema, EditarTema, ListarTema, MostrarTema, 
CrearInterprete, EliminarInterprete, EditarInterprete, ListarInterprete, CrearGenero, MostrarInterprete, EliminarGenero, EditarGenero, MostrarGenero ,ListarGenero,
CrearDiscografica,  EliminarDiscografica, EditarDiscografica, ListarDiscografica,  MostrarDiscografica )

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',home, name="index"),  
    path('contacto/', Contacto.as_view(), name="contacto"),
    path('about/', About.as_view(), name="about"),
    
    path('proyecto',ProyectoIntegrador.as_view(), name="proyecto"),         
   
    path('crear-album' , CrearAlbum.as_view(), name='crear_album'),
    path('eliminar-album/<int:pk>' , EliminarAlbum.as_view(), name='eliminar_album'),
    path('editar-album/<int:pk>' , EditarAlbum.as_view(), name='editar_album'),
    path('listar-album' , ListarAlbum.as_view(), name='listar_album'),
    path('mostrar-album/<int:pk>/' , MostrarAlbum.as_view(), name='mostrar_album'),

    path('crear-tema' , CrearTema.as_view(), name='crear_tema'),
    path('eliminar-tema/<int:pk>' , EliminarTema.as_view(), name='eliminar_tema'),
    path('editar-tema/<int:pk>' , EditarTema.as_view(), name='editar_tema'),
    path('listar-tema' , ListarTema.as_view(), name='listar_tema'),
    path('mostrar-tema/<int:pk>/' , MostrarTema.as_view(), name='mostrar_tema'),

        #NOTA: respetar los nombres de las creacion de las funciones, si los mismos deciden cambiarlos deben a su vez, 
               #cambiar el nombre en cada modulo del ruteo que corresponda!!!

    # los path formato a completar por mateo

    # los path interprete a completar por mateo

    # los path de genero a completar por lizbeth

    # los path de discografica a completar por joaquin

]

