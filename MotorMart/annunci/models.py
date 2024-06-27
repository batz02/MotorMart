from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Annuncio(models.Model):
    marca = models.CharField(max_length=20)
    modello = models.CharField(max_length=30)
    anno = models.IntegerField()
    prezzo = models.IntegerField()
    chilometraggio = models.IntegerField()
    potenza = models.IntegerField()
    cilindrata = models.IntegerField()
    stato = models.CharField(max_length=20)
    carburante = models.CharField(max_length=20)
    cambio = models.CharField(max_length=20)
    colore = models.CharField(max_length=30)
    descrizione = models.CharField(max_length=200)
    utente = models.ForeignKey(User,on_delete=models.CASCADE,related_name="copie")
    data_inserimento = models.DateTimeField(default=datetime.now, blank=True)