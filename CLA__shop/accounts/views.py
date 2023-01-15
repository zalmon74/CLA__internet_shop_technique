from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView

from .business_logic import get_queryset_brandproduct_exclude_favite_for_user
from .forms import (
    ChangeUserPasswordForm, CustomAuthenticationForm, CustomUserCreateForm,
    FavoriteBrandsForm, ProfileUserForm,
)
from .models import BrandProduct, Product


class RegisterUser(CreateView):
    """
    Вьюшка для регистрации пользователя
    """

    template_name = 'accounts/register_login_user.html'
    form_class = CustomUserCreateForm

    def get(self, request, *args, **kwargs):
        # Если пользователь уже авторизован, то он не должен видеть данную страницу
        if self.request.user.is_authenticated:
            return redirect('user_profile')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['text_button'] = 'Регистрация'
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        del form.fields['is_staff']
        return form

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user_profile')


class LoginUser(LoginView):
    """
    Вьюшка авторизации пользователя
    """

    template_name = 'accounts/register_login_user.html'
    form_class = CustomAuthenticationForm

    def get(self, request, *args, **kwargs):
        # Если пользователь уже авторизован, то он не должен видеть данную страницу
        if self.request.user.is_authenticated:
            return redirect('user_profile')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        context['text_button'] = 'Войти'
        return context

    def get_success_url(self):
        return reverse_lazy('user_profile')


def logout_user(request):
    """
    Вьюшка для выхода пользователя
    """

    logout(request)
    return redirect('home')


class UserProfile(FormView):
    """
    Отображение аккаунта пользователя
    """

    template_name = 'accounts/user_profile.html'
    form_class = ProfileUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        context['text_button'] = 'Изменить данные'
        return context

    def get_form(self, form_class=None):
        # Получаем форму и заполняем ее пользовательскими данными
        form = super().get_form(form_class)
        form.fields['username'].initial = self.request.user.username
        form.fields['email'].initial = self.request.user.email
        form.fields['first_name'].initial = self.request.user.first_name
        form.fields['last_name'].initial = self.request.user.last_name

        return form

    def form_valid(self, form):
        data = form.cleaned_data
        self.request.user.first_name = data['first_name']
        self.request.user.last_name = data['last_name']
        self.request.user.save()
        return redirect('user_profile')


class UserChangePassword(FormView):
    """
    Изменение пароля пользователя
    """

    template_name = 'accounts/change_password_user.html'
    form_class = ChangeUserPasswordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение пароля'
        context['text_button'] = 'Изменить пароль'
        return context

    def form_valid(self, form):
        password = form.clean_password2()
        user = self.request.user
        user.set_password(password)
        user.save()
        login(self.request, user)
        return redirect('user_profile')


class UserFavoriteProducts(ListView):
    """ Показывает список избранных товаров пользователя
    """
    template_name = 'accounts/favorite_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return self.request.user.favorite_products.all()


def ajax_delete_product_from_favorite(request):
    """ Вьюшка, которая обрабатывает ajax-запрос на удаление товара из избранного
    """
    # Получаем ИД товара, который необходимо удалить
    product_id = int(request.GET['product_url_detail'].split('/')[-2])
    # Удаляем товар
    request.user.favorite_products.remove(Product.objects.get(id=product_id))
    return HttpResponse()


class UserFavoriteBrands(FormView):
    """ Показывает список избранных брендов, а также позволяет их выбирать
    """
    template_name = 'accounts/favorite_brands.html'
    form_class = FavoriteBrandsForm

    def get_form(self, form_class=None, *args, **kwargs):
        form = super().get_form(form_class,  *args, **kwargs)
        form.fields['favorite_brands'].label = 'Доступные бренды'
        brands = get_queryset_brandproduct_exclude_favite_for_user(self.request.user)
        self.len_brandproduct_exclude_favite_for_user = len(brands)
        form.fields['favorite_brands'].queryset = brands
        return form
    
    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        # Добавляем бренды в избранное
        lst_favorite_brands = request.GET.getlist('favorite_brands', [])
        if len(lst_favorite_brands) != 0:
            for brand in BrandProduct.objects.filter(id__in=lst_favorite_brands):
                request.user.favorite_brands.add(brand)
            return HttpResponseRedirect('/accounts/user_favorite_brands/')
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['len_brandproduct_exclude_favite_for_user'] = self.len_brandproduct_exclude_favite_for_user
        context['favorite_brands'] = self.request.user.favorite_brands.all()
        return context
    
def ajax_delete_brand_from_favorite(request):
    """ Вьюшка, которая обрабатывает ajax-запрос на удаление бренда из избранного
    """
    # Получаем ИД товара, который необходимо удалить
    name_brand = request.GET['favorite_brand_name_delte']
    # Удаляем бренд из избранного
    request.user.favorite_brands.remove(BrandProduct.objects.get(name=name_brand))
    return HttpResponse()
