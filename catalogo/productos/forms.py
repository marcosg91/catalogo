#clases que sirven para crear formularios a nivel .html

from django import forms 

from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model= Producto # a partir de este modelo
        fields=["nombre", "descripcion", "precio", "activo", "imagen", "categoria", "categoria2"] #que incluya estos campos


    def clean_precio(self):
        precio = self.cleaned_data ["precio"]
        if precio <= 0:
            raise forms.ValidationError ("el precio debe ser un numero positivo")
        return precio 


    
    
     