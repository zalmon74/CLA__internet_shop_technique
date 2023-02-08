import os
import sys

from shutil import copy
from string import ascii_letters

import django

from settings import *

sys.path.append('/home/konstantin/Dropbox/Python_Lerning/Django/CLA__internet_shop_technique/CLA__shop')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

django.setup()

from admin_tools_stats.models import (
    DashboardStats, DashboardStatsCriteria, chart_types, operation,
    time_scales,
)
from django.db import IntegrityError
from shop_products.models import BrandProduct, CategoryProduct


def create_dict_for_json_brands():
    """ Функция создает словарь для JSON с названиями брендов
    """
    dict_for_json = {None: [None, 'Все'],}
    all_brands = BrandProduct.objects.all()
    for brand in all_brands:
        dict_for_json[str(brand.pk)] = [str(brand.pk), brand.name]
    return dict_for_json


def create_dict_for_json_categories():
    """ Функция создает словарь для JSON с названиями категорий
    """
    dict_for_json = {None: [None, 'Все'],}
    all_categories = CategoryProduct.objects.all()
    for category in all_categories:
        dict_for_json[str(category.pk)] = [str(category.pk), category.name]
    return dict_for_json
    

def get_or_create_filters():
    """ Функция создает объекты "DashboardStatsCriteria" и записывает их в БД
    """  
    try:
        brand_filter = DashboardStatsCriteria.objects.get(criteria_name='filter_brand')
    except DashboardStatsCriteria.DoesNotExist:
        brand_filter = DashboardStatsCriteria(
        criteria_name='filter_brand',
        dynamic_criteria_field_name='products__brand',
        criteria_dynamic_mapping=create_dict_for_json_brands()
        )
        brand_filter.save()
    try:
        categories_filter = DashboardStatsCriteria.objects.get(criteria_name='filter_categories')
    except DashboardStatsCriteria.DoesNotExist:
        categories_filter = DashboardStatsCriteria(
            criteria_name='filter_categories',
            dynamic_criteria_field_name='products__category',
            criteria_dynamic_mapping=create_dict_for_json_categories()
        )
        categories_filter.save()
    return brand_filter, categories_filter

def create_charts():
    """ Функция создает объекты типа "DashboardStats" и записывает их в БД
    """
    # Фильтры для графиков
    filters = get_or_create_filters()
    # График с количеством проданных товаров
    try:
        chart_count_sell_products = DashboardStats.objects.get(graph_key='count_sell_products')
    except DashboardStats.DoesNotExist:
        chart_count_sell_products=DashboardStats(
            graph_key='count_sell_products',
            graph_title='Количество проданных товаров',
            model_app_name='shop_products',
            model_name='PurchaseHistoryModel',
            date_field_name='datetime_purchase',
            operation_field_name='count',
            type_operation_field_name=list(zip(*operation))[0][1],
            is_visible=True,
            default_chart_type=list(zip(*chart_types))[0][1],
            allowed_chart_types=list(zip(*chart_types))[0][:2],
            allowed_time_scales=list(zip(*time_scales))[0][1:],
            allowed_type_operation_field_name = list(zip(*operation))[0][1]
        )
        chart_count_sell_products.save()
    # Проверяем, что нужные фильтры имеются
    for filter in filters:
        if not filter in chart_count_sell_products.criteria.all():
            chart_count_sell_products.criteria.add(filter)
    
    # График суммой 
    
    
    

create_charts()


