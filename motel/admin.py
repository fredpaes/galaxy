from django.contrib import admin
from .models import Servicio, Producto, Categoria, Hostal

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Hostal)