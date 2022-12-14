from django.shortcuts import render 

from products.models import Producto
def admin_listado_productos(request):
    template_name='productos/listado.html'

    contexto = {
        'productos': Producto.objects.all()
    }
    return render( request, template_name, contexto)
