
from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.password_validation import validate_password

from .business_logic import check_confirm_code
from .models import CustomUser


class CustomUserCreateForm(UserCreationForm):
    """
    Форма создания пользователя
    """

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Пароль'})
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Повтор пароля'})
    )

    captcha = CaptchaField(
        widget=(
            CaptchaTextInput(
                attrs={'class': 'contactus', 'style': 'margin-top: 30px;', 'placeholder': 'Введите текст с картинки'}
            )
        ),
        error_messages={'invalid': 'Введенный текст не соответствует картинке, пожалуйста повторите'},
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
    """
    Форма аутентификации пользователя
    """

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


class ProfileUserForm(forms.Form):
    """
    Форма для отображения данных о пользователе и изменении его имени и фамилии
    """

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'contactus', 'readonly': ''})
    )
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'contactus', 'readonly': ''})
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'contactus', })
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'contactus', })
    )


class ChangeUserPasswordForm(forms.Form):
    """
    Форма для изменения пароля профиля
    """

    error_messages = {
        'password_mismatch': 'Введенные пароли не совпадают',
    }
    password1 = forms.CharField(
        label='Пароль',
        validators=[validate_password],
        widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Пароль'})
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        validators=[validate_password],
        widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Повтор пароля'})
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


class ConfirmEmailUserForm(forms.Form):
    """
    Форма для подтверждения email'а
    """
    confirm_email = forms.CharField(
        label='Код',
        required=False,
        widget=forms.TextInput(attrs={'class': 'contactus'})
    )
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ConfirmEmailUserForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        cleanned_data = super().clean()
        # Проверяем правильность введенного кода
        if not check_confirm_code(self.request.user, cleanned_data['confirm_email']):
            self.add_error('confirm_email', 'Неверный код')
        return cleanned_data
    

class FavoriteBrandsForm(forms.ModelForm):
    """
    Форма с избранными брендами
    """
    
    class Meta:
        model = CustomUser
        fields = ['favorite_brands', ]
