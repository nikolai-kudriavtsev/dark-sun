from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
import uuid

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser should have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser should have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    USERNAME_FIELD = 'email'
    
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    patronymic = models.CharField(max_length=64)
    date_of_birth = models.DateField(null=True, blank=True)

    phone_number = models.CharField(max_length=16, null=True, blank=True)

    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)

    @property
    def full_name(self):
        return self.first_name+' '+self.last_name

    @property
    def fio(self):
        return ' '.join([self.last_name, self.first_name, self.patronymic])
    
    def __str__(self):
        return f'Пользователь {self.email}'