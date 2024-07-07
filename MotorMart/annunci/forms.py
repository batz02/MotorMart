from django import forms
from .models import Annuncio

class CreaAnnuncio(forms.ModelForm):
    class Meta:
        model = Annuncio
        fields = ['marca', 'modello', 'anno', 'prezzo', 'chilometraggio', 'potenza',
                  'cilindrata', 'stato', 'carburante', 'cambio', 'colore', 'descrizione', 'immagine']
        