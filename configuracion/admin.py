from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration, FotosPortada, FotosSecciones, AcercaSecciones

class FotosInlines(admin.TabularInline):
    model = FotosPortada
    extra = 1
    max_num = 5

class SeccionesInlines(admin.TabularInline):
    model = FotosSecciones
    extra = 1
    max_num = 10

class AcercaInlines(admin.TabularInline):
    model = AcercaSecciones
    extra = 3

class SiteConfigAdmin(SingletonModelAdmin):
    inlines = [FotosInlines, SeccionesInlines, AcercaInlines]


admin.site.register(SiteConfiguration, SiteConfigAdmin)
