from django.db import models

from categorias.models import Categoria

class Producto(models.Model): 
    nombre = models.CharField(max_length=225)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion =models.TextField() 

    activo = models.BooleanField(default=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True) # CASCADE borra en cascada todos los elementos si se elimina una categoria

    def __str__(self):
        return self.nombre
