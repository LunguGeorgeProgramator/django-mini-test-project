from django.db import models


class Masini(models.Model):
    marca = models.CharField(max_length=255)
    pret = models.FloatField()
