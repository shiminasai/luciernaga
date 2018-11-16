from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration, FotosPortada, FotosSecciones

class FotosInlines(admin.TabularInline):
    model = FotosPortada
    extra = 1

class SeccionesInlines(admin.TabularInline):
    model = FotosSecciones
    extra = 1

class SiteConfigAdmin(SingletonModelAdmin):
    inlines = [FotosInlines, SeccionesInlines]


admin.site.register(SiteConfiguration, SiteConfigAdmin)
