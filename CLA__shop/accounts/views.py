from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from django.views.generic import CreateView, FormView

from django.shortcuts import render, redirect

from .models import CustomUser
from .forms import CustomUserCreateForm, CustomAuthenticationForm, ProfileUserForm, ChangeUserPasswordForm


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
