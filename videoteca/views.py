from django.shortcuts import render
from .forms import BusquedaVideoteca

# Create your views here.

def busqueda_videoteca(request, template='videoteca.html'):
    params = {}
    if request.method == 'POST':
        params['cod_cat__contains'] = request.POST.get('cod_cat')
        params['titulo__icontains'] = request.POST.get('titulo')
        params['serie__nombre__contains'] = request.POST.get('serie')
        params['genero__nombre__contains'] = request.POST.get('genero')
        params['temas__nombre__contains'] = request.POST.get('temas')
        params['pais__nombre__contains'] = request.POST.get('pais')
        params['anio__icontains'] = request.POST.get('anio')
        params['idioma__nombre__icontains'] = request.POST.get('idioma')

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)

    for key in unvalid_keys:
        del params[key]

    videoteca_list = Videotecas.objects.filter(**params)

    paginator = Paginator(videoteca_list, 10)
    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)


    return render(request, template, locals())
