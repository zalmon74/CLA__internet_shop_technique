import unittest

from django.core.validators import ValidationError

from django.contrib.auth import get_user_model

from django.test import TestCase

from .validators import validation_username, validation_first_last_name


class ValidatorsTests(unittest.TestCase):
    """
    Тесты проверяет работоспособность валидаторов
    """

    def test_username(self):
        """
        Проверка валидации логина пользователя
        """
        username_valid = ['test', 'test1', '1test', 't1est', 'Test', 'TEST', 'TesT']
        username_invalid = [' test', 'test ', 'test 1', '1 test', 'тест', 'Тест', 'TestТест', 'ТестTest']

        for username in username_valid:
            self.assertIsNone(validation_username(username))

        for username in username_invalid:
            with self.assertRaises(ValidationError, msg=f'Слово: {username} не вызвало исключение, хотя должно было'):
                validation_username(username)

    def test_first_last_name(self):
        """
        Проверка валидации имени и фамилии пользователя
        """
        first_name_valid = ['Тест', 'тест', 'тЕст', 'тесТ', 'ТесТ', 'Тест-Тест', 'Тест-Тест-Тест']
        first_name_invalid = [' Тест', 'Тест ', 'Тест тест', 'Test', 'TestТест', 'ТестTest', 'Тест1', '1Тест', 'Т1ест']

        for first_name in first_name_valid:
            self.assertIsNone(validation_first_last_name(first_name))

        for first_name in first_name_invalid:
            with self.assertRaises(
                    ValidationError,
                    msg=f'Слово: "{first_name}" не вызвало исключение, хотя должно было'
            ):
                validation_first_last_name(first_name)


class CustomUserManagerTest(TestCase):
    """
    Проверка пользовательского менеджера моделей
    """

    def _check_raises_create_user(self, username, email, first_name, last_name):
        """
        Проверка исключений при создании пользователя

        :param username: Логин пользователя
        :param email: Эмаил пользователя
        :param first_name: Имя пользователя
        :param last_name:  Фамилия пользователя
        """
        user_model = get_user_model()

        with self.assertRaises(TypeError):
            user_model.objects.create_user()
        with self.assertRaises(TypeError):
            user_model.objects.create_user(username)
        with self.assertRaises(TypeError):
            user_model.objects.create_user(username, email)
        with self.assertRaises(TypeError):
            user_model.objects.create_user(username, email, first_name)
        with self.assertRaises(TypeError):
            user_model.objects.create_user(username, email, first_name, last_name)


    def test_create_user(self):
        """
        Проверка создания простого пользователя
        """
        username = 'TestUser'
        email = 'testuser@mail.ru'
        first_name = 'Test'
        last_name = 'User'
        password = 'password'

        user_model = get_user_model()
        user = user_model.objects.create_user(
            username,
            email,
            first_name,
            last_name,
            password,
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self._check_raises_create_user(username, email, first_name, last_name)

    def test_create_staff_user(self):
        """
        Проверка создания администратора
        """
        username = 'TestStaffUser'
        email = 'teststaffuser@mail.ru'
        first_name = 'Staff'
        last_name = 'User'
        password = 'password'

        user_model = get_user_model()
        user = user_model.objects.create_admin(
            username,
            email,
            first_name,
            last_name,
            password,
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)
        self._check_raises_create_user(username, email, first_name, last_name)

    def test_create_superuser(self):
        """
        Проверка создания суперпользователя
        """

        username = 'TestSuperUser'
        email = 'testsuperuser@mail.ru'
        first_name = 'Super'
        last_name = 'User'
        password = 'password'

        user_model = get_user_model()
        user = user_model.objects.create_superuser(
            username,
            email,
            first_name,
            last_name,
            password,
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self._check_raises_create_user(username, email, first_name, last_name)
