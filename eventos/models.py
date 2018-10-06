from django.db import models
from django.template import defaultfilters

from geoposition.fields import GeopositionField
from sorl.thumbnail import ImageField

# Create your models here.

class Eventos(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    portada = ImageField(upload_to='eventos/')
    fecha_inicio = models.DateTimeField()
    fecha_finalizacion = models.DateTimeField()
    descripcion = models.TextField()
    lugar = models.CharField(max_length=250)
    name = models.CharField('Ciudad', max_length=100)
    position = GeopositionField()

    adjunto = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def save(self, *args, **kwargs):
      self.slug = defaultfilters.slugify(self.titulo)
      super(Eventos, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
