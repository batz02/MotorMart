from django.db import models
from annunci.models import Annuncio
from django.contrib.auth.models import User
from django.utils import timezone


class Proposta(models.Model):
    annuncio = models.ForeignKey(Annuncio, on_delete=models.CASCADE, related_name='annuncio')
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    prezzo = models.IntegerField()
    accettata = models.BooleanField(null=True, blank=True)
    data_inserimento = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f'{self.annuncio.marca} {self.annuncio.modello} - {self.prezzo}'
