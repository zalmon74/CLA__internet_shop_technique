from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import redirect
from django.views.generic import ListView
from shop_products.models import PurchaseHistoryModel

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
    message = ''
    message_email = 'Вы купили: \n'
    # Получаем список продуктов с корзины
    lst_products_in_basket = ShoppingBasketModel.objects.filter(user=request.user.id)    
    # Вычесть количество каждого продукта в своей таблице и проверить количество
    # запрашиваемого товара, если не хватает
    lst_products = Product.objects.filter(id__in=[obj.product.id for obj in lst_products_in_basket])
    lst_products_for_purchase_history = []
    for product in lst_products:
        prod_basket_count = lst_products_in_basket.get(product=product.id).count
        left_prod_count = product.count-prod_basket_count
        if left_prod_count < 0:
            message += f'Вы ввели слишком большое количество товара "{product.name}". Введите другое значение (максимальное {product.count}).'
        else:
            lst_products_for_purchase_history.append(PurchaseHistoryModel(
                    user=request.user, 
                    products=product,
                    count=prod_basket_count,
                )
            )
            product.count = left_prod_count
            message_email += f'\t{product.name} в количестве {prod_basket_count} штук по цене {product.price} р.\n'
    # Если нет ошибок, то обрабатываем дальше
    if len(message) == 0:
        # Изменяем время на одинаковое
        for product in lst_products_for_purchase_history:
            product.datetime_purchase = lst_products_for_purchase_history[-1].datetime_purchase    
        PurchaseHistoryModel.objects.bulk_create(lst_products_for_purchase_history)
        # Если занесли строки о покупках, тогда необходимо обновить таблицу с
        # товарами (обновить их количество), а также отчистить корзину
        [product.save() for product in lst_products]
        lst_products_in_basket.delete()
        # Отправить сообщение о покупке на почту      
        send_mail(
            subject='Покупка товаров',
            message=message_email,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email,]
        )
        return HttpResponse()
    else:
        return HttpResponseServerError(message)
    
    
