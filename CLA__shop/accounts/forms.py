from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms

from .models import CustomUser


class CustomUserCreateForm(UserCreationForm):

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Пароль'})
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Повтор пароля'})
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_staff',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Логин'}),
            'email': forms.EmailInput(attrs={'class': 'contactus', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Фамилия'}),
        }


class CustomAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Логин'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Пароль'})
    )

    class Meta:
        model = CustomUser
