from rest_framework import serializers
from .models import Producto
 
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('fotografia', 'codigo', 'nombre', 'tipo_juguete')