from django.db import models

from socialbooking.authentication.models import User
from socialbooking.catalog.models import Stay

class Category(models.Model):

    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'

    name = models.CharField(
        max_length=30, help_text="Введите название", verbose_name="Название"
    )

    def __str__(self):
        return self.name


class Service(models.Model):

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ServiceOption(models.Model):

    class Meta:
        verbose_name = 'Опция услуг'
        verbose_name_plural = 'Опции услуг'

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.price} Р.)"

class StayService(models.Model):

    class Meta:
        verbose_name = 'Набор услуг'
        verbose_name_plural = 'Наборы услуг'

    stay = models.ForeignKey(Stay, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    options = models.ManyToManyField(ServiceOption, blank=True)

    def __str__(self):
        return f"{self.service.name}"

# Create your models here.


# class Service(models.Model):
#     name = models.CharField(
#         max_length=30, help_text="Введите название", verbose_name="Название"
#     )
#     category = models.ForeignKey(
#         "Category",
#         on_delete=models.CASCADE,
#         help_text="Выберите категорию",
#         verbose_name="Услуга ",
#     )

#     price = models.FloatField(help_text="Введите значение", verbose_name="Цена")
#     images = models.ImageField(
#         help_text="Выберите изображение", verbose_name="Изображение"
#     )

#     def __str__(self):
#         return self.name

class Provide(models.Model):
    dataprovide = models.DateTimeField(
        help_text="Введите значение", verbose_name="Дата оказания услуги"
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        help_text="Выберите услугу",
        verbose_name="Услуга ",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Выберите пользователя",
        verbose_name="Отдыхающий ",
    )
    dataprovide = models.DateTimeField(
        help_text="Введите значение", verbose_name="Дата оказания услуги"
    )
