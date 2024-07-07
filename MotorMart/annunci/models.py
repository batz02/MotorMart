from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    immagine = models.ImageField(upload_to ='media/uploads/') 
    descrizione = models.CharField(max_length=200)
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inserimento = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.modello
