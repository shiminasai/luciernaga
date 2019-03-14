from django.shortcuts import render
from .forms import BusquedaVideoteca

# Create your views here.

def busqueda_videoteca(request, template='videoteca.html'):

    return render(request, template, locals())
