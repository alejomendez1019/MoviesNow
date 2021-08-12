from django.urls import path, include
from .views import home, contacto, agregar_pelicula, listar_pelicula, modificar_pelicula, eliminar_pelicula, \
    registro, PeliculaViewset, GeneroViewset, admin
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('pelicula', PeliculaViewset)
router.register('genero', GeneroViewset)


urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-pelicula/', agregar_pelicula, name="agregar_pelicula"),
    path('listar-pelicula/', listar_pelicula, name="listar_pelicula"),
    path('modificar-pelicula/<id>/', modificar_pelicula, name="modificar_pelicula"),
    path('eliminar-pelicula/<id>/', eliminar_pelicula, name="eliminar_pelicula"),
    path('registro/', registro, name="registro"),
    path('admin/', admin, name="admin"),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)