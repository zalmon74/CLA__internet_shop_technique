from django.urls import path
from django.views.decorators.cache import never_cache

from .views import *

urlpatterns = [
    path('<int:pk>/give_review/',
         never_cache(GiveReviewForProduct.as_view()),
         name='give_review_for_product'),
    path('<int:pk>/edit_review/',
         never_cache(EditReviewForProduct.as_view()),
         name='edit_review'),
    path('ajax_get_categories_for_brand/', ajax_get_categories_for_current_brand, name='ajax_get_categories_for_brand'),
    path(
        'ajax_get_el_specifications/',
        ajax_get_categories_with_id_elements_specifications,
        name='ajax_get_el_specifications'),
    path(
        'ajax_add_favorite_product/',
        never_cache(ajax_add_favorite_product),
        name='ajax_add_favorite_product'),
    path('<int:pk>/', ProductsDetailView.as_view(), name='product_detail'),
    path('', ProductsListView.as_view(), name='product_list'),
]
