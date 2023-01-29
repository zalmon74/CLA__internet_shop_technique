from accounts.models import CustomUser
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Product


@receiver(post_save, sender=Product)
def post_save_product(*args, **kwargs):
    """ Сигнал для отправки сообщений на почту об изменении товаров
    """
    instance = kwargs['instance']
    f_created = kwargs['created']
    if f_created:  
        # Оповещаем покупателей о добавлении нового товара с избранным брендом
        user_with_favorite = CustomUser.objects.filter(favorite_brands=instance.brand)
        send_mail(
            subject=f'Новый товар в магазине от бренда "{instance.brand}"',
            message=f'Появился новый товар "{instance}" от бренда "{instance.brand}"',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email for user in user_with_favorite]
        )
    else:
        # Оповещаем покупателей о малом количестве избранного товара
        if instance.count < 6:
            user_with_favorite = CustomUser.objects.filter(favorite_products=instance)
            send_mail(
            subject=f'Осталось малое количество товара "{instance}"',
            message=f'"{instance}" осталось {instance.count} штук',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email for user in user_with_favorite]
        )
