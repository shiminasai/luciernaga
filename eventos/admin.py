from django.contrib import admin
from .models import Eventos
from .forms import FormEventoMapa

class EventoAdmin(admin.ModelAdmin):
    form = FormEventoMapa
    list_display = ('titulo','fecha_inicio','fecha_finalizacion',)
    search_fields = ('titulo', 'lugar',)

# Register your models here.
admin.site.register(Eventos, EventoAdmin)
