from django.db import models
from django.template import defaultfilters

#from geoposition.fields import GeopositionField
from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager
from location_field.models.plain import PlainLocationField

# Create your models here.

class Eventos(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)
    portada = ImageField(upload_to='eventos/')
    fecha_inicio = models.DateTimeField()
    fecha_finalizacion = models.DateTimeField()
    descripcion = models.TextField()
    pais = models.CharField(max_length=50, null=True, blank=True)
    lugar = models.CharField(max_length=250)
    name = models.CharField('Ciudad', max_length=100)
    position = PlainLocationField(based_fields=['name'], zoom=7)

    adjunto = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    tags = TaggableManager()

    def save(self, *args, **kwargs):
      self.slug = defaultfilters.slugify(self.titulo)
      super(Eventos, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
