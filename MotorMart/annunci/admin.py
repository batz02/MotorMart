from django.contrib import admin
from .models import Annuncio


class AnnuncioAdmin(admin.ModelAdmin):
    
    list_display = ('marca', 'modello', 'anno', 'prezzo', 'chilometraggio', 'potenza', 'cilindrata', 
                    'stato', 'carburante', 'cambio', 'colore', 'utente', 'data_inserimento', 'venduto')
    list_filter = ('stato', 'carburante', 'cambio', 'venduto', 'data_inserimento')

admin.site.register(Annuncio, AnnuncioAdmin)
