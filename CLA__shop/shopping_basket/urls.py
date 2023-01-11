from django.urls import path
from django.views.decorators.cache import never_cache

from .views import ShopingBasketView, add_product_in_shopping_basket

urlpatterns = [
    path(
        'add_product_in_shopping_basket/', 
        never_cache(add_product_in_shopping_basket), 
        name='add_product_in_shopping_basket'
    ),
    path('', never_cache(ShopingBasketView.as_view()), name='shopping_basket'),
]
