from django.shortcuts import render
from .models import *

def listarCatalogo(request):
    modelos = Modelo.objects.filter().order_by('categoriaModelo')
    return render(request, 'Catalogo/listarCatalogo.html', {'modelos' : modelos})