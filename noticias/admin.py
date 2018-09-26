from django.contrib import admin
from .models import Noticias, Temas
from sorl.thumbnail.admin import AdminImageMixin

class AdminNoticias(AdminImageMixin, admin.ModelAdmin):
    '''
        Admin View for
    '''
    list_display = ('titulo','portada','fecha','usuario')
    list_filter = ('fecha',)
    search_fields = ('titulo',)

admin.site.register(Noticias, AdminNoticias)
admin.site.register(Temas)
