# -*- coding: utf-8 -*-

from django import forms

class BusquedaNoticias(forms.Form):
    titulo = forms.CharField(max_length=250, required=False)

class BusquedaEventos(forms.Form):
    titulo = forms.CharField(max_length=250, required=False)
