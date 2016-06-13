from django.db import models
from django.utils import timezone

class Activmad(models.Model):
    titulo = models.CharField(max_length=200)
    fechaevento = models.DateTimeField()
    fechafin =  models.DateTimeField()
    descricion = models.CharField(max_length=300)
    tipo= models.CharField(max_length=200)
    idevento = models.CharField(max_length=30)
    
    
def __str__(self):
    return self.titulo