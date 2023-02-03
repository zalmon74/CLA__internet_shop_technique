from django.core.cache import cache
from django.db import DatabaseError, transaction
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect
from django.views.generic import DetailView, FormView, ListView, TemplateView
from shop_products.forms import (
    ContactUsForm, FilterProductsForm, GiveReviewForProductForm,
)
from shop_products.models import (
    BrandProduct, CommentProductReviewModel, ContactFormModel, PhotoProduct,
    Product, ReviewProductModel,
)

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


def ajax_add_favorite_product(request):
    """ Вьюшка, которая обрабатывает ajax-запрос на добавление товара в избранный
    """
    product_id = int(request.GET['product_url_detail'].split('/')[-2])
    # Добавляем товар как избранный
    request.user.favorite_products.add(Product.objects.get(id=product_id))
    return HttpResponse()


class IndexView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавление товаров для банера
        products_for_banner = cache.get('products_for_banner')
        if not products_for_banner:
            products_for_banner = get_random_products()
            cache.set('products_for_banner', products_for_banner, 60)
        # Добавление фото для банера
        photo_for_banner = cache.get('photo_for_banner')
        if not photo_for_banner:
            photo_for_banner = PhotoProduct.objects.filter(product__in=[obj.pk for obj in products_for_banner])
            cache.set('photo_for_banner', photo_for_banner, 60)
        context['products_for_banner'] = {products_for_banner[ind]:photo_for_banner[ind].photo.url for ind in range(len(products_for_banner))}
        # Добавление категорий
        all_categories = cache.get('all_categories')
        if not all_categories:
            all_categories = CategoryProduct.objects.all()
            cache.set('all_categories', all_categories, 60)
        context['all_categories'] = all_categories
        # Добавление брендов
        all_brands = cache.get('all_brands')
        if not all_brands:
            all_brands = BrandProduct.objects.all()
            cache.set('all_brands', all_brands, 60)
        context['all_brands'] = all_brands
        return context


class AboutView(TemplateView):
    template_name = 'shop_products/about.html'


class ContactUsView(FormView):
    form_class = ContactUsForm
    template_name = 'shop_products/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Связаться с нами'
        context['text_button'] = 'Отправить'
        return context

    def form_valid(self, form):
        contact_model = ContactFormModel()
        contact_model.name = form.cleaned_data['name']
        contact_model.email = form.cleaned_data['email']
        contact_model.phone_number = form.cleaned_data['phone_number']
        contact_model.message = form.cleaned_data['message']
        contact_model.save()
        return redirect('home')


class ProductsListView(ListView, FormView):
    model = Product
    template_name = 'shop_products/product.html'
    context_object_name = 'all_products'

    paginate_by = 15

    form_class = FilterProductsForm

    def get_queryset(self):
        current_queryset = super().get_queryset()
        # Определяем фильтры
        filter_categories = self.request.GET.getlist('categories', [])
        filter_brands = self.request.GET.getlist('brands', [])
        # Фильтруем
        if len(filter_categories) != 0:
            current_queryset = current_queryset.filter(category__in=filter_categories)
        if len(filter_brands) != 0:
            current_queryset = current_queryset.filter(brand__in=filter_brands)
        return current_queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_categories'] = self.request.GET.getlist('categories', [])
        context['filter_brands'] = self.request.GET.getlist('brands', [])
        # Формируем список из кортежей (товар, название_категории, url_photo)
        # Для всех товаров на странице (Оптимизация SQL-запроса)
        context['all_products'] = get_product_category_photo(context['all_products'])
        
        return context


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'shop_products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = ReviewProductModel.objects.filter(product=self.get_object().id)
        return context


class GiveReviewForProduct(DetailView, FormView):
    model = Product
    form_class = GiveReviewForProductForm
    template_name = 'shop_products/give_review.html'
    
    def get(self, request, *args, **kwargs):
        # Определяем, оставлял ли покупалетль на данный товар отзыв
        try:
            review = get_review_object(self.request.user, self.get_object())
        except ReviewProductModel.DoesNotExist:
            # Если покупатель не оставлял отзыв, то отправляем его к форме
            return super().get(request, *args, **kwargs)
        else:
            # Если покупатель уже оставлял отзыв, то перенаправляем его на редактирования
            return redirect('edit_review', pk=self.get_object().pk)
    
    def form_valid(self, form):
        try:
            clean_data = form.cleaned_data
            with transaction.atomic():
                comment_obj = CommentProductReviewModel(content=clean_data['comment_text'])
                comment_obj.save()
                ReviewProductModel.objects.create(
                    product=self.get_object(),
                    user=self.request.user,
                    grade=clean_data['grade'],
                    comment=comment_obj,
                )
        except DatabaseError:
            return HttpResponseBadRequest()
        
        return redirect('purchase_history_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = f'Оставить отзыв на товар "{self.get_object().name}"'
        return context


class EditReviewForProduct(DetailView, FormView):
    model = Product
    form_class = GiveReviewForProductForm
    template_name = 'shop_products/give_review.html'
    
    def form_valid(self, form):
        try:
            clean_data = form.cleaned_data
            # Изменяем содержимое комментария к отзыву
            review_obj = get_review_object(self.request.user, self.get_object())
            review_obj.comment.content = clean_data['comment_text']
            review_obj.comment.save()
        except DatabaseError:
            return HttpResponseBadRequest()
        return redirect('purchase_history_user')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = f'Изменить отзыв к товару "{self.get_object().name}"'
        # Получаем уже оставленный отзыв
        review = get_review_object(self.request.user, self.get_object())
        # Выставляем уже созданную оценку и не даем возможности ее менять
        context['form'].fields['grade'].initial = review.grade
        context['form'].fields['grade'].choices = [(review.grade, review.grade),]
        # Добавляем в форму уже написанный комментарий
        context['form'].fields['comment_text'].initial = review.comment.content
        return context
