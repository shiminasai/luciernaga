# -*- coding: utf-8 -*-

from django import forms

class BusquedaNoticias(forms.Form):
    titulo = forms.CharField(max_length=250, required=False)

class BusquedaEventos(forms.Form):
    titulo = forms.CharField(max_length=250, required=False)

class BusquedaPublicacion(forms.Form):
    titulo = forms.CharField(max_length=250, required=False,
                            widget=forms.TextInput(attrs={'class': "form-control",
                                                   'placeholder':"Buscar..."})
                            )

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Correo'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}))
