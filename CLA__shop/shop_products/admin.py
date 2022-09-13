from django.contrib import admin

from django.utils.safestring import mark_safe

from .models import *


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=100>')

    list_display = ('id', 'name', 'get_html_photo', )
    fields = ('name', 'photo', 'get_html_photo', )
    readonly_fields = ('get_html_photo', )

    get_html_photo.short_description = 'Фото'


admin.site.register(Product)
admin.site.register(BrandProduct)

admin.site.register(ComputerCaseSpecifications)
admin.site.register(CoolerSpecifications)
admin.site.register(HDDSpecifications)
admin.site.register(MotherboardSpecifications)
admin.site.register(PowerSupplySpecifications)
admin.site.register(ProcessorSpecifications)
admin.site.register(RamSpecifications)
admin.site.register(SolidStateDriveSpecifications)
admin.site.register(VideoCartSpecifications)
