# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from .models import Noticias, Temas, PersonalLuciernaga
from eventos.models import Eventos
from videoteca.models import Videotecas, Temas, SubTemas
from memorias.models import Memorias
from videoteca.forms import BusquedaVideoteca
from publicaciones.models import Publicaciones
from .forms import BusquedaNoticias, BusquedaEventos, BusquedaPublicacion, ContactForm
import json
# Create your views here.

class HomeView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticias.objects.all().order_by('-fecha')[:4]
        context['eventos'] = Eventos.objects.all().order_by('-fecha_inicio')[:8]
        context['videotecas'] = Videotecas.objects.all().order_by('-id')[:8]
        context['total_videoteca'] = Videotecas.objects.count()

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

def get_subtemas(request):
    '''Metodo para obtener los subtemas via Ajax segun los temas selectos'''
    ids = request.GET.get('ids', '')
    dicc = {}
    resultado = []
    if ids:
        lista = ids.split(',')
        for id in lista:
            try:
                tema = get_object_or_404(Temas, pk=id)
                subtemas = SubTemas.objects.filter(tema__id=tema.pk).order_by('nombre')
            except:
                pass
            for obj in subtemas:
                dicc[obj.tema.nombre] = []
            for obj in subtemas:
                muni = {'id': obj.id, 'nombre': obj.nombre}
                if not muni in dicc[obj.tema.nombre]:
                    dicc[obj.tema.nombre].append(muni)

    resultado.append(dicc)
    #print(resultado)
    return HttpResponse(json.dumps(resultado), content_type='application/json')

class ContactenosView(FormView):
    form_class = ContactForm
    template_name = 'contactenos.html'
    success_url = '/contactenos/'

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super().form_valid(form)

    def send_mail(self, valid_data):
        message = "{name} / {email} dice: ".format(
        name=valid_data['name'],
        email=valid_data['email'])
        message += "\n\n{0}".format(valid_data['message'])
        send_mail(
            subject='Contacto desde la web',
            message=message,
            from_email='noreply@fundacionluciernaga.org',
            recipient_list=['crocha09.09@gmail.com'],
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal'] = PersonalLuciernaga.objects.all()
        return context
