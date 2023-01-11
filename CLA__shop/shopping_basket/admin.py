from django.contrib import admin

from .models import ShoppingBasketModel


@admin.register(ShoppingBasketModel)
class ShoppingBasketModelAdminModel(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'count')
    list_display_links = ('user', 'product', 'count')

    readonly_fields = ('id',)
    
    list_filter = ('user',)

