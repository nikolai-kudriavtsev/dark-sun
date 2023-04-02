import os
import datetime

from django.db import models
from socialbooking.authentication.models import User
from socialbooking.geo.models import City, Coordinates, Region, Address


class Stay(models.Model):

    class Meta:
        verbose_name = 'Социальный объект'
        verbose_name_plural = 'Социальные объекты'

    TYPE_CHOICES = [
        ('sanatoriy', 'Санаторий'),
        ('campsite', 'Лагерь'),
        ('recreation_place', 'Дом отдыха'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=256, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    coordinates = models.OneToOneField(Coordinates, on_delete=models.CASCADE)
    phone = models.CharField(max_length=9)

    photos = models.ManyToManyField('Photo')

    def __str__(self):
        return f"{self.place_name}"

class Suite(models.Model):

    class Meta:
        verbose_name = 'Позиция пребывния'
        verbose_name_plural = 'Позиции пребывния'
    
    stay = models.ForeignKey(Stay, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photos = models.ManyToManyField('Photo')
    

    def __str__(self):
        return f"{self.name} в {self.stay}"

class AvailabilityCalendar(models.Model):

    class Meta:
        verbose_name = 'Календарь бронирования'
        verbose_name_plural = 'Календари бронирования'

    suite = models.OneToOneField(Suite, on_delete=models.CASCADE)

    @property
    def dates(self):
        return self.date_set.filter(check_in__gte=datetime.date.today())

class BookingInterval(models.Model):

    class Meta:
        verbose_name = 'Интервал пребывания'
        verbose_name_plural = 'Интервалы пребывания'

    calendar = models.ForeignKey(AvailabilityCalendar, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    duration = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField()

class Booking(models.Model):

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    suite = models.ForeignKey(Suite, on_delete=models.CASCADE)
    dates = models.ManyToManyField(BookingInterval)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    confirmed = models.BooleanField(default=False)

class Payment(models.Model):

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)

# Create your models here.
class Type(models.Model):
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
    databirth = models.DateField(
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
        Region,
        on_delete=models.CASCADE,
        help_text="Выберите регион",
        verbose_name="Регион объекта ",
    )
    city = models.ForeignKey(
        City,
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
        User,
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
        User,
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

def get_upload_path(instance, filename):
    return os.path.join(f'{instance.owner.slug}', 'photos', filename)

class Photo(models.Model):

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    owner = models.ForeignKey(Stay, on_delete=models.CASCADE)
    alt = models.CharField(
        max_length=32,
        blank=True,
        verbose_name='Альтернативный текст',
        help_text='Введите альтернативный текст',
        )
    image = models.ImageField(upload_to=get_upload_path)
