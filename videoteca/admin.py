from django.contrib import admin
from import_export import resources
from .models import ( Generos, Idiomas,
                                        Temas, Videotecas,
                                        Series, Pais,
                                        EnlacePublicacion,
                                        SubTemas,
                                    )
from import_export.admin import ImportExportModelAdmin

class VideotecasResource(resources.ModelResource):
    class Meta:
        model = Videotecas
        exclude = ('slug', )

class GenerosResource(resources.ModelResource):
    class Meta:
        model = Generos

class IdiomasResource(resources.ModelResource):
    class Meta:
        model = Idiomas

class TemasResource(resources.ModelResource):
    class Meta:
        model = Temas

class SeriesResource(resources.ModelResource):
    class Meta:
        model = Series

class PaisResource(resources.ModelResource):
    class Meta:
        model = Pais

# class ColeccionResource(resources.ModelResource):
#     class Meta:
#         model = Coleccion

class GenerosAdmin(ImportExportModelAdmin):
    resource_class = GenerosResource

class IdiomasAdmin(ImportExportModelAdmin):
    resource_class = IdiomasResource

class TemasAdmin(ImportExportModelAdmin):
    resource_class = TemasResource
    ordering = ['id']
    search_fields = ['nombre']

class SeriesAdmin(ImportExportModelAdmin):
    resource_class = SeriesResource

class PaisAdmin(ImportExportModelAdmin):
    resource_class = PaisResource

# class ColeccionAdmin(ImportExportModelAdmin):
#     resource_class = ColeccionResource

class EnlaceInlines(admin.TabularInline):
    model = EnlacePublicacion
    extra = 1

class VideotecasAdmin(ImportExportModelAdmin):
    resource_class = VideotecasResource
    inlines = [EnlaceInlines]
    list_display = ['cod_cat', 'titulo', 'genero']
    list_filter = ('genero', 'idioma',)
    search_fields = ('titulo', 'sintesis',)
    autocomplete_fields = ['temas']

    class Media:

        css = {
            "all": ('/static/css/bootstrap-multiselect.css', )
        }
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '/static/js/bootstrap.min.js',
            '/static/js/bootstrap-multiselect.js',
            '/static/js/admin_subtemas.js',
        )

class SubTemasAdmin(admin.ModelAdmin):
    list_display = ['tema','nombre']
    list_display_links = ['tema','nombre']

# Register your models here.
admin.site.register(Generos, GenerosAdmin)
admin.site.register(Idiomas, IdiomasAdmin)
admin.site.register(Temas, TemasAdmin)
admin.site.register(SubTemas, SubTemasAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Videotecas, VideotecasAdmin)
