from django.db import models
from django.utils import timezone

class Carrot(models.Model):
    time = models.DateTimeField(default=timezone.now, null=True)
    temperature = models.FloatField()
    wetness = models.FloatField()
    award = models.FloatField()
    end_status = models.BooleanField(default=False)

    class Meta:
        ordering = ['time',]
