from django.db import models

from .brands import BrandProduct
from .categories import CategoryProduct


class Product(models.Model):
    """
    Товар
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name='Наименование товара',
    )
    price = models.IntegerField(
        default=0,
        verbose_name='Цена товара',
        help_text='Цена товара, по умолчанию 0',
    )
    count = models.IntegerField(
        default=0,
        verbose_name='Количество',
        help_text='Количество товаров на складе (сколько можно продать товаров)',
    )
    brand = models.ForeignKey(
        BrandProduct,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name='Бренд',
    )
    category = models.ForeignKey(
        CategoryProduct,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name='Категория',
    )
    description = models.TextField(
        verbose_name='Описание товара'
    )
    show = models.BooleanField(
        default=True,
        verbose_name='Флаг показа товара',
        help_text='Флаг, который позволяет регулировать отображение товара на страницах',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', ]

    def __str__(self):
        return self.name

    def get_photos (self):
        """ Метод получения фото для заданного товара
        """
        return self.photoproduct_set.all()

def upload_to(instance, filename):
    return 'products/images/%s/%s' % (instance.product.name, filename)


class PhotoProduct(models.Model):
    """
    Фото товаров
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to=upload_to,
        verbose_name='Фотографии товара',
    )
