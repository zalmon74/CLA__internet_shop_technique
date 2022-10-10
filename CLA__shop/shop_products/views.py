from django.core.cache import cache

from django.views.generic import TemplateView

from django.http import JsonResponse

from shop_products.models import BrandProduct

from .business_logic import *


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


def ajax_get_categories_with_id_elements_specifications(request):
    """
    Вьюшка, которая обрабатывает ajax-запрос на выдачу id-элементов формы для всех категорий
    """
    # Формируем словарь, который сопоставляет категории и id-элементов. Чтобы отображать необходимые формы
    # при добавлении элемента. Или берем из кэша.
    dict_match_cat_spec = cache.get('dict_match_cat_spec')
    if not dict_match_cat_spec:
        dict_match_cat_spec = create_dict_match_category_and_specification()
        cache.set('dict_match_cat_spec', dict_match_cat_spec, 60)
    return JsonResponse({'dict_match_cat_spec': dict_match_cat_spec})


class IndexView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_categories = cache.get('all_categories')
        if not all_categories:
            all_categories = CategoryProduct.objects.all()
            cache.set('all_categories', all_categories, 60)
        context['all_categories'] = all_categories
        return context
