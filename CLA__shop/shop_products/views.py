from django.core.cache import cache

from django.views.decorators.cache import cache_page

from django.http import JsonResponse

from shop_products.models import BrandProduct


def ajax_get_categories_for_current_brand(request):
    """
    Вьюшка, которая обрабатывает ajax запрос на выдачу категорий для соответствующего бренда
    """
    # Вытаскиваем из БД или кэша выбранный бренд, чтобы определить доступные категории
    brand = request.GET.get('brand')
    if brand != '':  # Если бренд не выбран, то отправляем пустой словарь
        # output_dict = None
        output_dict = cache.get('brand_' + str(brand))
        if not output_dict:
            brand = BrandProduct.objects.get(pk=brand)
            # Запихиваем все доступные категории в выходной словарь
            output_dict = {'categories': []}
            for category in brand.categories.all():
                output_dict['categories'].append(
                    {'pk': category.pk, 'name': category.name}
                )
            # Добавляем в кэш
            cache.set('brand_' + str(brand), output_dict, 60)
    else:
        output_dict = {}
    return JsonResponse(output_dict)

