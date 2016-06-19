from django.db import models
from django.utils import timezone

class Activmad(models.Model):
    tipo= models.CharField(max_length=200)
    idevento = models.CharField(max_length=30)
    titulo = models.CharField(max_length=200)
    fechaevento = models.DateTimeField()
    fechafin =  models.DateTimeField()
    descripcion = models.CharField(max_length=200)
    
class Activbcn(models.Model):
    tipo= models.CharField(max_length=200)
    idevento = models.CharField(max_length=30)
    titulo = models.CharField(max_length=200)
    fechaevento = models.DateTimeField()
    fechafin =  models.DateTimeField()
    
def __str__(self):
    return self.titulo