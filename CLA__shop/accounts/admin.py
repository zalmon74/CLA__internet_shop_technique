from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreateForm
from .models import CustomUser


@admin.register(CustomUser)
class AdminCustomUser(UserAdmin):

    add_form = CustomUserCreateForm

    list_display = ['username', 'email', 'mail_confirmation', 'first_name', 'last_name', 'is_staff', 'is_superuser',]
    list_display_links = ['username', 'email', 'first_name', 'last_name', ]

    fieldsets = (
        ('Данные для авторизации', {'fields': ('username', 'password')}),
        ('Персональная информация', {
            'fields': ('email', 'first_name', 'last_name', 'mail_confirmation', 'favorite_products', 'favorite_brands')
        }),
        ('Права доступа', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined', 'mail_confirmation', 'favorite_products', 'favorite_brands')
    add_fieldsets = (
        (
            'Обязательные поля', {
                'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'captcha')
            }
        ),
        ('Второстепенные поля', {'fields': ('is_staff', )}),
    )
