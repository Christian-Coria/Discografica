from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FormatoCreationForm(forms.Form):
    pass # a completar por mateo

    
class InterpreteCreationForm(forms.Form):
    pass # a completar por mateo

    
class GeneroCreationForm(forms.Form):
    pass # a completar por lizbeth

    
class DiscograficaCreationForm(forms.Form):
    pass #a completar por joaquin

    
class TemaCreationForm(forms.Form):
    titulo = forms.CharField(max_length=255)
    duracion = forms.IntegerField()
    autor = forms.CharField(max_length=255)
    compositor = forms.CharField(max_length=255)
    cod_album = forms.ForeignKey(Album,null=True, on_delete=forms.CASCADE)
    interprete = forms.CharField(max_length=255)

    
class AlbumCreationForm(forms.Form):                   

    nombre = forms.CharField(label='Nombre', max_length=30, required=False)
    interprete = forms.ForeignKey(Interprete, on_delete=forms.DO_NOTHING)
    genero = forms.ForeignKey(Genero, on_delete=forms.DO_NOTHING)
    cant_temas = forms.CharField(label='Cantidad de Temas', widget=forms.PasswordInput,required=False)
    discografica = forms.ForeignKey(Discografica, on_delete=forms.DO_NOTHING)
    fec_lanzamiento = forms.CharField(max_length=40)
    precio = forms.IntegerField()    
    cantidad = forms.IntegerField()