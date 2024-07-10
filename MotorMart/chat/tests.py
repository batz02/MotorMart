from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Chat, Message
from django.db.utils import IntegrityError
import datetime
from django.urls import reverse

class ChatModelTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='test123')
        self.user2 = User.objects.create_user(username='user2', password='test123')

    def test_chat_creation(self):
        chat = Chat.objects.create(utente1=self.user1, utente2=self.user2)
        self.assertIsInstance(chat, Chat)

    def test_unique_together_constraint(self):
        Chat.objects.create(utente1=self.user1, utente2=self.user2)
        with self.assertRaises(IntegrityError):
            Chat.objects.create(utente1=self.user1, utente2=self.user2)

class MessageModelTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='test123')
        self.user2 = User.objects.create_user(username='user2', password='test123')
        self.chat = Chat.objects.create(utente1=self.user1, utente2=self.user2)

    def test_message_creation(self):
        message = Message.objects.create(chat=self.chat, sender=self.user1, content="Hello World", timestamp=datetime.datetime.now())
        self.assertEqual(message.sender, self.user1)
        self.assertEqual(message.content, "Hello World")


class ChatViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='test123')
        self.user2 = User.objects.create_user(username='user2', password='test123')
        self.chat = Chat.objects.create(utente1=self.user1, utente2=self.user2)
        self.client.login(username='user1', password='test123')

    def test_chat_list_view(self):
        response = self.client.get(reverse('chat:chat_list'))
        self.assertEqual(response.status_code, 200)

