# -*- coding: utf-8 -*-

from django import forms
from .models import Generos, Series, Temas, Pais, Idiomas

class BusquedaVideoteca(forms.Form):
    codigo_cat = forms.CharField(max_length=250, required=False)
    titulo = forms.CharField(max_length=250, required=False)
    serie = forms.ModelChoiceField(queryset=Series.objects.all(), required=False)
    genero = forms.ModelChoiceField(queryset=Generos.objects.all(), required=False)
    temas = forms.ModelChoiceField(queryset=Temas.objects.all(), required=False)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=False)
    anio = forms.CharField(label='Año', max_length=250, required=False)
    idioma = forms.ModelChoiceField(queryset=Idiomas.objects.all(), required=False)
