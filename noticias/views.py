# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Noticias, Temas, PersonalLuciernaga
from eventos.models import Eventos
from videoteca.models import Videotecas, Temas, SubTemas
from memorias.models import Memorias
from videoteca.forms import BusquedaVideoteca
from publicaciones.models import Publicaciones
from .forms import BusquedaNoticias, BusquedaEventos, BusquedaPublicacion
import json
# Create your views here.

class HomeView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticias.objects.all().order_by('-fecha')[:4]
        context['eventos'] = Eventos.objects.all().order_by('-fecha_inicio')[:8]
        context['videotecas'] = Videotecas.objects.all().order_by('-id')[:8]

        return context

class AcercaView(TemplateView):

    template_name = 'acerca.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['memorias'] = Memorias.objects.all().order_by('-id')[:4]

        return context

class NoticiasListView(ListView):
    template_name = 'notas_lista.html'
    model = Noticias
    queryset =  Noticias.objects.order_by('-fecha')
    form_class = BusquedaNoticias
    #paginated_by = 12

    def get_queryset(self):
        params = {}

        form = self.form_class(self.request.GET)
        if form.is_valid():
            params['titulo__icontains'] = form.cleaned_data['titulo']
            unvalid_keys = []
            for key in params:
                if not params[key]:
                    unvalid_keys.append(key)

            for key in unvalid_keys:
                del params[key]
            return Noticias.objects.filter(**params)
        return Noticias.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaNoticias()

        return context

class NoticiaDetailView(DetailView):
    model = Noticias
    template_name = 'blog_single.html'
    #context_object_name = 'nota'
    form_class = BusquedaNoticias

    def get_queryset(self):
        params = {}

        form = self.form_class(self.request.GET)
        if form.is_valid():
            params['titulo__icontains'] = form.cleaned_data['titulo']
            unvalid_keys = []
            for key in params:
                if not params[key]:
                    unvalid_keys.append(key)

            for key in unvalid_keys:
                del params[key]
            return Noticias.objects.filter(**params)
        return Noticias.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_noticias'] = Noticias.objects.exclude(pk=self.object.pk).order_by('-fecha')[:3]
        context['temas'] = Temas.objects.all()
        context['form'] = BusquedaNoticias()

        return context

class EventosListView(ListView):
    template_name = 'eventos_lista.html'
    model = Eventos
    queryset =  Eventos.objects.order_by('-fecha_inicio')
    form_class = BusquedaEventos
    #paginated_by = 12

    def get_queryset(self):
        params = {}

        form = self.form_class(self.request.GET)
        if form.is_valid():
            params['titulo__icontains'] = form.cleaned_data['titulo']
            unvalid_keys = []
            for key in params:
                if not params[key]:
                    unvalid_keys.append(key)

            for key in unvalid_keys:
                del params[key]
            return Eventos.objects.filter(**params)
        return Eventos.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaEventos()

        return context

class EventoDetailView(DetailView):
    model = Eventos
    template_name = 'event_single.html'
    #context_object_name = 'nota'
    form_class = BusquedaEventos

    def get_queryset(self):
        params = {}

        form = self.form_class(self.request.GET)
        if form.is_valid():
            params['titulo__icontains'] = form.cleaned_data['titulo']
            unvalid_keys = []
            for key in params:
                if not params[key]:
                    unvalid_keys.append(key)

            for key in unvalid_keys:
                del params[key]
            return Eventos.objects.filter(**params)
        return Eventos.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_noticias'] = Noticias.objects.order_by('-fecha')[:3]
        context['temas'] = Temas.objects.all()
        context['position'] = self.object.position.split(',')
        context['form'] = BusquedaEventos()

        return context

from django.db.models import Q
class VideotecasListView(ListView):
    template_name = 'videoteca.html'
    model = Videotecas
    form_class = BusquedaVideoteca
    #paginate_by = 12

    def get_queryset(self):
        params = {}
        queryset = Videotecas.objects.all()
        conteo_final = Videotecas.objects.all().count()
        frase = 'ÚLTIMAS PRODUCCIONES'

        form = self.form_class(self.request.GET)
        if form.is_valid():
            params['cod_cat__contains'] = form.cleaned_data['codigo_cat']
            if form.cleaned_data['titulo']:
                queryset = Videotecas.objects.filter(
                            Q(titulo__icontains=form.cleaned_data['titulo']) |
                            Q(sintesis__icontains=form.cleaned_data['titulo']) |
                            Q(observaciones__icontains=form.cleaned_data['titulo'])
                            )
            params['serie'] = form.cleaned_data['serie']
            params['genero'] = form.cleaned_data['genero']
            params['temas'] = form.cleaned_data['temas']
            params['pais_prod'] = form.cleaned_data['pais']
            params['anio__icontains'] = form.cleaned_data['anio']
            params['idioma'] = form.cleaned_data['idioma']
            unvalid_keys = []
            for key in params:
                if not params[key]:
                    unvalid_keys.append(key)

            for key in unvalid_keys:
                del params[key]

            if params or form.cleaned_data['titulo']:
                conteo_final = len(queryset.filter(**params))
                frase = 'RESULTADOS PRODUCCIONES'
                aja = queryset.filter(**params)
                return (aja, conteo_final, frase)
        return (queryset, conteo_final, frase)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaVideoteca()
        algo = self.get_queryset()
        context['object_list'] = algo[0]
        context['conteo'] = algo[1]
        context['frase'] = algo[2]

        return context

