import os

from django.db import models
from reprezentanta.models import Reprezentanta


class Masini(models.Model):
    marca = models.CharField(max_length=255)
    pret = models.FloatField()
    reprezentanta = models.ForeignKey(Reprezentanta, blank=True, null=True, on_delete=models.SET_NULL)

    def delete(self):
        for image in self.media_set.all():
            if os.path.isfile(image.media.path):
                os.remove(image.media.path)
            image.delete()
        super(Masini, self).delete()