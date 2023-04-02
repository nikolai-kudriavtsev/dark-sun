from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Type(models.Model):
    name = models.CharField(
        max_length=30, help_text="Введите название", verbose_name="Название"
    )

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(
        max_length=30, help_text="Введите название", verbose_name="Название"
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        max_length=30, help_text="Введите название", verbose_name="Название"
    )

    def __str__(self):
        return self.name


class Sweets(models.Model):
    name = models.CharField(
        max_length=30, help_text="Введите название", verbose_name="Название"
    )

    def __str__(self):
        return self.name


class Bank(models.Model):
    name = models.CharField(
        max_length=30, help_text="Введите название", verbose_name="Название"
    )
    inn = models.FloatField(help_text="Введите значение", verbose_name="Инн")
    telephone = models.CharField(
        max_length=11, help_text="Введите номер телефона", verbose_name="Номер телефона"
    )
    price = models.FloatField(help_text="Введите значение", verbose_name="Цена")

    def __str__(self):
        return self.name


class Typerooms(models.Model):
    name = models.CharField(
        max_length=30, help_text="Введите название", verbose_name="Название"
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(
        max_length=30, help_text="Введите название", verbose_name="Название"
    )

    def __str__(self):
        return self.name


class Worker(models.Model):
    surname = models.CharField(
        max_length=30, help_text="Введите фамилия", verbose_name="Фамилия"
    )
    name = models.CharField(max_length=30, help_text="Введите имя", verbose_name="Имя")
    patronymic = models.CharField(
        max_length=30, help_text="Введите отчество", verbose_name="Отчество"
    )
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        help_text="Выберите должность",
        verbose_name="Должность",
    )
    databirth = models.DateTimeField(
        help_text="Введите значение", verbose_name="Дата рождения"
    )

    def __str__(self):
        return self.surname


class Object(models.Model):
    name = models.CharField(
        max_length=30, help_text="Введите название", verbose_name="Название"
    )
    type = models.ForeignKey(
        "Type", on_delete=models.CASCADE, verbose_name="Тип объекта "
    )
    region = models.ForeignKey(
        "Region",
        on_delete=models.CASCADE,
        help_text="Выберите регион",
        verbose_name="Регион объекта ",
    )
    city = models.ForeignKey(
        "City",
        on_delete=models.CASCADE,
        help_text="Выберите город",
        verbose_name="Город объекта ",
    )
    sweets = models.ForeignKey(
        "Sweets",
        on_delete=models.CASCADE,
        help_text="Выберите улицу",
        verbose_name="Улица объекта ",
    )
    home = models.FloatField(help_text="Введите значение", verbose_name="Дом")
    telephone = models.FloatField(help_text="Введите значение", verbose_name="Телефон")
    email = models.CharField(
        max_length=30, help_text="Введите еmail", verbose_name="Email"
    )

    price = models.FloatField(help_text="Введите значение", verbose_name="Цена")
    images = models.ImageField(
        help_text="Выберите изображение", verbose_name="Изображение"
    )
    #     код директора
    def __str__(self):
        return self.name


class Rooms(models.Model):
    room = models.CharField(
        max_length=50, help_text="Введите комнату", verbose_name="Комната"
    )
    floor = models.CharField(
        max_length=50, help_text="Введите этаж", verbose_name="Этаж"
    )
    people = models.CharField(
        max_length=50,
        help_text="Введите количество людей",
        verbose_name="Количество людей",
    )
    price = models.FloatField(help_text="Введите значение", verbose_name="Цена")
    typerooms = models.ForeignKey(
        "Typerooms",
        on_delete=models.CASCADE,
        help_text="Выберите тип комнаты",
        verbose_name="Тип комнаты",
    )
    object = models.ForeignKey(
        "Object",
        on_delete=models.CASCADE,
        help_text="Выберите объект",
        verbose_name="Объект ",
    )

    def __str__(self):
        return self.room


