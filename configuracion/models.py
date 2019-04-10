# -*- coding: utf-8 -*-
from django.db import models
from solo.models import SingletonModel

# Create your models here.

class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Site Name')
    maintenance_mode = models.BooleanField(default=False)
    acerca = models.TextField()

    def __str__(self):
        return u"Sitio Configuración"

    class Meta:
        verbose_name = "Sitio Configuración"


class FotosPortada(models.Model):
    sitio = models.ForeignKey(SiteConfiguration, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    foto = models.FileField(upload_to='fotoportada/')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Foto de portada'
        verbose_name_plural = 'Fotos de las portadas'

class FotosSecciones(models.Model):
    sitio = models.ForeignKey(SiteConfiguration, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField('url de la seccion', max_length=50)
    foto = models.FileField(upload_to='fotosecciones/')

    def __str__(self):
        return 'fotos de secciones'

    class Meta:
        verbose_name = 'Foto de sección'
        verbose_name_plural = 'Fotos de las secciones'


class AcercaSecciones(models.Model):
    sitio = models.ForeignKey(SiteConfiguration, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Acerca de sección'
        verbose_name_plural = 'Acerca de secciones'
