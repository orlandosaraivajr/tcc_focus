from django.test import TestCase
from core.models import FeriadoModel
from datetime import date

class NoFeriadoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
        
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
        
    def test_texto(self):
        self.assertContains(self.resp, 'Hoje não tem feriado')

class FeriadoTest(TestCase):
    def setUp(self):
        FeriadoModel.objects.create(nome='Feriado aleatório', 
                                    data=date.today())
        self.resp = self.client.get('/')
        
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
        
    def test_texto(self):
        self.assertContains(self.resp, 'Feriado aleatório')
        


class FeriadoModelTest(TestCase):
    def setUp(self):
        FeriadoModel.objects.create(nome='Feriado aleatório', 
                                    data=date.today())

    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_instances(self):
        cadastro = FeriadoModel.objects.first()
        self.assertIsInstance(cadastro.data, date)

    def test_data_in_SGBD(self):
        cadastro = FeriadoModel.objects.first()
        nome = cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, 'Feriado aleatório')
        data = cadastro.__dict__.get('data', '')
        self.assertEqual(data, date.today())