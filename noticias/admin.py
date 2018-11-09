from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django import forms
from .models import Noticias, Temas
from sorl.thumbnail.admin import AdminImageMixin
from tinymce import TinyMCE

class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FlatPage
        fields = '__all__'


class PageAdmin(FlatPageAdmin):
    form = FlatPageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)

class AdminNoticias(AdminImageMixin, admin.ModelAdmin):
    '''
        Admin View for
    '''
    list_display = ('titulo','portada','fecha','usuario')
    list_filter = ('fecha',)
    search_fields = ('titulo',)

admin.site.register(Noticias, AdminNoticias)
admin.site.register(Temas)


