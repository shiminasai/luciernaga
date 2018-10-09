from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('noticia/<int:pk>-<str:slug>', views.NoticiaDetailView.as_view(), name='noticia_detail'),
    path('evento/<int:pk>-<str:slug>', views.EventoDetailView.as_view(), name='evento_detail'),
]
