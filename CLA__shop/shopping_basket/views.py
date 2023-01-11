from django.shortcuts import redirect
from django.views.generic import ListView

from .models import Product, ShoppingBasketModel


def add_product_in_shopping_basket(request):
    
    product_id = request.GET['product']
    
    # Добавляем товар в корзину к пользователю
    ShoppingBasketModel.objects.update_or_create(
        user=request.user,
        product=Product.objects.get(id=product_id),
        count=1,
    )
    return redirect('product_detail', pk=product_id)


class ShopingBasketView(ListView):
    model = ShoppingBasketModel
    template_name = 'shopping_basket/shopping_basket.html'
    context_object_name = 'objects'
    
    def get_queryset(self):
        print(ShoppingBasketModel.objects.filter(user=self.request.user))
        return ShoppingBasketModel.objects.filter(user=self.request.user)
