from django.db import models

from socialbooking.catalog.models import Stay, Photo

class Featured(models.Model):

    class Meta:
        verbose_name = 'Демонстрируемый объект'
        verbose_name_plural = 'Демонстрируемые объекты'
    
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    stay = models.ForeignKey(Stay, on_delete=models.CASCADE, blank=True)
