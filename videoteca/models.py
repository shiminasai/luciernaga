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

class Coleccion(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Colleción'
        verbose_name_plural = 'Collecciones'

class Pais(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

class Series(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'serie'
        verbose_name_plural = 'series'

class Videotecas(models.Model):
    cod_cat = models.CharField('Codigo categoría', max_length=50)
    #fecha = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
    duracion = models.CharField('Duración' , max_length=150, null=True, blank=True)
    edicion = models.CharField('Edición', max_length=250, null=True, blank=True)
    fotografia = models.CharField('Fotografía', max_length=250, null=True, blank=True)
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    guion = models.CharField('Guión', max_length=250, null=True, blank=True)
    idioma = models.ForeignKey(Idiomas, on_delete=models.CASCADE)
    musica_original = models.CharField('Música original', max_length=250, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    pais_prod = models.ForeignKey( Pais, on_delete=models.CASCADE,
                            verbose_name='Pais de producción',  related_name='pais_produccion', null=True, blank=True)
    pais_ref = models.ForeignKey(Pais, on_delete=models.CASCADE,
                            verbose_name='Pais de referidos', related_name='pais_referidos', null=True, blank=True)
    produccion = models.CharField('Producción', max_length=250, null=True, blank=True)
    productora = models.CharField('Productora', max_length=250, null=True, blank=True)
    realizacion = models.CharField('Realización', max_length=250, null=True, blank=True)
    serie = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, blank=True)
    sintesis = models.TextField('Síntesis', null=True, blank=True)
    subtitulos = models.CharField('Subtítulos', max_length=250, null=True, blank=True)
    temas = models.ManyToManyField(Temas, verbose_name='Temas finales', blank=True)
    url_video = models.URLField(null=True, blank=True)
    imagen_portada = models.ImageField(null=True, blank=True)
    imagen_fill = models.ImageField(null=True, blank=True)
    #anio = models.CharField('Año', max_length=50)
    #apoyo = models.CharField('Apoyo de', max_length=50)

    def save(self, *args, **kwargs):
      self.slug = defaultfilters.slugify(self.titulo)
      super(Videotecas, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Videoteca'
        verbose_name_plural = 'Videotecas'

class GuiasVideoteca(models.Model):
    titulo = models.CharField('Titulo de la guia', max_length=50)
    guia = models.FileField(upload_to='/guiasVideotecas/')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Guia de videoteca'
        verbose_name_plural = 'Guias de videotecas'

class ColeccionesPDF(models.Model):
    pass
