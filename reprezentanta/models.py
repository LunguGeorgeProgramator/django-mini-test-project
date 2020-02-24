from django.db import models


class Reprezentanta(models.Model):
    nume = models.CharField(max_length=255)
    localitate = models.CharField(max_length=255)
