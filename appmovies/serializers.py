from .models import Pelicula, Genero
from  rest_framework import serializers

class GeneroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genero
        fields = '__all__'


class PeliculaSerializer(serializers.ModelSerializer):

    nombre_genero = serializers.CharField(read_only=True, source="genero.nombre")
    genero = GeneroSerializer(read_only=True)
    genero_id = serializers.PrimaryKeyRelatedField(queryset=Genero.objects.all(), source="genero")
    nombre = serializers.CharField(required=True, min_length=3)

    def validate_nombre(self, value):
        existe = Pelicula.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Esta pelicula ya existe")

        return value


    class Meta:
        model = Pelicula
        fields = '__all__'
