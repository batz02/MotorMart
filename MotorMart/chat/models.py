from django.contrib.auth.models import User
from django.db import models

class Chat(models.Model):
    utente1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="utente1")
    utente2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="utente2")

    class Meta:
        unique_together = ['utente1', 'utente2']

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
