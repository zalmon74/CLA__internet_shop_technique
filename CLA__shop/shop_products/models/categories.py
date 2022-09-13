from django.db import models

from shop_products.validators import validate_category_name


class CategoryProduct(models.Model):
    """
    Категория товара
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        validators=[validate_category_name],
        verbose_name='Категория',
        help_text='Название категории товара',
    )
    photo = models.ImageField(
        upload_to=f'categories/images/{name}/',
        verbose_name='Фото категории',
        help_text='Картинка, которая отображается на главном экране, при выборе категории',
    )

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        ordering = ['name', ]

    def __str__(self):
        return self.name

