from django.db import models


class Coordinates(models.Model):

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'

    latitude = models.DecimalField(max_digits=9, decimal_places=6, help_text='Широта')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, help_text='Долгота')

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"

class Region(models.Model):

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    name = models.CharField(max_length=255, help_text='Название региона')

    def __str__(self):
        return self.name

class City(models.Model):

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    name = models.CharField(max_length=255, help_text='Название города')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    coordinates = models.OneToOneField(Coordinates, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.name}, {self.region.name}"

class Address(models.Model):

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    building_number = models.CharField(max_length=10, blank=True)
    apartment_number = models.CharField(max_length=10, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        address = f"{self.city.name}, {self.street}, дом {self.house_number}"
        if self.building_number:
            address = address+', корпус '+self.building_number
        if self.apartment_number:
            address = address+', квартира '+self.apartment_number
        return address
