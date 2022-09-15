from django.urls import path

from .views import *

urlpatterns = [
    path('ajax_get_categories_for_brand/', ajax_get_categories_for_current_brand, name='ajax_get_categories_for_brand'),
]
