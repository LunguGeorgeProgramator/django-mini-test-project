from django.test import TestCase
from reprezentanta.models import Reprezentanta


class MasinaTestClass(TestCase):

    def setUp(self):
        self.reprezentanta = Reprezentanta.objects.create(
            nume="Masini pentru toti",
            localitate="Mures"
        )

    def tearDown(self):
        self.reprezentanta.delete()

    def test_read_reprezentanta(self):
        self.assertEqual(self.reprezentanta.nume, "Masini pentru toti")
        self.assertEqual(self.reprezentanta.localitate, "Mures")

    def test_update_reprezentanta(self):
        self.reprezentanta.nume = "Masini pentru mine"
        self.reprezentanta.save()
        self.assertEqual(self.reprezentanta.nume, "Masini pentru mine")

    def test_create_method(self):
        response = self.client.get('/reprezentanta/create')
        self.assertEqual(200, response.status_code)

        response = self.client.post('/reprezentanta/store', {
            'nume': "Masini pentru toti",
            'localitate': "Mures",
            'masini[]': [1]
        })
        self.assertEqual(302, response.status_code)

    def test_update_method(self):
        response = self.client.get('/reprezentanta/edit/' + str(self.reprezentanta.id))
        self.assertEqual(200, response.status_code)

        response = self.client.post('/reprezentanta/' + str(self.reprezentanta.id) + '/update', {
            'nume': "Masini pentru mine",
            'localitate': "Arges"
        })
        self.assertEqual(302, response.status_code)

    def test_index_method(self):
        response = self.client.get('/reprezentanta')
        self.assertEqual(200, response.status_code)