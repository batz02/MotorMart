from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Recensione(models.Model):
    
    rating_opzioni = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

    recensore = models.ForeignKey(User,on_delete=models.CASCADE, related_name="recensore")
    venditore = models.ForeignKey(User,on_delete=models.CASCADE, related_name="venditore")
    descrizione = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(choices=rating_opzioni)
    data_inserimento = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        unique_together = ('recensore', 'venditore')