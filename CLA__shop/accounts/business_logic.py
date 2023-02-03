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
