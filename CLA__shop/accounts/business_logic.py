import random

from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail

from .models import BrandProduct, Product


def get_queryset_brandproduct_exclude_favite_for_user(user):
    """ Метод возвращает список записями (queryset) с производителями (брендами),
        которые не находятся в избранном для заданного пользователя

    Args:
        user : пользователь, для которого необходиом получить список
    """
    # Queryset избранных брендов
    user_favorite_brands_quryset = user.favorite_brands.all()
    # Список с ИД избранных брендов
    user_favorite_brands_id_list = [brand.id for brand in user_favorite_brands_quryset]
    return BrandProduct.objects.exclude(id__in=user_favorite_brands_id_list)
        
def get_product_category_photo(all_products):
    """ Функция формирует список с кортежами типа (товар, категория_товара, фото_товара)

    Args:
        all_products: QuerySet - с товарами, для которых необходимо сформировать кортеж
    """
    # Получаем список категорий для каждого товара
    categories = all_products.select_related('category')
    categories_for_products = [obj.category for obj in categories]
    # Получаем список с url-фото для товара соответствующего товара
    all_products = all_products.prefetch_related('photoproduct_set')
    photo_for_products = [obj.photoproduct_set.all()[0].photo.url for obj in all_products]
    return [(all_products[ind], categories_for_products[ind], photo_for_products[ind]) for ind in range(len(all_products))]


def get_product_category_photo_count_datepurchase(purchase_history):
    """ Функция формирует список с кортежами типа (товар, категория_товара, фото_товара, кол-во_товара, дата_покупки)
        для купленных товаров
        
    Args:
        purchase_history: QuerySet - с товарами, для которых необходимо сформировать кортеж
    """
    # Получаем список продуктов
    purchase_history = purchase_history.select_related('products')
    lst_purchase_history_id_products = [obj.products.id for obj in purchase_history]
    all_products  = Product.objects.filter(id__in=lst_purchase_history_id_products)
    # Получаем категорию для каждого товара
    categories = all_products.select_related('category')
    categories_for_products = [obj.category.name for obj in categories]
    # Получаем фото для каждого товара
    all_products = all_products.prefetch_related('photoproduct_set')
    photo_for_products = [obj.photoproduct_set.all()[0].photo.url for obj in all_products]
    return [(all_products[ind], categories_for_products[ind], photo_for_products[ind], purchase_history[ind].count, purchase_history[ind].datetime_purchase) 
            for ind in range(len(all_products))]
    

def get_review_product_comment(review_products):
    """ Функция формирует список с кортежами типа (отзыв, товар, комментарий)
        для оставленных отзывов пользователя
        
    Args:
        review_products: QuerySet - с оставленными отзывами для текущего покупателя
    """
    review_products_s = review_products.select_related('product')
    products = [obj.product for obj in review_products_s]
    review_products_s = review_products.select_related('comment')
    comments = [obj.comment for obj in review_products_s]
    return [(review_products[ind], products[ind], comments[ind]) for ind in range(len(review_products))]


def generate_code_for_confirm_email(count_symbols=settings.COUNT_SYMBOLS_FOR_CONFIRM_EMAIL):
    """ Функция генерации символов для подтверждения email
    
    Args:
        count_symbols: Количество генерируемых символов
    """    
    return ''.join([str(random.randint(0, 10)) for _ in range(count_symbols)])


def generate_key_name_for_code_confirm_email_for_user(user):
    """ Функция генерирует имя ключа для записи кода подтверждения email в КЭШ

    Args:
        user: Объект пользователя, для которого сгенерирован ключ
    """
    return f'{user}_{user.email}_code'


def generate_key_name_for_time_code_confirm_email_for_user(user):
    """ Функция генерирует имя ключа для записи в КЭШ булевое значение, которое
        будет сигнализировать запрет на отправку повторного сообщения

    Args:
        user: Объект пользователя, для которого сгенерирован ключ
    """
    return f'{user}_{user.email}_code_time'


def get_or_set_confirm_email_from_cache(user):
    """ Функция получает код для подтверждения почты из КЭШа, если он отсутствует,
        то генерирует и добавляет его в КЭШ
        
    Args:
        user: Пользователь, для которого необходим код подтверждения
    """
    # Проверяем наличие кода для данного пользователя в кэше, если нет,
    # то генерируем его и добавляем в кэш
    key_code = generate_key_name_for_code_confirm_email_for_user(user)
    code = cache.get(key_code)
    if not code:
        code = generate_code_for_confirm_email()
        cache.set(key_code, code, settings.TIME_VALID_CODE_CONFIRM_EMAIL)
    return code
    

def send_email_message_for_confirm_email(user):
    """ Функция отправляет сообщение на почту пользователя с кодом для
        ее подтверждения

    Args:
        user: Пользователь, для котрого необходимо подтвердить почту
    """
    # Проверяем, что повторное сообщение уже можно отправлять
    if not cache.get(generate_key_name_for_time_code_confirm_email_for_user(user)):
        # Получаем код для подтверждения почты
        code = get_or_set_confirm_email_from_cache(user)
        # Отправляем сообщение на почту
        result = send_mail(
            subject='Подтверждение почты на сайте cla_shop',
            message=f'Код для подтверждения: {code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email,],
        )
        # Устанавливаем запрет на отправку повтроного сообщения
        cache.set(generate_key_name_for_time_code_confirm_email_for_user(user), True, settings.TIME_REPEAT_SEND_CODE_CONFIRM_EMAIL)
       

def create_message_on_confirm_email(email):
    """ Фукция создает сообщение об отправки сообщения с кодом на почту для ее 
        подтверждения

    Args:
        email: Почта, для которой необходимо подтверждение
    """
    return f'На почту {email} отправлен код для подтверждения почты (сообщения можно отпровлять только раз в {settings.TIME_REPEAT_SEND_CODE_CONFIRM_EMAIL} сек.)'


def check_confirm_code(user, user_code):
    """ Функция проверяем правильность введенного кода подтверждения с кодом
        отправленным на почту

    Args:
        user: Объект с пользователем, для которого производится проверка
    """
    return cache.get(generate_key_name_for_code_confirm_email_for_user(user)) == user_code


def send_message_at_change_email(new_email):
    """ Функция отправляет сообщение о смене почты (сообщение отправляется на 
        новую почту для проверки ее существования)
        
    Args:
        new_email: email, на который необходимо отправить сообщение
    """
    send_mail(
            subject='Изменение почты на сайте cla_shop',
            message=f'Поздравляю с успешным изменением почты',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_email,],
    )
    