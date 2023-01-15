from .models import BrandProduct


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
        