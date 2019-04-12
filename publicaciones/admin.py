from django.contrib import admin

# Register your models here.

class ArchivosInlines(admin.TabularInline):
    model = ArchivosCatalogos
    extra = 1

class CatalogosAdmin(admin.ModelAdmin):
    inlines = [ArchivosInlines]
    list_display = ['titulo', 'year', 'autores', '_tiene_pdf']
    search_fields = ('titulo', 'autores',)