class User(AbstractUser):
    surname = models.CharField(
        max_length=30, help_text="Введите фамилия", verbose_name="Фамилия"
    )
    name = models.CharField(max_length=30, help_text="Введите имя", verbose_name="Имя")
    patronymic = models.CharField(
        max_length=30, help_text="Введите отчество", verbose_name="Отчество"
    )
    databirth = models.DateTimeField(
        help_text="Введите значение", verbose_name="Дата рождения", null=True
    )
    telephone = models.FloatField(
        help_text="Введите значение", verbose_name="Номер телефона", null=True
    )
    email = models.CharField(
        max_length=50, help_text="Введите значение", verbose_name="Email", null=True
    )
    pas_seria = models.FloatField(
        help_text="Введите значение", verbose_name="Серия паспорта", null=True
    )
    pas_number = models.FloatField(
        help_text="Введите значение", verbose_name="Номер паспорта", null=True
    )
    pas_data = models.DateTimeField(
        help_text="Введите значение", verbose_name="Дата выдачи", null=True
    )
    pas_who = models.CharField(
        max_length=50, help_text="Введите значение", verbose_name="Кем выдан", null=True
    )
    home = models.FloatField(
        help_text="Введите значение", verbose_name="Номер дома", null=True
    )
    kvartira = models.FloatField(
        help_text="Введите значение", verbose_name="Номер квартиры", null=True
    )

    def __str__(self):
        return "".join([self.surname, self.name, self.patronymic])


class Schedule(models.Model):

    data_check = models.DateTimeField(
        help_text="Введите значение", verbose_name="Дата заезда"
    )
    data_exit = models.DateTimeField(
        help_text="Введите значение", verbose_name="Дата выезда"
    )
    object = models.ForeignKey(
        "Object", on_delete=models.CASCADE, verbose_name="Объект "
    )

    def __str__(self):
        return self.data_check


class Dogovor(models.Model):
    number = models.CharField(
        max_length=50, help_text="Введите значение", verbose_name="Номер"
    )
    datadogovor = models.DateTimeField(
        help_text="Введите значение", verbose_name="Дата заключения договора"
    )
    object = models.ForeignKey(
        "Object",
        on_delete=models.CASCADE,
        help_text="Выберите объект",
        verbose_name="Объект ",
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        help_text="Выберите пользователя",
        verbose_name="Отдыхающий",
    )
    price = models.FloatField(help_text="Введите значение", verbose_name="Цена")
    dataeviction = models.DateTimeField(
        help_text="Введите значение", verbose_name="Дата выселения"
    )

    def __str__(self):
        return self.number


class Settlement(models.Model):
    dogovor = models.ForeignKey(
        "Dogovor",
        on_delete=models.CASCADE,
        help_text="Выберите договор",
        verbose_name="Договор ",
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        help_text="Выберите пользователя",
        verbose_name="Отдыхающий ",
    )
    rooms = models.ForeignKey(
        "Rooms",
        on_delete=models.CASCADE,
        help_text="Выберите комнату",
        verbose_name="Номер комнаты ",
    )


class Category(models.Model):
    name = models.CharField(
        max_length=30, help_text="Введите название", verbose_name="Название"
    )

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(
        max_length=30, help_text="Введите название", verbose_name="Название"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        help_text="Выберите категорию",
        verbose_name="Услуга ",
    )

    price = models.FloatField(help_text="Введите значение", verbose_name="Цена")
    images = models.ImageField(
        help_text="Выберите изображение", verbose_name="Изображение"
    )

    def __str__(self):
        return self.name


class Provide(models.Model):
    dataprovide = models.DateTimeField(
        help_text="Введите значение", verbose_name="Дата оказания услуги"
    )
    dogovor = models.ForeignKey(
        "Dogovor",
        on_delete=models.CASCADE,
        help_text="Выберите договор",
        verbose_name="Договор ",
    )
    service = models.ForeignKey(
        "Service",
        on_delete=models.CASCADE,
        help_text="Выберите услугу",
        verbose_name="Услуга ",
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        help_text="Выберите пользователя",
        verbose_name="Отдыхающий ",
    )
    dataprovide = models.DateTimeField(
        help_text="Введите значение", verbose_name="Дата оказания услуги"
    )
