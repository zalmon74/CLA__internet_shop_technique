from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractUser

from django.db import models

from .managers import CustomUserManager
from .validators import *

from shop_products.models import Product, BrandProduct


class CustomUser(AbstractUser):
    """
    Перегруженная модель пользователей
    """
    username = models.CharField(
        max_length=50,
        validators=[validation_username, ],
        unique=True,
        db_index=True,
        verbose_name='Логин пользователя',
        help_text='Логин может иметь максимум 50 символов и содержать только буквы и цифры.',
        error_messages={
            'unique': 'Пользователь с таким логином, уже существует',
        }
    )
    email = models.EmailField(unique=True, db_index=True, verbose_name='Email')
    first_name = models.CharField(
        max_length=50,
        validators=[validation_first_last_name, ],
        verbose_name='Имя',
        help_text='Имя пользователя может иметь максимум 50 символов и содержать только русские буквы'
    )
    last_name = models.CharField(
        max_length=50,
        validators=[validation_first_last_name, ],
        verbose_name='Фамилия',
        help_text='Фамилия пользователя может иметь максимум 50 символов и содержать только русские буквы'
    )
    favorite_products = models.ManyToManyField(Product, verbose_name='Любимые товары')
    favorite_brands = models.ManyToManyField(BrandProduct, verbose_name='Любимые производители (бренды)')

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['password', 'email', 'first_name', 'last_name', ]

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
