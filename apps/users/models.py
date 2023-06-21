from django.contrib.auth.models import AbstractUser
from django.db import models
from conf.settings import AUTH_USER_MODEL

from apps.users.managers import UserManager



class UserPosition(models.TextChoices):
    USER = 'пользователь', 'Пользователь'
    MASTER = 'мастер', 'Мастер'
    OWNER = 'владелец', 'Владелец'


class UserGender(models.TextChoices):
    MALE = 'мужчина', 'Мужчина'
    FEMALE = 'женщина', 'Женщина'
    OTHER = 'другое', 'Другое'


class User(AbstractUser):
    """Пользователь"""
    phone = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=30, null=True, blank=True, unique=False)
    first_name = None
    last_name = None
    gender = models.CharField('Пол', max_length=50, default=UserGender.OTHER, choices=UserGender.choices)
    position = models.CharField('Позиция', max_length=50, default=UserPosition.USER, choices=UserPosition.choices)
    created_dt = models.DateTimeField('Дата и время создания юзера', auto_now_add=True)
    updated_dt = models.DateTimeField('Последние обновление объекта', auto_now=True)
    # avatar = models.ImageField(upload_to='users/avatars/', null=True, blank=True)
    USERNAME_FIELD = 'phone'
    objects = UserManager()

    class Meta:
            verbose_name = 'Пользователь'
            verbose_name_plural = 'Пользователи'

    def get_phone(self):
        return self.phone

    def get_gender(self):
        return self.get_gender_display()

    def get_position(self):
        return self.get_position_display()

    def get_created_dt(self):
        return self.created_dt

    def get_updated_dt(self):
        return self.updated_dt

    def __str__(self):
        return f'{self.username} {self.phone}'
    