# -*- coding: utf-8 -*-
from django.db import models
from django.template import defaultfilters
from sorl.thumbnail import ImageField
# Create your models here.

class Publicaciones(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)
    portada = ImageField(upload_to='publicaciones/')
    sinopsis = models.TextField()
    year = models.CharField('año', max_length=20)
    autores = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
      self.slug = defaultfilters.slugify(self.titulo)
      super(Publicaciones, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def _tiene_pdf(self, *args, **kwargs):
        if self.archivospublicaciones_set.count() > 0:
            return True
        return False
    _tiene_pdf.boolean = True

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'


class ArchivosPublicaciones(models.Model):
    catalogo = models.ForeignKey(Publicaciones, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivosPublicaciones/')

    class Meta:
        verbose_name = 'Archivo para publicación'
        verbose_name_plural = 'Archivos para las publicaciones'

class EnlaceVideoteca(models.Model):
    publicacion = models.ForeignKey(Publicaciones, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    url = models.URLField()

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Enlace Videoteca'
        verbose_name_plural = 'Enlaces Videotecas'
