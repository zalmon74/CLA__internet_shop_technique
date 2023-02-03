from django.db.models import QuerySet
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import redirect
from django.views.generic import ListView

from .bussines_logic import *
from .models import Product, ShoppingBasketModel


def ajax_add_product_in_shopping_bassket(request):
    """ Вьюшка, которая обрабатывает ajax-запрос на добавление товара в корзину
    """
    product_id = int(request.GET['product_url_detail'].split('/')[-2])
    # Добавляем товар в корзину к пользователю
    ShoppingBasketModel.objects.update_or_create(
        user=request.user,
        product=Product.objects.get(id=product_id),
        count=1,
    )
    return HttpResponse()


def ajax_delete_product_from_shopping_bassket(request):
    """ Вьюшка, которая обрабатывает ajax-запрос на удаление товара из корзины
    """
    product_id = int(request.GET['product_url_detail'].split('/')[-2])
    ShoppingBasketModel.objects.get(user=request.user, product=product_id).delete()
    return HttpResponse()


class ShopingBasketView(ListView):
    model = ShoppingBasketModel
    template_name = 'shopping_basket/shopping_basket.html'
    context_object_name = 'objects'
    
    def get_queryset(self):
        return ShoppingBasketModel.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Формируем список из кортежей (товар, название_категории, url_photo, кол-во_товара)
        # Для всех товаров на странице (Оптимизация SQL-запроса)
        context['objects'] = get_product_category_photo_count(context['objects'])
        return context


def ajax_update_count_product_from_shopping_bassket(request):
    """ Вьюшка, которая обрабатывает ajax-запрос на обновление количества товара
        корзине
    """
    product_id = int(request.GET['product_url_detail'].split('/')[-2])
    new_count = int(request.GET['new_count'])
    obj = ShoppingBasketModel.objects.get(user=request.user.id, product=product_id)
    obj.count = new_count
    obj.save()
    return HttpResponse()


def ajax_buy_products_from_shopping_bassket(request):
    """ Вьюшка, которая обрабатывает ajax-запрос на покупку товара из корзины
    """
    message = buy_products(request.user) 
    if not message or len(message) == 0:
        return HttpResponse()
    else:
        return HttpResponseServerError(message)
    
    
