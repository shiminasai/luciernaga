from django import forms
from .models import Eventos

class FormEventoMapa(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormEventoMapa, self).__init__(*args, **kwargs)
        self.initial['position'] = '12.11586547566659,-86.2921142578125'

    class Meta:
        model = Eventos
        fields = '__all__'
