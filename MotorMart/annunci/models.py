from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class Annuncio(models.Model):

    cambio_opzioni = [
        ('automatico', 'Automatico'),
        ('manuale', 'Manuale'),
    ]

    stato_opzioni = [
        ('ottimo', 'Ottimo'),
        ('buono', 'Buono'),
        ('danneggiato', 'Danneggiato'),
    ]

    carburante_opzioni = [
        ('benzina', 'Benzina'),
        ('diesel', 'Diesel'),
        ('GPL', 'GPL'),
        ('metano', 'Metano'),
        ('elettrico', 'Elettrico')
    ]

    marca = models.CharField(max_length=20)
    modello = models.CharField(max_length=30)
    anno = models.IntegerField()
    prezzo = models.IntegerField()
    chilometraggio = models.IntegerField()
    potenza = models.IntegerField()
    cilindrata = models.IntegerField()
    stato = models.CharField(max_length=20, choices=stato_opzioni)
    carburante = models.CharField(max_length=20, choices=carburante_opzioni)
    cambio = models.CharField(max_length=20, choices=cambio_opzioni)
    colore = models.CharField(max_length=30)
    immagine = models.ImageField(upload_to ='static/img/uploads') 
    descrizione = models.CharField(max_length=200)
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inserimento = models.DateTimeField(default=timezone.now, blank=True)
    venduto = models.BooleanField(null=True, blank=True)
    compratore = models.IntegerField(null=True, blank=True)
    prezzo_acquisto = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.modello
