from django.core.validators import ValidationError

import re


def validate_category_name(name):
    """
    Валидатор для названия категории.

    Категория может состоять только из русских символов и пробелов
    """

    if bool(re.search('[a-zA-Z0-9]', name)):
        raise ValidationError('Название категории должно состоять только из русских букв')

