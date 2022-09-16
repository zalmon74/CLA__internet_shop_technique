from django.db import models

from ..products import Product


class FactoryDataCoolerSpecifications(models.Model):
    """
    Заводские данные
    """
    warranty = models.IntegerField(verbose_name='Гарантия от производителя')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Заводские данные для товара {self.product} категории "Кулер"'

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'
        ordering = ['product', ]


class CommonParametersCoolerSpecifications(models.Model):
    """
    Общие данные
    """
    type = models.CharField(max_length=20, default='Кулер для процессора', verbose_name='Тип')
    model = models.CharField(max_length=25, verbose_name='Модель')
    socket = models.CharField(max_length=100, verbose_name='Сокет')
    power_dissipation = models.IntegerField(verbose_name='Рассеиваемая мощность', help_text='Вт')
    construction_type = models.CharField(max_length=25, verbose_name='Тип конструкции')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Общие данные для товара {self.product} категории "Кулер"'

    class Meta:
        verbose_name = 'Общие данные'
        verbose_name_plural = 'Общие данные'
        ordering = ['product', ]


class RadiatorCoolerSpecifications(models.Model):
    """
    Радиатор
    """
    base_material = models.CharField(max_length=25, verbose_name='Материал основания')
    radiator_material = models.CharField(max_length=25, verbose_name='Материал радиатора')
    number_heat_pipes = models.IntegerField(verbose_name='Количество тепловых трубок')
    heat_pipe_diameter = models.IntegerField(verbose_name='Диаметр тепловых трубок', help_text='мм.')
    nickel_plated = models.CharField(max_length=50, verbose_name='Никелированное покрытие')
    radiator_color = models.CharField(max_length=25, verbose_name='Цвет радиатора')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Радиатор для товара {self.product} категории "Кулер"'

    class Meta:
        verbose_name = 'Радиатор'
        verbose_name_plural = 'Радиатор'
        ordering = ['product', ]


class FanCoolerSpecifications(models.Model):
    """
    Вентилятор
    """
    number_fans_included = models.IntegerField(verbose_name='Количество вентиляторов в комплекте')
    max_number_installed_fans = models.IntegerField(verbose_name='Максимальное количество устанавливаемых вентиляторов')
    dimensions_complete_fans = models.CharField(max_length=50, verbose_name='Размеры комплектных вентиляторов')
    fan_color = models.CharField(max_length=25, verbose_name='Цвет вентиляторов')
    max_rotation_speed = models.IntegerField(verbose_name='Максимальная скорость вращения', help_text='об/мин')
    min_rotation_speed = models.IntegerField(verbose_name='Минимальная скорость вращения', help_text='об/мин')
    rotation_speed_adjustment = models.CharField(
        max_length=15,
        default='Автоматическая',
        verbose_name='Регулировка скорости вращения',
    )
    max_airflow = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Максимальный воздушный поток',
        help_text='CFM',
    )
    max_static_pressure = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Максимальное статическое давление',
        help_text='Па',
    )
    max_noise_level = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Максимальный уровень шума',
        help_text='дБ',
    )
    rated_current = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Номинальный ток',
        help_text='А',
    )
    rated_voltage = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Номинальное напряжение',
        help_text='В',
    )
    bearing_type = models.CharField(max_length=50, verbose_name='Тип подшипника')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Вентилятор для товара {self.product} категории "Кулер"'

    class Meta:
        verbose_name = 'Вентилятор'
        verbose_name_plural = 'Вентилятор'
        ordering = ['product', ]


class DimensionsCoolerSpecifications(models.Model):
    """
    Габариты
    """
    length = models.IntegerField(verbose_name='Длина', help_text='мм.')
    width = models.IntegerField(verbose_name='Ширина', help_text='мм.')
    height = models.IntegerField(verbose_name='Высота', help_text='мм.')
    weight = models.IntegerField(verbose_name='Вес', help_text='г.')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Габариты данные для товара {self.product} категории "Кулер"'

    class Meta:
        verbose_name = 'Габариты'
        verbose_name_plural = 'Габариты'
        ordering = ['product', ]













