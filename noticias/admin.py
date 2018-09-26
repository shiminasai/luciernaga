from django.contrib import admin
from .models import Noticias, Temas

class AdminNoticias(admin.ModelAdmin):
    '''
        Admin View for
    '''
    list_display = ('titulo','fecha','usuario')
    list_filter = ('fecha',)
    search_fields = ('titulo',)

admin.site.register(Noticias, AdminNoticias)
admin.site.register(Temas)
