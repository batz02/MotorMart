from django.contrib import admin
from .models import Recensione

class RecensioneAdmin(admin.ModelAdmin):
    list_display = ('recensore', 'venditore', 'rating', 'data_inserimento', 'descrizione')
    list_filter = ('recensore', 'venditore', 'rating', 'data_inserimento')

admin.site.register(Recensione, RecensioneAdmin)
