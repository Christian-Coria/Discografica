from django.contrib import admin
from .models import Formato ,Interprete,Tema, Genero, Album,  Discografica

admin.site.register(Formato)
admin.site.register(Interprete)
admin.site.register(Genero)
admin.site.register(Tema)
admin.site.register(Discografica)
admin.site.register(Album)