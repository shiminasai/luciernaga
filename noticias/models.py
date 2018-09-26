# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
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
    fecha = models.DateTimeField()
    tema = models.ForeignKey('Temas',
                                                    on_delete=models.CASCADE,
                                                    )
    portada = ImageField(upload_to='media/portadas/')
    contenido = HTMLField()
    tags = TaggableManager()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
                                                        on_delete=models.CASCADE,
                                                        )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

