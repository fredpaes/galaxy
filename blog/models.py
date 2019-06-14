from django.db import models

# Create your models here.
class Post(models.Model):
    nombre = models.CharField(max_length=120)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.nombre