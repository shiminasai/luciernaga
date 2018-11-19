from django.contrib import admin
from django import forms
from solo.admin import SingletonModelAdmin
from tinymce import TinyMCE
from .models import SiteConfiguration, FotosPortada, FotosSecciones, AcercaSecciones

class MyFormContent(forms.ModelForm):
    contenido = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))

    class Meta:
        model = AcercaSecciones
        fields = '__all__'

class FotosInlines(admin.TabularInline):
    model = FotosPortada
    extra = 1
    max_num = 5

class SeccionesInlines(admin.TabularInline):
    model = FotosSecciones
    extra = 1
    max_num = 10

class AcercaInlines(admin.TabularInline):
    form = MyFormContent
    model = AcercaSecciones
    extra = 3

class SiteConfigAdmin(SingletonModelAdmin):
    inlines = [FotosInlines, SeccionesInlines, AcercaInlines]


admin.site.register(SiteConfiguration, SiteConfigAdmin)
