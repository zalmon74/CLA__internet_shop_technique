from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView

from .models import Product, ShoppingBasketModel


def ajax_add_product_in_shopping_bassket(request):
    product_id = int(request.GET['product_url_detail'].split('/')[-2])
    # Добавляем товар в корзину к пользователю
    ShoppingBasketModel.objects.update_or_create(
        user=request.user,
        product=Product.objects.get(id=product_id),
        count=1,
    )
    return HttpResponse()


class ShopingBasketView(ListView):
    model = ShoppingBasketModel
    template_name = 'shopping_basket/shopping_basket.html'
    context_object_name = 'objects'
    
    def get_queryset(self):
        return ShoppingBasketModel.objects.filter(user=self.request.user)
