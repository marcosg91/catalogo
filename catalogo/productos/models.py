from django.db import models

from categorias.models import Categoria
from usuarios.models import Usuario


class Producto(models.Model): 
    nombre = models.CharField(max_length=225)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion =models.TextField() 

    activo = models.BooleanField(default=True)

    # relacion para un producto una categoria 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, related_name="categorias", blank=True) # CASCADE borra en cascada todos los elementos si se elimina una categoria

    # relacion para un producto mas de una categoria 
    categoria2 = models.ManyToManyField(Categoria) # aqui django crea en la base de datos automaticamente una tabla intermedia y relaciona las fk de productos y categorias 

    imagen = models.ImageField(upload_to="productos", null=True, blank=True)
    # models.FieldFile campo para archivos 
    # models.BinaryField campo para guardar ruta mas archivo completo


   # ficha = models.OneToOneField(Ficha) en el caso de requerir que un producto tenga una sola ficha y esa ficha tenga un solo producto
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, related_name="productos", blank=True)
   
   
    def __str__(self):
        return self.nombre

class MeGusta (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


"""
x = Producto.objects.filter(id = 1).first() #exists()
if x:
    pass
"""

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
    