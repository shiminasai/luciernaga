from django.contrib import admin
from import_export import resources
from .models import Generos, Idiomas, Temas, Videotecas
from import_export.admin import ImportExportModelAdmin

class VideotecasResource(resources.ModelResource):
    class Meta:
        model = Videotecas
        exclude = ('slug', )

class VideotecasAdmin(ImportExportModelAdmin):
    resource_class = VideotecasResource

# Register your models here.
admin.site.register(Generos)
admin.site.register(Idiomas)
admin.site.register(Temas)
admin.site.register(Videotecas, VideotecasAdmin)
