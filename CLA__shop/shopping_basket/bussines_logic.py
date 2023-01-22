from django.conf import settings
from django.core.mail import send_mail
from django.db import DatabaseError, transaction
from shop_products.models import PurchaseHistoryModel

from .models import Product, ShoppingBasketModel


def get_products_for_current_user_in_shopping_basket(user):
    """ Функция возвращает 'queryset' c товарами, которые находятся в корзине
        для заданного пользователя
        
    Args:
        user: объект, который описывает пользователя, для которого необходимо найти
              его товары из корзины

    Returns:
        0 - 'queryset' с объектами модели "shopping_basket"
        1 - 'queryset' с объектами модели "products"
    """
    query_shop_basket = ShoppingBasketModel.objects.filter(user=user.id)    
    query_products = Product.objects.filter(id__in=[obj.product.id for obj in query_shop_basket])
    return (query_shop_basket, query_products)
    

def set_single_time_for_lst_purchasehistorymodel(lst):
    """ Изменяет время создания объектов модели "PurchaseHistoryModel" во входном
        списке на последнее заданное

    Args:
        lst: Список в котором необходимо изменить время создание объектов

    Returns:
        Список с объектами, у которых поменяли время создания
    """
    for product in lst:
        product.datetime_purchase = lst[-1].datetime_purchase
    return lst   
    
    
def get_lst_with_objects_products_for_purchase_history(user):
    """ Функция позволяет получить список с объектами типа "PurchaseHistoryModel"
        для добавления купленных товаров в историю покупок

    Args:
        user: объект, который описывает пользователя 

    Returns:
        0 - сформированный список 
        1 - сообщение об ошибке, если оно имеется
    """
    # Сообщение об ошибки запроса
    message = None
    # Получаем 'queryset' с объектами из корзины, а также товарами, которые
    # находятся в корзине
    lst_products_in_basket, lst_products = get_products_for_current_user_in_shopping_basket(user)
    # Список для добавления товаров в "историю покупок"
    lst_for_purchase_history = []    
    # Перебираем список с корзины, а также формируем список с купленными товарами
    for product_in_bustket in lst_products_in_basket:
        # Вычисляем количество оставшегося данного товара
        left_prod_count = product_in_bustket.product.count-product_in_bustket.count
        if left_prod_count < 0:
            message += f'Вы ввели слишком большое количество товара "{product_in_bustket.product.name}". Введите другое значение (максимальное {product_in_bustket.count}).'
        else:  # Создаем объекты для добавления в историю покупок
            lst_for_purchase_history.append(
                PurchaseHistoryModel(
                    user=user, 
                    products=product_in_bustket.product,
                    count=product_in_bustket.count,
                )
            )
    # Изменяем время на одинаковое, так как продукты куплены в одно время
    lst_for_purchase_history = set_single_time_for_lst_purchasehistorymodel(lst_for_purchase_history)
    return (lst_for_purchase_history, message)


def create_email_message_at_buy_products(user):
    """ Функция создает сообщение, которое будет отправляться на почту при покупке
        товаров

    Args:
        user: Объект пользователя, который совершает покупку

    Returns:
        Строка, которая содержит сообщение о покупке
    """
    # Получаем список с товарами в корзине
    (products_in_busket, _) = get_products_for_current_user_in_shopping_basket(user)
    # Формируем сообщение для отправки на почту
    message_email = 'Вы купили: \n'
    for obj in products_in_busket:
        message_email += f'\t"{obj.product.name}" в количестве {obj.count} штук по цене {obj.product.price} р.\n'
    return message_email


def get_products_with_updated_quantity_after_purchase(user):
    """ Функция позволяет получить список с объектами типа "PurchaseHistoryModel"
        для добавления купленных товаров в историю покупок

    Args:
        user: объект, который описывает пользователя 

    Returns:
        0 - queryset с обновленным количеством товара
        1 - сообщение об ошибке, если оно имеется
    """
    message = None
    # Получаем список с товарами в корзине
    (products_in_busket, products) = get_products_for_current_user_in_shopping_basket(user)
    for product in products:
        # Вычисляем количество оставшегося данного товара
        left_prod_count = product.count - products_in_busket.get(product=product.id).count
        if left_prod_count < 0:
            message += f'Вы ввели слишком большое количество товара "{product.name}". Введите другое значение (максимальное {products_in_busket.get(product=product.id).count.count}).'
        else:  # Обновляем количество товара
            product .count = left_prod_count
    return (products, message)


def updating_tables_when_buying_products(user, lst_products_for_purchase_history):
    """ Функция обновления таблиц (с товарами, списком купленных товаров и корзиной)
        при покупке товаров

    Args:
        user: Объект с пользователем, который совершает покупку
        lst_products_for_purchase_history: Список, который содержит объекты для
            добавления их в таблицу со списком купленных товаров

    Returns:
        Сообщение об ошибки, если оно имеется
    """
    # Получаем список с товарами в корзине
    (products_in_busket, _) = get_products_for_current_user_in_shopping_basket(user)
    # Получаем queryset с обновленным количеством товаров после покупки
    (products, message) = get_products_with_updated_quantity_after_purchase(user)
    
    if not message or len(message) == 0:
        try:
            with transaction.atomic():
                # Добавляем список купленных товаров
                PurchaseHistoryModel.objects.bulk_create(lst_products_for_purchase_history)
                # Обновляем количество товаров в таблице с товарами
                [product.save() for product in products]
                # Удаляем купленные товары из корзины
                products_in_busket.delete()
        except DatabaseError:
            message = 'Возникла ошибка, пожалуйста попробуйте позже'

    return message


def send_email_message_after_purchase(message_email, user):
    """ Функция отправляет сообщение о покупке товаров на почту покупателя

    Args:
        message_email: Текст сообщения
        user: Объект с пользователем, которому необходимо отправить письмо

    Returns:
        Сообщение об ошибки, если оно имеется
    """
    message = None
    # Отправить сообщение о покупке на почту      
    result = send_mail(
            subject='Покупка товаров',
            message=message_email,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email,]
        )
    if result < 1:
        message = 'При отправки сообщения на почту о покупке товаров произошла ошибка'
    return message


def buy_products(user):
    """ Функция имитирует покупку в магазине

    Args:
        user: Объект, который описывает пользователя сайта

    Returns:
        Сообщение об ошибки, если оно имеется
    """
    # Получаем список с объектами, которые добавятся в таблицу с историей покупок
    (lst_for_purchase_history, message) = get_lst_with_objects_products_for_purchase_history(user)
    # Если нет ошибок, то обрабатываем дальше
    if not message or len(message) == 0:
        # Формирование сообщений для отправки на почту
        message_email = create_email_message_at_buy_products(user)
        # обновляем таблицы, после покупки товаров
        message = updating_tables_when_buying_products(
            user, 
            lst_for_purchase_history,
        )
    # Отправляем сообщение о покупке товаров на почту
    if not message or len(message) == 0:
        message = send_email_message_after_purchase(message_email, user)
    return message
