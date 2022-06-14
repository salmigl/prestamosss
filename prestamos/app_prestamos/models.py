from django.db import models

# Create your models here.

class Prestamo(models.Model):
    """
    Modelo de Prestamo
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    libro = models.CharField(max_length=50, null=True, blank=True)
    entregado = models.BooleanField(default=False)

    def str(self):
        return '{}'.format(self.id)
