#dentro de la libreria shortcuts esta la funcion render 
from django.shortcuts import render 

def inicio(request):
    template_name = "index.html"
    contexto = {
    }
    return render( request, template_name, contexto)