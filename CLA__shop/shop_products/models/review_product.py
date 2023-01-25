from django.conf import settings
from django.db import models

from .products import Product


class CommentProductReviewModel(models.Model):
    content = models.TextField(verbose_name='Текст комментария')
    f_delete = models.BooleanField(
        default=False, 
        verbose_name='Флаг удаления комментрия админом',
    )
    created = models.DateTimeField(
        verbose_name='Время создания комментария',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Время последнего изменения комментария',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'Комментарий к товару'
        verbose_name_plural = 'Комментарии к товару'
    

class ReviewProductModel(models.Model):
    
    class GradeChoices(models.IntegerChoices):
        one =   (1, ('1'))
        two =   (2, ('2'))
        three = (3, ('3'))
        four =  (4, ('4'))
        five =  (5, ('5'))
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name='Товар',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        db_index=True,
        verbose_name='Пользователь, который оставляет отзыв',
    )
    grade = models.SmallIntegerField(
        verbose_name='Оценка товара',
        choices=GradeChoices.choices
    )
    comment = models.OneToOneField(
        CommentProductReviewModel,
        on_delete=models.CASCADE,
        verbose_name='Отзыв',
    )

    class Meta:
        verbose_name = 'Отзыв к купленному товару'
        verbose_name_plural = 'Отзывы к купленному товару'
