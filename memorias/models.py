from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.

class Memorias(models.Model):
    portada = ImageField(upload_to='portadas/')
    titulo = models.CharField(max_length=250)
    fecha = models.DateField()
    descripcion = models.TextField('Descripción')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Memorias'

class ArchivosMemorias(models.Model):
    catalogo = models.ForeignKey(Memorias, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='memorias/')

    class Meta:
        verbose_name = 'Archivo para Memoria'
        verbose_name_plural = 'Archivos para las Memorias'
