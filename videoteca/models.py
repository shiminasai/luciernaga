# -*- coding: utf-8 -*-

from django.db import models
from django.template import defaultfilters

# Create your models here.

class Generos(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

class Idiomas(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

class Temas(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

class Videotecas(models.Model):
    cod_cat = models.CharField('Codigo categoría', max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)
    anio = models.CharField('Año', max_length=50)
    apoyo = models.CharField('Apoyo de', max_length=50)
    coleccion = models.CharField('Colección', max_length=250)
    duracion = models.CharField('Duración' , max_length=150)
    edicion = models.CharField('Edición', max_length=250, null=True, blank=True)
    fotografia = models.CharField('Fotografía', max_length=250)
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE,)
    guion = models.CharField('Guión', max_length=250, null=True, blank=True)
    idioma = models.ForeignKey(Idiomas, on_delete=models.CASCADE,)
    musica_original = models.CharField('Música original', max_length=250, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    pais_prod = models.CharField('Pais de producción', max_length=250, null=True, blank=True)
    pais_ref = models.CharField('Pais de referidos', max_length=250, null=True, blank=True)
    produccion = models.CharField('Producción', max_length=250, null=True, blank=True)
    productora = models.CharField('Productora', max_length=250)
    realizacion = models.CharField('Realización', max_length=250)
    serie = models.CharField(max_length=250)
    sintesis = models.TextField('Síntesis')
    subtitulos = models.CharField('Subtítulos', max_length=250)
    temas = models.ManyToManyField(Temas, verbose_name='Temas finales', blank=True)

    def save(self, *args, **kwargs):
      self.slug = defaultfilters.slugify(self.titulo)
      super(Videotecas, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Videoteca'
        verbose_name_plural = 'Videotecas'
