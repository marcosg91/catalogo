from django.db import models

from categorias.models import Categoria

class Producto(models.Model): 
    nombre = models.CharField(max_length=225)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion =models.TextField() 

    activo = models.BooleanField(default=True)

    # relacion para un producto una categoria 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, related_name="categorias") # CASCADE borra en cascada todos los elementos si se elimina una categoria

    # relacion para un producto mas de una categoria 
    categoria2 = models.ManyToManyField(Categoria) # aqui django crea en la base de datos automaticamente una tabla intermedia y relaciona las fk de productos y categorias 

   # ficha = models.OneToOneField(Ficha) en el caso de requerir que un producto tenga una sola ficha y esa ficha tenga un solo producto

    def __str__(self):
        return self.nombre

"""
c = Categoria.objects.get(id=1)
c.categorias.all()
"""

"""
# creacion de tabla intermedia de forma manual 
class ProductoCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True) 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True) 
    # fecha
"""
    