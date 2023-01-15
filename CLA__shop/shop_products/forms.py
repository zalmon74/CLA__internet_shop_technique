from django import forms
from phonenumber_field.formfields import (
    PhoneNumberField, RegionalPhoneNumberWidget,
)
from shop_products.validators import validate_category_name

from .business_logic import get_all_name_brands, get_all_name_categories


class ContactUsForm(forms.Form):
    """
    Форма "Связаться с нами"
    """

    name = forms.CharField(
        max_length=100,
        validators=[validate_category_name],
        widget=forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Имя'})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contactus', 'placeholder': 'Email'}))
    phone_number = PhoneNumberField(
        widget=RegionalPhoneNumberWidget(attrs={'class': 'contactus', 'placeholder': 'Номер телефона (начиная с +)'})
    )
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Сообщение'})
    )


class FilterProductsForm(forms.Form):
    """
    Форма с фильтрами для товаров
    """

    categories = forms.CharField(
        label='Категория',
        required=False,
        widget=forms.SelectMultiple(choices=get_all_name_categories())
    )
    brands = forms.CharField(label='Бренд', required=False, widget=forms.SelectMultiple(choices=get_all_name_brands()))

