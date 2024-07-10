from django import forms
from .models import Proposta
from annunci.models import Annuncio

class CreaProposta(forms.ModelForm):
    class Meta:
        model = Proposta
        fields = ['prezzo']

    def __init__(self, *args, **kwargs):
        self.annuncio = kwargs.pop('annuncio', None)
        super(CreaProposta, self).__init__(*args, **kwargs)

    def clean_prezzo(self):
        prezzo = self.cleaned_data.get('prezzo')
        if self.annuncio and prezzo >= self.annuncio.prezzo:
            self.add_error('prezzo', 'L\'anno deve essere un numero positivo.')
        return prezzo

    