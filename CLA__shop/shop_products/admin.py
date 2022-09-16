from django.contrib import admin

from django.utils.safestring import mark_safe

from .models import *


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):

    def get_html_photo(self, object_):
        if object_.photo:
            return mark_safe(f'<img src="{object_.photo.url}" width=100>')

    list_display = ('id', 'name', 'get_html_photo', )
    list_display_links = ('name', 'get_html_photo')

    fields = ('id', 'name', 'photo', 'get_html_photo', )
    readonly_fields = ('id', 'get_html_photo', )

    search_fields = ('name', )

    get_html_photo.short_description = 'Фото'


@admin.register(BrandProduct)
class BrandProductAdmin(admin.ModelAdmin):

    def get_html_photo(self, object_):
        if object_.photo:
            return mark_safe(f'<img src="{object_.photo.url}" width=100>')

    list_display = ('id', 'name', 'get_html_photo', 'email', 'show')
    list_display_links = ('name', 'get_html_photo', 'email')

    fields = ('id', 'name', 'photo', 'get_html_photo', 'email', 'categories', 'description', 'show')
    readonly_fields = ('id', 'get_html_photo')

    search_fields = ('name', 'categories')
    list_filter = ('categories', 'show', )

    list_editable = ('show', )


admin.site.register(Product)

