from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from shop_products.validators import validate_category_name


class ContactFormModel(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[validate_category_name],
        verbose_name='Имя',
    )
    email = models.EmailField(verbose_name='Email')
    phone_number = PhoneNumberField(verbose_name='Номер телефона', blank=False, null=False)
    message = models.TextField(verbose_name='Сообщение')
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата сообщения')

    def __str__(self):
        return f'{self.name} {self.email} {self.phone_number}'

    class Meta:
        verbose_name = 'Данные с формы "Связаться с нами"'
        verbose_name_plural = 'Данные с формы "Связаться с нами"'

