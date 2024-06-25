from django.db import models
from datetime import datetime

# Create your models here.

class Annuncio(models.Model):
    marca = models.CharField(max_length=20)
    modello = models.CharField(max_length=30)
    anno = models.IntegerField()
    prezzo = models.IntegerField()
    chilometraggio = models.IntegerField()
    potenza = models.IntegerField()
    data_inserimento = datetime.now()