from django import template
from django.db.models import Model
from django.http import QueryDict
from shop_products.business_logic import get_list_specifications_for_category
from shop_products.models import CategoryProduct

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


@register.simple_tag
def get_dict_with_specifications_parameters_for_product(product: Model):
    """ Тег позволяет получить словарь с расширенными характеристиками для
    заданного товара

    :param product: объект с товаром, для которого необходимо получить
        рассширенные параметры
        
    :return output: список, который содержит словари с раширенными параметрами
    """
    # Определяем модели с расширенными параметрами
    specifications = get_list_specifications_for_category(product.category.name)
    output = []
    # Перебираем все модели с раширенными параметрами
    for cur_spec in specifications:
        output_dict = {}
        output_dict[getattr(product, cur_spec)._meta.verbose_name+' '] = None
        for name_field in getattr(product, cur_spec)._meta.fields:
            value = getattr(getattr(product, cur_spec), name_field.name)
            if isinstance(value, bool):
                    value = 'Да' if value else 'Нет'
            output_dict[name_field.verbose_name] = value
        # Убираем из словаря ID и товар, так как это служебные данные
        del output_dict['ID']
        del output_dict['Товар']
        output.append(output_dict)
    return output
