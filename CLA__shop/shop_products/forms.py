from django import forms

from phonenumber_field.formfields import PhoneNumberField, RegionalPhoneNumberWidget

from shop_products.validators import validate_category_name


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


