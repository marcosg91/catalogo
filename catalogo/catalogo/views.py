from django.shortcuts import render 

def inicio(request):
    template_name = "index.html"
    contexto = {
        'nombre': "Marcos"
    }
    return render( request, template_name, contexto)