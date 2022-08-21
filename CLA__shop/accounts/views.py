from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from django.views.generic import CreateView

from django.shortcuts import render, redirect

from .forms import CustomUserCreateForm, CustomAuthenticationForm


class RegisterUser(CreateView):
    template_name = 'accounts/register_login_user.html'
    form_class = CustomUserCreateForm

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
        return redirect('home')


class LoginUser(LoginView):
    template_name = 'accounts/register_login_user.html'
    form_class = CustomAuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        context['text_button'] = 'Войти'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
