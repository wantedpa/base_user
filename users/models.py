from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    city = models.CharField(
        verbose_name='Город',
        max_length=50,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'