from django.urls import path
from django.views.decorators.cache import never_cache

from .views import *

urlpatterns = [
    path('ajax_add_product_in_shopping_bassket/',
         never_cache(ajax_add_product_in_shopping_bassket),
         name='ajax_add_product_in_shopping_bassket'),
    path('ajax_delete_product_from_shopping_bassket/',
         never_cache(ajax_delete_product_from_shopping_bassket),
         name='ajax_delete_product_from_shopping_bassket'),
    path('ajax_update_count_product_from_shopping_bassket/',
         never_cache(ajax_update_count_product_from_shopping_bassket),
         name='ajax_update_count_product_from_shopping_bassket'),
    path('ajax_buy_products_from_shopping_bassket/',
         never_cache(ajax_buy_products_from_shopping_bassket),
         name='ajax_buy_products_from_shopping_bassket'),
    path('', never_cache(ShopingBasketView.as_view()), name='shopping_basket'),
]
