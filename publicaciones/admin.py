from django.contrib import admin
from .models import ArchivosPublicaciones, Publicaciones
# Register your models here.

class ArchivosInlines(admin.TabularInline):
    model = ArchivosPublicaciones
    extra = 1

class PublicacionesAdmin(admin.ModelAdmin):
    inlines = [ArchivosInlines]
    list_display = ['titulo', 'year', 'autores', '_tiene_pdf']
    search_fields = ('titulo', 'autores',)


admin.site.register(Publicaciones, PublicacionesAdmin)
