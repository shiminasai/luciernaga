from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('noticia/<int:pk>-<str:slug>',
         views.NoticiaDetailView.as_view(), name='noticia_detail'),
    path('evento/<int:pk>-<str:slug>',
         views.EventoDetailView.as_view(), name='evento_detail'),
    path('videotecas/',
         views.VideotecaListView.as_view(), name='videoteca_list'),
    path('videoteca/<int:pk>-<str:slug>',
         views.VideotecaDetailView.as_view(), name='videoteca_detail'),
]
