from django.contrib import admin
from .models import Proposta

class PropostaAdmin(admin.ModelAdmin):
    list_display = ('annuncio', 'utente', 'prezzo', 'accettata', 'data_inserimento')
    list_filter = ('annuncio', 'utente', 'accettata', 'data_inserimento')

admin.site.register(Proposta, PropostaAdmin)
