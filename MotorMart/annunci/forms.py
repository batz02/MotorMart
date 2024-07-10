from django import forms
from .models import Annuncio


class CreaAnnuncio(forms.ModelForm):

    class Meta:
        model = Annuncio
        fields = [
            'marca', 'modello', 'anno', 'prezzo', 'chilometraggio', 'potenza',
            'cilindrata', 'stato', 'carburante', 'cambio', 'colore', 'descrizione', 'immagine'
        ]

    def clean(self):
        cleaned_data = super().clean()
        anno = cleaned_data.get('anno')
        prezzo = cleaned_data.get('prezzo')
        chilometraggio = cleaned_data.get('chilometraggio')
        potenza = cleaned_data.get('potenza')
        cilindrata = cleaned_data.get('cilindrata')

        if anno is not None and anno < 1900:
            self.add_error('anno', 'L\'anno deve essere un numero positivo.')

        if prezzo is not None and prezzo <= 0:
            self.add_error('prezzo', 'Il prezzo deve essere un numero positivo.')

        if chilometraggio is not None and chilometraggio <= 0:
            self.add_error('chilometraggio', 'Il chilometraggio deve essere un numero positivo.')

        if potenza is not None and potenza <= 0:
            self.add_error('potenza', 'La potenza deve essere un numero positivo.')

        if cilindrata is not None and cilindrata <= 0:
            self.add_error('cilindrata', 'La cilindrata deve essere un numero positivo.')

        marca = cleaned_data.get('marca')
        modello = cleaned_data.get('modello')

        if marca:
            cleaned_data['marca'] = marca.capitalize()

        if modello:
            cleaned_data['modello'] = modello.capitalize()

        return cleaned_data
