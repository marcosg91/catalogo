#clases que sirven para crear formularios a nivel .html

from django import forms 

from.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model= Producto # a partir de este modelo
        fields=["nombre", "descripcion", "precio", "activo", "imagen", "categoria", "categoria2"] #que incluya estos campos