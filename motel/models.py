from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(decimal_places=2, max_digits=8, default=0.0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre

class Hostal(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=250)
    referencia = models.CharField(max_length=300, null=True, blank=True)
    telefono = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.nombre