from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreateForm


@admin.register(CustomUser)
class AdminCustomUser(UserAdmin):

    add_form = CustomUserCreateForm

    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser',]
    list_display_links = ['username', 'email', 'first_name', 'last_name', ]

    fieldsets = (
        ('Данные для авторизации', {'fields': ('username', 'password')}),
        ('Персональная информация', {
            'fields': ('email', 'first_name', 'last_name', 'favorite_products', 'favorite_brands')
        }),
        ('Права доступа', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined', 'favorite_products', 'favorite_brands')
    add_fieldsets = (
        (
            'Обязательные поля', {
                'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')
            }
        ),
        ('Второстепенные поля', {'fields': ('is_staff', )}),
    )
