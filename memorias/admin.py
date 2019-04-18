from django.contrib import admin
from .models import Memorias, ArchivosMemorias
# Register your models here.

class InlinesMemorias(admin.TabularInline):
    model = ArchivosMemorias
    extra = 1

class MemoriasAdmin(admin.ModelAdmin):
    inlines = [InlinesMemorias]
    list_display = ['titulo','fecha']
    search_fields = ['titulo']

admin.site.register(Memorias, MemoriasAdmin)
