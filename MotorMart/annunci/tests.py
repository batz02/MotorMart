from django.test import TestCase
from django.contrib.auth.models import User
from .models import Annuncio
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import ValidationError

class AnnuncioModelTest(TestCase):
    
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        self.annuncio = Annuncio.objects.create(
            marca='Fiat',
            modello='Panda',
            anno=2020,
            prezzo=10000,
            chilometraggio=15000,
            potenza=85,
            cilindrata=1200,
            stato='Usato',
            carburante='Benzina',
            cambio='Manuale',
            colore='Rosso',
            immagine='static/img/uploads/test_image.jpg',
            descrizione='Descrizione test annuncio',
            utente=self.user,
            data_inserimento=timezone.now()
        )
    
    def test_annuncio_creation(self):
        annuncio = self.annuncio
        self.assertTrue(isinstance(annuncio, Annuncio))
        self.assertEqual(str(annuncio), 'Panda') 
    
    def test_annuncio_fields(self):
        annuncio = self.annuncio
        self.assertEqual(annuncio.marca, 'Fiat')
        self.assertEqual(annuncio.modello, 'Panda')
        self.assertEqual(annuncio.anno, 2020)
        self.assertEqual(annuncio.prezzo, 10000)
        self.assertEqual(annuncio.chilometraggio, 15000)
        self.assertEqual(annuncio.potenza, 85)
        self.assertEqual(annuncio.cilindrata, 1200)
        self.assertEqual(annuncio.stato, 'Usato')
        self.assertEqual(annuncio.carburante, 'Benzina')
        self.assertEqual(annuncio.cambio, 'Manuale')
        self.assertEqual(annuncio.colore, 'Rosso')
        self.assertEqual(annuncio.immagine, 'static/img/uploads/test_image.jpg')
        self.assertEqual(annuncio.descrizione, 'Descrizione test annuncio')
        self.assertEqual(annuncio.utente, self.user)
        self.assertIsNotNone(annuncio.data_inserimento)

    def test_invalid_carburante_raises_error(self):
        annuncio = Annuncio(
            marca='Fiat',
            modello='Panda',
            anno=2020,
            prezzo=10000,
            chilometraggio=15000,
            potenza=85,
            cilindrata=1200,
            stato='ottimo',
            carburante='invalid_fuel',  
            cambio='manuale' 
        )
        with self.assertRaises(ValidationError):
            annuncio.full_clean()


class AnnunciViewTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

        self.annuncio1 = Annuncio.objects.create(
            marca='Fiat',
            modello='Panda',
            anno=2020,
            prezzo=10000,
            chilometraggio=15000,
            potenza=85,
            cilindrata=1200,
            stato='Usato',
            carburante='Benzina',
            cambio='Manuale',
            colore='Rosso',
            immagine='media/uploads/test_image.jpg',
            descrizione='Descrizione test annuncio 1',
            utente=self.user,
            data_inserimento=timezone.now()
        )

        self.annuncio2 = Annuncio.objects.create(
            marca='Toyota',
            modello='Corolla',
            anno=2021,
            prezzo=12000,
            chilometraggio=10000,
            potenza=100,
            cilindrata=1500,
            stato='Nuovo',
            carburante='Diesel',
            cambio='Automatico',
            colore='Blu',
            immagine='media/uploads/test_image2.jpg',
            descrizione='Descrizione test annuncio 2',
            utente=self.user,
            data_inserimento=timezone.now()
        )

    def test_listings_view(self):
        response = self.client.get(reverse('annunci:annunci_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'annunci/cars.html')
        self.assertContains(response, self.annuncio1.modello)
        self.assertContains(response, self.annuncio2.modello)

    def test_details_view(self):
        response = self.client.get(reverse('annunci:details', args=[self.annuncio1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'annunci/details.html')
        self.assertContains(response, self.annuncio1.prezzo)

    def test_search_view(self):
        response = self.client.post(reverse('annunci:search'), {'anno': 2020})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'annunci/cars.html')
        self.assertContains(response, self.annuncio1.modello)
        

