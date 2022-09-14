from django.db import models

from .categories import CategoryProduct


def upload_to(instance, filename):
    return 'brands/images/%s/%s' % (instance, filename)


class BrandProduct(models.Model):
    """
    Бренд (производитель) товара
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name='Бренд',
        help_text='Наименование бренда',
    )
    photo = models.ImageField(
        upload_to=upload_to,
        verbose_name='Логотип бренда',
        help_text='Картинка, которая отображается на главном экране, при выборе бренда',
    )
    categories = models.ManyToManyField(
        CategoryProduct,
        verbose_name='Категории',
        help_text='Категории, с которыми работает данный бренд'
    )
    description = models.TextField(
        verbose_name='Описание бренда',
        help_text='Описание, которое отображается на странице бренда'
    )
    email = models.EmailField(verbose_name='Email', help_text='Email тех.поддержки бренда')
    show = models.BooleanField(
        default=True,
        verbose_name='Флаг показа бренда',
        help_text='Флаг, который позволяет регулировать отображение бренда на страницах',
    )

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ['name', ]

    def __str__(self):
        return self.name




