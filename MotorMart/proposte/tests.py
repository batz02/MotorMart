from django.test import TestCase
from django.contrib.auth.models import User
from .models import Proposta, Annuncio

class PropostaModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.annuncio = Annuncio.objects.create(
            marca='Toyota',
            modello='Corolla',
            anno=2020,
            prezzo=20000,
            chilometraggio=50000,
            potenza=132,
            cilindrata=1798,
            stato='ottimo',
            carburante='benzina',
            cambio='automatico',
            colore='rosso',
            descrizione='Auto in ottime condizioni',
            utente=self.user,
            venduto=False
        )
        self.proposta = Proposta.objects.create(
            annuncio=self.annuncio,
            utente=self.user,
            prezzo=19000
        )

    def test_proposta_creation(self):
        self.assertIsInstance(self.proposta, Proposta)
        self.assertEqual(self.proposta.prezzo, 19000)
        self.assertIsNone(self.proposta.accettata)
        self.assertTrue(self.proposta.data_inserimento)

    def test_proposta_str(self):
        expected_object_name = f'{self.proposta.annuncio.marca} {self.proposta.annuncio.modello} - {self.proposta.prezzo}'
        self.assertEqual(expected_object_name, str(self.proposta))
