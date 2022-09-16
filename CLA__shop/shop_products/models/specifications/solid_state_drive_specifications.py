from django.db import models

from ..products import Product


class FactoryDataSolidStateDriveSpecifications(models.Model):
    """
    Заводские данные
    """
    warranty = models.IntegerField(verbose_name='Гарантия')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Заводские данные для товара {self.product} категории "ССД"'

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'
        ordering = ['product', ]


class CommonParametersSolidStateDriveSpecifications(models.Model):
    """
    Общие параметры
    """
    type = models.CharField(max_length=15, default='SSD накопитель', verbose_name='Тип')
    model = models.CharField(max_length=50, verbose_name='Модель')
    manufacturer_code = models.CharField(max_length=50, verbose_name='Код производителя')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Общие параметры для товара {self.product} категории "ССД"'

    class Meta:
        verbose_name = 'Общие параметры'
        verbose_name_plural = 'Общие параметры'
        ordering = ['product', ]


class MainCharacteristicsSolidStateDriveSpecifications(models.Model):
    """
    Основные характеристики
    """
    storage_capacity = models.IntegerField(verbose_name='Объект накопителя', help_text='Гб')
    nvme = models.BooleanField(default=False, verbose_name='Поддержка NVMе')
    connection_connector = models.CharField(max_length=10, verbose_name='Разъем подключения')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Основные характеристики для товара {self.product} категории "ССД"'

    class Meta:
        verbose_name = 'Основные характеристики'
        verbose_name_plural = 'Основные характеристики'
        ordering = ['product', ]


class DriveConfigurationSolidStateDriveSpecifications(models.Model):
    """
    Конфигурация накопителя
    """
    number_bits_per_cell = models.IntegerField(verbose_name='Количество бит на ячейку')
    memory_structure = models.CharField(max_length=25, verbose_name='Структура памяти')
    dram_buffer = models.BooleanField(default=False, verbose_name='Наличие DRAM-буфера')
    size_dram_buffer = models.IntegerField(verbose_name='Размер DRAM-буфера', help_text='МБ')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Конфигурация накопителя для товара {self.product} категории "ССД"'

    class Meta:
        verbose_name = 'Конфигурация накопителя'
        verbose_name_plural = 'Конфигурация накопителя'
        ordering = ['product', ]


class PerformanceIndicatorsSolidStateDriveSpecifications(models.Model):
    """
    Показатели производительности
    """
    max_sequential_read_speed = models.IntegerField(verbose_name='Максимальная скорость последовательного чтения')
    max_sequential_write_speed = models.IntegerField(verbose_name='Максимальная скорость последовательной записи')
    random_read_speed_qd32 = models.IntegerField(verbose_name='Скорость произвольного чтения 4 Кб файлов (QD32)')
    random_write_speed_qd32 = models.IntegerField(verbose_name='Скорость произвольной записи 4 Кб файлов (QD32)')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Показатели производительности для товара {self.product} категории "ССД"'

    class Meta:
        verbose_name = 'Показатели производительности'
        verbose_name_plural = 'Показатели производительности'
        ordering = ['product', ]


class ReliabilitySolidStateDriveSpecifications(models.Model):
    """
    Надежность
    """
    tbw = models.IntegerField(verbose_name='Максимальный ресурс записи (TBW)', help_text='ТБ')
    dwpd = models.FloatField(verbose_name='DWPD')
    max_overload = models.IntegerField(verbose_name='Максимальная перегрузка', help_text='G')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Надежность для товара {self.product} категории "ССД"'

    class Meta:
        verbose_name = 'Надежность'
        verbose_name_plural = 'Надежность'
        ordering = ['product', ]


class DimensionsSolidStateDriveSpecifications(models.Model):
    """
    Габариты, вес
    """
    length = models.IntegerField(verbose_name='Длина', help_text='мм.')
    width = models.IntegerField(verbose_name='Ширина', help_text='мм.')
    height = models.IntegerField(verbose_name='Высота', help_text='мм.')
    weight = models.IntegerField(verbose_name='Вес', help_text='г.')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Габариты, вес для товара {self.product} категории "ССД"'

    class Meta:
        verbose_name = 'Габариты, вес'
        verbose_name_plural = 'Габариты, вес'
        ordering = ['product', ]










