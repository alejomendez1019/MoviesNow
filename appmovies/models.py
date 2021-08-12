from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Pelicula(models.Model):

    nombre = models.CharField(max_length=150)
    precio = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="peliculas", null=True)
    
    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

class Contacto(models.Model):

    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mesaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre