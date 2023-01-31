import inspect
import types

from importlib import import_module
from random import sample

import django.db.models

from django.core.cache import cache

from .models import BrandProduct, CategoryProduct, Product, ReviewProductModel


def get_func_str_code_all_models_one_module(lst_models: list) -> str:
    """
    Функция получения исходного кода дандер метода "__str__", чтобы определить к какой категории относятся данные
    расширенные настройки.

    P.S.: В каждой модели должен (по договоренности) присутствовать перегруженный дандер метод, который имеют
    следующий шаблон: "'Блок с характеристиками' для продукта {self.product} категории 'Название категориии'".
    Пример: f'Общие параметры для продукта {self.product} категории "Корпуса"'.

    :param lst_models: список с объектами классов моделей
    :return: Исходный код дандер-метода __str__ одной из модели
    """

    func_code = ''
    for name_model, obj_model in lst_models:
        if '__str__' in obj_model.__dict__.keys():
            func_code = inspect.getsource(obj_model.__dict__['__str__'])
            break
    return func_code


def create_name_id_for_fieldset(name_category: str) -> str:
    """
    Формирует ID-объекта html, который содержит в себе форму для заполнения расширенных характеристик

    :param name_category - название категории
    :return Возвращает название id-объекта html
    """
    return f'{name_category}-group'


def match_category_and_specifications(all_categories: django.db.models.QuerySet, func_code: str, lst_models: list) -> dict:
    """
    Функция сопоставления категории и модуля.

    :param all_categories: QuerySet с категориями
    :param func_code: исходный код дандер-метода для определения категории
    :param lst_models: Список с объектами классов, которые находятся в текущем модуле
    :return: Возвращает словарь, который в key = ID-категории, data = Массив с ID объектами формы для текущей категории
    """
    # Выходной словарь
    output_dict = {}
    # Перебираем категории и сопоставляем их с исходным кодом
    for category in all_categories:
        if category.name in func_code:  # Наши нужную категорию
            # Перебираем все модели и добавляем их в словарь
            output_dict[category.id] = [create_name_id_for_fieldset(n.lower()) for n, o in lst_models]
            # Так как одна категория = один файл с расширенными параметрами, то заканчиваем после одного файла
            break
    return output_dict


def create_dict_match_category_and_specification_one_module(obj_module: types.ModuleType) -> dict:
    """
    Функция формирует словарь, который сопоставляет категории и id-элементов html страницы. Чтобы отображать необходимые
    формы при добавлении элемента для одной категории.

    :return Возвращает словарь, который в key = ID-категории, data = Массив с ID объектами формы для текущей категории
    """
    # Получаем весь список категорий через кэщ
    all_categories = cache.get('all_categories')
    if not all_categories:
        all_categories = CategoryProduct.objects.all()
        cache.set('all_categories', all_categories, 60)
    # Получаем все модели в данной модуле
    lst_models = inspect.getmembers(obj_module, inspect.isclass)
    # Получаем исходный код для поиска категории
    func_code = get_func_str_code_all_models_one_module(lst_models)
    # Сопоставляем название категории и модуля
    output_dict = match_category_and_specifications(all_categories, func_code, lst_models)
    return output_dict


def create_dict_match_category_and_specification() -> dict:
    """
    Функция формирует словарь, который сопоставляет категории и id-элементов html страницы. Чтобы отображать необходимые
    формы при добавлении элемента.

    :return Возвращает словарь, который в key = ID-категории, data = Массив с ID объектами формы для текущей категории
    """
    # Выходной словарь
    output_dict = {}
    # Модуль с расширенными характеристиками для товаров
    module_specification = 'shop_products.models.specifications'
    # Получаем все модули с расширенными параметрами
    lst_modules = inspect.getmembers(import_module(module_specification), inspect.ismodule)
    # Получаем ID объектов для каждой категории (модуля) по очереди
    for name_module, obj_module in lst_modules:
        dict_category = create_dict_match_category_and_specification_one_module(obj_module)
        output_dict.update(dict_category)
    return output_dict


def get_list_specifications_for_category(name_category: str):
    """
    Функция возвращает список с названиями моделей, которые описывают расширенные параметры
    
    :param name_category - название категории
    """
    # Словарь, который содержит списки с моделями для каждой категории
    dict_with_spec = {
        # Название категории: [Список моделей с расширенными моделями]
        "Блок питания": [
            'factorydatapowersupplyspecifications',
            'commonparameterspowersupplyspecifications',
            'appearancepowersupplyspecifications',
            'cablesconnectorspowersupplyspecifications',
            'electricalparameterspowersupplyspecifications',
            'coolingsystempowersupplyspecifications',
            'certificationpowersupplyspecifications',
            'dimensionsweightpowersupplyspecifications',
            ],
        "Видеокарта": [
            'factorydatavideocartspecifications',
            'commonparametersvideocartspecifications',
            'mainparametersvideocartspecifications',
            'videomemoryvideocartspecifications',
            'videoprocessorvideocartspecifications',
            'outputimagevideocartspecifications',
            'connectionvideocartspecifications',
            'coolingsystemvideocartspecifications',
            'dimensionsandwightvideocartspecifications',
            ],
        "Жесткий диск": [
            'factorydatahddspecifications',
            'commonparametershddspecifications',
            'storagedevicehddspecifications',
            'mechanicsreliabilityhddspecifications',
            'dimensionshddspecifications',
            ],
        "Корпус": [
            'factorydatacomputercasespecifications',
            'commonparameterscomputercasespecifications',
            'formfactorcomputercasespecifications',
            'appearancecomputercasespecifications',
            'compatibilitycomputercasespecifications',
            'coolingcomputercasespecifications',
            'frontpanelconnectorscomputercasespecifications',
            'servicecomputercasespecifications',
            ],
        "Кулер": [
            'factorydatacoolerspecifications',
            'commonparameterscoolerspecifications',
            'radiatorcoolerspecifications',
            'fancoolerspecifications',
            'dimensionscoolerspecifications',
            ],
        "Материнская плата": [
            'factorydatamotherboardspecifications',
            'commonparametersmotherboardspecifications',
            'formfactordimensionsmotherboardspecifications',
            'processorchipsetmotherboardspecifications',
            'memorymotherboardspecifications',
            'storagecontrollersmotherboardspecifications',
            'expansionslotsmotherboardspecifications',
            'backpanelmotherboardspecifications',
            'internalconnectorsmotherboardspecifications',
            'audiomotherboardspecifications',
            'netmotherboardspecifications',
            'coolingpowermotherboardspecifications',
            ],
        "Оперативная память": [
            'factorydataramspecifications',
            'commonparametersramspecifications',
            'compositionramspecifications',
            'performanceramspecifications',
            'timingsramspecifications',
            'designramspecifications',
            ],
        "Процессор": [
            'factorydataprocessorspecifications',
            'commonparametersprocessorspecifications',
            'corearchitectureprocessorspecifications',
            'frequencyoverclockingprocessorspecifications',
            'ramoptionsprocessorspecifications',
            'thermalcharacteristicsprocessorspecifications',
            'graphicscoreprocessorspecifications',
            'buscontrollersprocessorspecifications',
            ],
        "ССД": [
            'factorydatasolidstatedrivespecifications',
            'commonparameterssolidstatedrivespecifications',
            'maincharacteristicssolidstatedrivespecifications',
            'driveconfigurationsolidstatedrivespecifications',
            'performanceindicatorssolidstatedrivespecifications',
            'reliabilitysolidstatedrivespecifications',
            'dimensionssolidstatedrivespecifications',
            ],
    }
    return dict_with_spec[name_category]


def get_all_name_categories():
    """
    Функция получения списка пар (id, имя) для выбора категории
    :return: возвращает список с парами (id, имя) для всех доступных категорий
    """

    all_category = CategoryProduct.objects.all()
    return [tuple([category.pk, category.name]) for category in all_category]


def get_all_name_brands():
    """
    Функция получения списка пар (id, имя) для выбора бренда
    :return: возвращает список с парами (id, имя) для всех доступных брендов
    """

    all_brands = BrandProduct.objects.all()
    return [tuple([brand.pk, brand.name]) for brand in all_brands]


def get_review_object(user, product):
    """ Функция получения объекта с отзывом из БД для заданного товара от опред.
        покупателя

    Args:
        user:  Покупатель, который оставлял отзыв
        product: Товар, на который оставляли отзыв

    Returns:
        объект с отзывом из БД
    """
    return ReviewProductModel.objects.get(user=user.id, product=product.id)


def get_random_products(count=5):
    """ Методо поулчения queryset со случайными товарами 

    Args:
        count: Количество товаров, которое необходимо получить. По умолчанию 5.
    """
    all_products = Product.objects.all()
    return all_products.filter(id__in=sample(range(0, len(all_products)), count))
