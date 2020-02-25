from django.db import models
from masina.models import Masini


class Recenzie(models.Model):
    autor = models.CharField(max_length=25)
    descriere = models.CharField(max_length=255)
    data_adaugari = models.DateTimeField()
    masina = models.ForeignKey(Masini, on_delete=models.CASCADE)
