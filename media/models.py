from django.db import models
from masina.models import Masini


class Media(models.Model):
    media = models.FileField(upload_to="masina/")
    masina = models.ForeignKey(Masini, on_delete=models.CASCADE)
