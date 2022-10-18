from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductsListView.as_view(), name='product_list'),
    path('ajax_get_categories_for_brand/', ajax_get_categories_for_current_brand, name='ajax_get_categories_for_brand'),
    path(
        'ajax_get_el_specifications/',
        ajax_get_categories_with_id_elements_specifications,
        name='ajax_get_el_specifications'),

]
