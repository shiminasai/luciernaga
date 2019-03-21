# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Noticias, Temas, PersonalLuciernaga
from eventos.models import Eventos
from videoteca.models import Videotecas, CatalogosPDF
from videoteca.forms import BusquedaVideoteca

# Create your views here.

class HomeView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticias.objects.all().order_by('-fecha')[:4]
        context['eventos'] = Eventos.objects.all().order_by('-fecha_inicio')[:8]
        context['videotecas'] = Videotecas.objects.all().order_by('-id')[:8]

        return context

class NoticiasListView(ListView):
    template_name = 'notas_lista.html'
    model = Noticias

class NoticiaDetailView(DetailView):
    model = Noticias
    template_name = 'blog_single.html'
    #context_object_name = 'nota'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_noticias'] = Noticias.objects.exclude(pk=self.object.pk).order_by('-fecha')[:3]
        context['temas'] = Temas.objects.all()

        return context

class EventosListView(ListView):
    template_name = 'eventos_lista.html'
    model = Eventos

class EventoDetailView(DetailView):
    model = Eventos
    template_name = 'event_single.html'
    #context_object_name = 'nota'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_noticias'] = Noticias.objects.order_by('-fecha')[:3]
        context['temas'] = Temas.objects.all()
        context['position'] = self.object.position.split(',')

        return context

class VideotecasListView(ListView):
    template_name = 'videoteca.html'
    model = Videotecas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaVideoteca()

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


class CatalogosListView(ListView):
    template_name = 'publicaciones.html'
    model = CatalogosPDF

class CatalogoDetailView(DetailView):
    model = CatalogosPDF
    template_name = 'detalle_publicacion.html'


def busqueda_videoteca(request, template='videoteca_busqueda.html'):
    form = BusquedaVideoteca()
    params = {}
    if request.method == 'POST':
        params['cod_cat__contains'] = request.POST.get('codigo_cat')
        params['titulo__icontains'] = request.POST.get('titulo')
        params['serie__id'] = request.POST.get('serie')
        params['genero__id'] = request.POST.get('genero')
        params['temas__id'] = request.POST.get('temas')
        params['pais__id'] = request.POST.get('pais')
        params['anio__icontains'] = request.POST.get('anio')
        params['idioma__id'] = request.POST.get('idioma')

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
