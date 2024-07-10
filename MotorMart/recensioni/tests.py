from django.db import IntegrityError
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Recensione
from django.utils import timezone
from django.urls import reverse
from annunci.models import Annuncio

class RecensioneModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username='recensore', password='testpass123')
        cls.user2 = User.objects.create_user(username='venditore', password='testpass123')
    
    def test_create_recensione(self):
        recensione = Recensione.objects.create(
            recensore=self.user1,
            venditore=self.user2,
            descrizione="Ottimo prodotto",
            rating=5,
            data_inserimento=timezone.now()
        )
        self.assertEqual(recensione.descrizione, "Ottimo prodotto")
        self.assertEqual(recensione.rating, 5)

    def test_unique_constraint(self):
        Recensione.objects.create(
            recensore=self.user1,
            venditore=self.user2,
            descrizione="Buon prodotto",
            rating=4,
            data_inserimento=timezone.now()
        )
        with self.assertRaises(IntegrityError):
            Recensione.objects.create(
                recensore=self.user1,
                venditore=self.user2,
                descrizione="Altro commento",
                rating=3,
                data_inserimento=timezone.now()
            )


class ReviewViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='recensore', password='testpass123')
        self.user2 = User.objects.create_user(username='venditore', password='testpass123')
        self.annuncio = Annuncio.objects.create(
            marca="Fiat",
            modello="500",
            anno=2020,
            prezzo=10000,
            chilometraggio=50000,
            potenza=95,
            cilindrata=1400,
            stato="ottimo",
            carburante="benzina",
            cambio="manuale",
            colore="rosso",
            descrizione="Descrizione di test",
            utente=self.user2,
            data_inserimento=timezone.now(),
            venduto=False
        )
        self.review_url = reverse('recensioni:review', kwargs={'pk': self.annuncio.pk})
        
        self.client.login(username='recensore', password='testpass123')

    def test_review_no_login(self):
        self.client.logout()
        response = self.client.get(self.review_url)
        self.assertRedirects(response, f'/login/?auth=notok&next={self.review_url}')

    def test_review_self(self):
        self.client.login(username='venditore', password='testpass123')
        response = self.client.get(self.review_url)
        self.assertEqual(response.status_code, 302) 

    def test_duplicate_review(self):
        self.client.post(self.review_url, {'rating': 5, 'descrizione': 'Ottimo!'})
        response = self.client.post(self.review_url, {'rating': 4, 'descrizione': 'Buono'})
        self.assertEqual(response.status_code, 302) 

    def test_successful_review_post(self):
        response = self.client.post(self.review_url, {'rating': 5, 'descrizione': 'Ottimo servizio'})
        self.assertEqual(response.status_code, 302) 
