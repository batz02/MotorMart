from django import forms
from .models import Annuncio

class CreaAnnuncio(forms.ModelForm):
    stato_opzioni = [
        ('ottimo', 'Ottimo'),
        ('buono', 'Buono'),
        ('danneggiato', 'Danneggiato'),
    ]

    cambio_opzioni = [
        ('automatico', 'Automatico'),
        ('manuale', 'Manuale'),
    ]
    
    stato = forms.ChoiceField(label='Stato', choices=stato_opzioni)

    cambio = forms.ChoiceField(label='Cambio', choices=cambio_opzioni)

    class Meta:
        model = Annuncio
        fields = [
            'marca', 'modello', 'anno', 'prezzo', 'chilometraggio', 'potenza',
            'cilindrata', 'stato', 'carburante', 'cambio', 'colore', 'descrizione', 'immagine'
        ]
