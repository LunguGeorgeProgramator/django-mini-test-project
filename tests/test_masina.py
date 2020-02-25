# import sys

from django.test import TestCase
from masina.models import Masini


class MasinaTestClass(TestCase):

    def setUp(self):
        self.masina = Masini.objects.create(marca="Logan XXX", pret=1500.0)

    def tearDown(self):
        self.masina.delete()

    def test_read_masina(self):
        self.assertEqual(self.masina.marca, 'Logan XXX')
        self.assertEqual(self.masina.pret, 1500.0)

    def test_update_masina(self):
        self.masina.marca = 'Logan YYY'
        self.masina.save()
        self.assertEqual(self.masina.marca, 'Logan YYY')
        # sys.exit(Masini.objects.last().marca) ## for print outs and variable testing

    def test_create_method(self):
        response = self.client.get('/masina/create')
        self.assertEqual(200, response.status_code)

        response = self.client.post('/masina/store', {
            'marca': 'Logan nou',
            'pret': 15000.1,
            'reprezentanta_id': None
        })
        self.assertEqual(302, response.status_code)

    def test_update_method(self):
        response = self.client.get('/masina/edit/' + str(self.masina.id))
        self.assertEqual(200, response.status_code)

        response = self.client.post('/masina/' + str(self.masina.id) + '/update', {
            'marca': 'Logan nou',
            'pret': 16000.1,
            'reprezentanta_id': None
        })
        self.assertEqual(302, response.status_code)

    def test_index_method(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

