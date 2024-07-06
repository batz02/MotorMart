from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Recensione(models.Model):
    utente_inserimento = models.ForeignKey(User,on_delete=models.CASCADE, related_name="utente_ins")
    utente_riferimento = models.ForeignKey(User,on_delete=models.CASCADE, related_name="utente_rif")
    descrizione = models.CharField(max_length=200)
    rating = models.IntegerField()
    data_inserimento = models.DateTimeField(default=datetime.now, blank=True)