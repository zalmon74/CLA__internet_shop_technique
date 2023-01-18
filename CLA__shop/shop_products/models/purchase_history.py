from django.conf import settings
from django.db import models
from shop_products.models import Product


class PurchaseHistoryModel(models.Model):
    """ Модель, которая хранит историю покупок пользователей
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        db_index=True,
        verbose_name='Пользователь',
    )
    products = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        verbose_name='Купленные товары'
    )
    datetime_purchase = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата и время покупки'
    )
    count = models.PositiveSmallIntegerField(verbose_name='Количество купленного товара')
    
    class Meta:
        verbose_name = 'История покупок'
        verbose_name_plural = 'История покупок'
        unique_together = (('user', 'products', 'datetime_purchase'),)
        ordering = ['user', 'datetime_purchase', ]
