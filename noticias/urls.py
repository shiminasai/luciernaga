from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('noticias/',
         views.NoticiasListView.as_view(), name='noticias_list'),
    path('noticia/<int:pk>-<str:slug>',
         views.NoticiaDetailView.as_view(), name='noticia_detail'),
    path('eventos/',
         views.EventosListView.as_view(), name='eventos_list'),
    path('evento/<int:pk>-<str:slug>',
         views.EventoDetailView.as_view(), name='evento_detail'),
    path('videotecas/',
         views.VideotecasListView.as_view(), name='videoteca_list'),
    path('videoteca/<int:pk>-<str:slug>',
         views.VideotecaDetailView.as_view(), name='videoteca_detail'),
    path('contactenos/',
        views.ContactenosView.as_view(), name='contactenos'),
    path('publicaciones/',
        views.PublicacionesListView.as_view(), name='publicaciones'),
    path('detalle-publicacion/<int:pk>-<str:slug>',
        views.PublicacionDetailView.as_view(), name='publicacion_detail'),
    #path('busqueda-videoteca',
    #    views.busqueda_videoteca, name='busqueda_videoteca'),
    path(
        'ajax/subtemas/',
        views.get_subtemas,
        name='get-subtemas',
    ),
]
