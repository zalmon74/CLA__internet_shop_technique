from django.core.validators import ValidationError

import re


def validation_username(username):
    """
    Валидатор для проверки имени пользователя

    :param username: Имя пользователя
    """

    if ' ' in username or bool(re.search('[а-яА-Я]', username)):
        raise ValidationError('Введенный логин должен состоять только из латинских букв и цифр')


def validation_first_last_name(name):
    """
    Валидатор для проверки имени и фамилии пользователей

    :param name: Имя или фамилия пользователя
    """

    if ' ' in name or bool(re.search('[a-zA-Z]', name)) or bool(re.search('[0-9]', name)):
        raise ValidationError(f'Поле должно содержать только русские буквы')
