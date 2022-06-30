from django.db import models

# Create your models here.
JUGUETES_MASCOTAS = (
    ('Perros', 'Perros'),
    ('Gatos', 'Gatos'),
)

class Producto (models.Model):
    fotografia = models.ImageField(upload_to='producto')
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    tipo_juguete = models.CharField(max_length=50, choices=JUGUETES_MASCOTAS)

    def __str__(self):
        return str(self.fotografia)