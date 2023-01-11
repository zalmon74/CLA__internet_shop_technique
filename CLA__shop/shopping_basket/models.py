from accounts.models import CustomUser
from django.db import models
from shop_products.models import Product

# class ProductForBasket(models.Model):
#     user = models.OneToOneField(
#         CustomUser, 
#         on_delete=models.CASCADE, 
#         db_index=True,
#         primary_key=True,
#         verbose_name='Пользователь'
#     )
#     product = models.OneToOneField(
#         Product,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         verbose_name='Товар, который находится в корзине'
#     )
#     count = models.PositiveSmallIntegerField(verbose_name='Количество товара')

#     def __str__(self):
#         return f'{self.product.__str__()} - {self.count}'
    
#     class Meta:
#         verbose_name = 'Товар в корзине'
#         verbose_name_plural = 'Товар в корзине'
        

class ShoppingBasketModel(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        db_index=True,
        verbose_name='Пользователь'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар, который находится в корзине'
    )
    count = models.PositiveSmallIntegerField(verbose_name='Количество товара')
    
    def __str__(self):
        return f'{self.user.__str__()} | {self.product.__str__()} | {self.count}'
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Козрина'
        unique_together = (('user', 'product'),)
        ordering = ['user', 'product' ]
