from django.contrib import admin
from .models import Chat, Message

class ChatAdmin(admin.ModelAdmin):
    list_display = ('utente1', 'utente2')
    list_filter = ('utente1', 'utente2')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'sender', 'timestamp', 'content')
    list_filter = ('chat', 'sender', 'timestamp')

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
