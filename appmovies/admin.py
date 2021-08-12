from django.contrib import admin
from .models import Genero, Pelicula, Contacto
from .forms import PeliculaForm

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "genero"]
    list_editable = ["precio", "genero"]
    search_fields = ["nombre"]
    list_filter = ["genero"]
    list_per_page = 10
    form = PeliculaForm

admin.site.register(Genero)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Contacto)