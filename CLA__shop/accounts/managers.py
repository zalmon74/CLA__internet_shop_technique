from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Перегруженный менеджер для пользователя. Добавлены новые обязательные поля: Имя, Фамилия, email

    Добавлен новый метод: создание админа, который создает пользователя с правами администратора (персонала)
    """

    def create_user(self, username, email, first_name, last_name, password, **extra_fields):
        """
        Создание обычного пользователя (покупателя) в магазине

        :param username: логин пользователя
        :param email: эмаил пользователя
        :param first_name: Имя пользователя
        :param last_name: Фамилия пользователя
        :param password: пароль
        :param extra_fields: дополнительные поля
        """
        # Проверяем входные параметры
        if not username:
            raise ValueError('username - является обязательным полем')
        if not email:
            raise ValueError('email - является обязательным полем')
        if not first_name:
            raise ValueError('first_name - является обязательным полем')
        if not last_name:
            raise ValueError('last_name - является обязательным полем')
        # Формируем модель пользователя
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_admin(self, username, email, first_name, last_name, password, **extra_fields):
        """
        Создание администратора (персонала) в магазине

        :param username: логин пользователя
        :param email: эмаил пользователя
        :param first_name: Имя пользователя
        :param last_name: Фамилия пользователя
        :param password: пароль
        :param extra_fields: дополнительные поля
        """
        # Устанавливаем флаги
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Администратор должен иметь is_staff=True')
        if extra_fields.get('is_superuser') is not False:
            raise ValueError('Администратор должен иметь is_superuser=False')
        return self.create_user(username, email, first_name, last_name, password, **extra_fields)

    def create_superuser(self, username, email, first_name, last_name, password, **extra_fields):
        """
        Создание суперпользователя в магазине

        :param username: логин пользователя
        :param email: эмаил пользователя
        :param first_name: Имя пользователя
        :param last_name: Фамилия пользователя
        :param password: пароль
        :param extra_fields: дополнительные поля
        """
        # Устанавливаем флаги
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True')
        return self.create_user(username, email, first_name, last_name, password, **extra_fields)




