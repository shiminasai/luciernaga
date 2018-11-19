# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.template import defaultfilters
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
from sorl.thumbnail import ImageField
from tinymce import HTMLField

# Create your models here.

class Temas(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

class Noticias(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)
    fecha = models.DateTimeField()
    tema = models.ForeignKey('Temas',
                                                    on_delete=models.CASCADE,
                                                    )
    portada = ImageField(upload_to='portadas/')
    contenido = HTMLField()
    tags = TaggableManager()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
                                                        on_delete=models.CASCADE,
                                                        )
    def save(self, *args, **kwargs):
      self.slug = defaultfilters.slugify(self.titulo)
      super(Noticias, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'


class PersonalLuciernaga(models.Model):
    nombre_completo = models.CharField(max_length=250)
    foto = ImageField(upload_to='personal/')
    cargo = models.CharField(max_length=250)
    correo = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name_plural = 'Personal de Luciérnaga'
