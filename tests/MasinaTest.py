from django.test import TestCase
from project01.masina.models import Masini


class MasinaTestCase(TestCase):

    def setUp(self):
        Masini.objects.create(marca="Logan XXX", pret=1500.0)

