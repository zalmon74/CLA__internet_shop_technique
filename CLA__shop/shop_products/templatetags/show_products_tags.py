from django import template
from django.http import QueryDict

register = template.Library()


@register.filter
def getlist(dictionary: QueryDict, key: object):
    """
    Фильтр для получения списка параметров из "QueryDict"

    :param dictionary: словарь типа "QueryDict"
    :param key: ключ, по которому необходимо получить список параметров
    :return: список параметров для соответствующего ключа
    """
    return dictionary.getlist(key)


@register.simple_tag
def create_get_parameters_for_url_products(page: int, brands: list, categories: list):
    """
    Тэг возвращает строку с GET-параметрами для URL с соответствующими параметрами

    :param page: Необходимая страница
    :param brands: Список фильтрации товаров по бренду
    :param categories: Список фильтрации товаров по категориям
    :return: Строка с GET-параметрами
    """
    output = '?'
    # Добавляем номер страницы
    output += f'page={page}'
    # Добавляем фильтрацию по бренду
    for brand in brands:
        output += f'&brands={brand}'
    # Добавляем фильтрацию по категориям
    for category in categories:
        output += f'&categories={category}'
    return output