class VideotecaDetailView(DetailView):
    model = Videotecas
    template_name = 'detalle_videoteca.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_videotecas'] = Videotecas.objects.filter(genero=self.object.genero).exclude(pk=self.object.pk).order_by('-id')[:3]
        context['temas'] = Temas.objects.all()

        return context

class ContactenosView(TemplateView):
    template_name = 'contactenos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal'] = PersonalLuciernaga.objects.all()
        return context

class PublicacionesListView(ListView):
    template_name = 'publicaciones.html'
    model = Publicaciones
    queryset =  Publicaciones.objects.order_by('-id')
    form_class = BusquedaPublicacion

    def get_queryset(self):
        params = {}

        form = self.form_class(self.request.GET)
        if form.is_valid():
            params['titulo__icontains'] = form.cleaned_data['titulo']
            unvalid_keys = []
            for key in params:
                if not params[key]:
                    unvalid_keys.append(key)

            for key in unvalid_keys:
                del params[key]
            return Publicaciones.objects.filter(**params)
        return Publicaciones.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaPublicacion()

        return context

class PublicacionDetailView(DetailView):
    model = Publicaciones
    template_name = 'detalle_publicacion.html'
    #context_object_name = 'nota'
    form_class = BusquedaPublicacion

    def get_queryset(self):
        params = {}

        form = self.form_class(self.request.GET)
        if form.is_valid():
            params['titulo__icontains'] = form.cleaned_data['titulo']
            unvalid_keys = []
            for key in params:
                if not params[key]:
                    unvalid_keys.append(key)

            for key in unvalid_keys:
                del params[key]
            return Publicaciones.objects.filter(**params)
        return Publicaciones.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaPublicacion()

        return context


# def busqueda_videoteca(request, template='videoteca_busqueda.html'):
#     form = BusquedaVideoteca(request.POST or None)
#     params = {}
#     if request.method == 'POST':
#         params['cod_cat__contains'] = request.POST.get('codigo_cat')
#         params['titulo__icontains'] = request.POST.get('titulo')
#         params['serie__id'] = request.POST.get('serie')
#         params['genero__id'] = request.POST.get('genero')
#         params['temas__id'] = request.POST.get('temas')
#         params['pais__id'] = request.POST.get('pais')
#         params['anio__icontains'] = request.POST.get('anio')
#         params['idioma__id'] = request.POST.get('idioma')

#     unvalid_keys = []
#     for key in params:
#         if not params[key]:
#             unvalid_keys.append(key)

#     for key in unvalid_keys:
#         del params[key]

#     print(params)

#     videoteca_list = Videotecas.objects.filter(**params)
#     print("------------")
#     print(len(videoteca_list))
#     print("------------")

#     paginator = Paginator(videoteca_list, 12)
#     page = request.GET.get('page')
#     object_list = paginator.get_page(page)
    # try:
    #     object_list = paginator.page(page)
    # except PageNotAnInteger:
    #     object_list = paginator.page(1)
    # except EmptyPage:
    #     object_list = paginator.page(paginator.num_pages)

    #return render(request, template, locals())

class SearchResultsView(TemplateView):
    template_name = "notas_lista.html"

    def find_entries(self, query_string):
        found_entries = None
        if query_string:
            entry_query_page = get_query(query_string, ['title','category', 'keywords', ])

            found_entries = Study.objects.filter(entry_query_page).order_by('title')

        return found_entries

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        query_string = ''
        if ('q' in self.request.GET) and self.request.GET['q'].strip():
            query_string = self.request.GET['q']
        context["all_found_entries"] = self.find_entries(query_string)

        return context


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
def get_subtemas(request):
    '''Metodo para obtener los subtemas via Ajax segun los temas selectos'''
    ids = request.GET.get('ids', '')
    dicc = {}
    resultado = []
    if ids:
        lista = ids.split(',')
        for id in lista:
            tema = get_object_or_404(Temas, pk=id)
            subtema = SubTemas.objects.filter(tema__id=tema.pk).order_by('nombre')
            for obj in subtema:
                muni = {'id': obj.id, 'nombre': obj.nombre}
                #if not muni in dicc[obj.tema.nombre]:
                dicc[obj.tema.nombre] = muni

    resultado.append(dicc)
    print(resultado)
    return HttpResponse(json.dumps(resultado), content_type='application/json')
