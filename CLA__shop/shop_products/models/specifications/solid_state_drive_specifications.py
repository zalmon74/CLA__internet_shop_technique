from django.db import models

from ..products import Product


class FactoryDataSolidStateDriveSpecifications(models.Model):
    """
    Заводские данные
    """
    warranty = models.IntegerField(verbose_name='Гарантия')

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'


class CommonParametersSolidStateDriveSpecifications(models.Model):
    """
    Общие параметры
    """
    type = models.CharField(max_length=15, default='SSD накопитель', verbose_name='Тип')
    model = models.CharField(max_length=50, verbose_name='Модель')
    manufacturer_code = models.CharField(max_length=50, verbose_name='Код производителя')

    class Meta:
        verbose_name = 'Общие параметры'
        verbose_name_plural = 'Общие параметры'


class MainCharacteristicsSolidStateDriveSpecifications(models.Model):
    """
    Основные характеристики
    """
    storage_capacity = models.IntegerField(verbose_name='Объект накопителя', help_text='Гб')
    nvme = models.BooleanField(default=False, verbose_name='Поддержка NVMе')
    connection_connector = models.CharField(max_length=10, verbose_name='Разъем подключения')

    class Meta:
        verbose_name = 'Основные характеристики'
        verbose_name_plural = 'Основные характеристики'


class DriveConfigurationSolidStateDriveSpecifications(models.Model):
    """
    Конфигурация накопителя
    """
    number_bits_per_cell = models.IntegerField(verbose_name='Количество бит на ячейку')
    memory_structure = models.CharField(max_length=25, verbose_name='Структура памяти')
    dram_buffer = models.BooleanField(default=False, verbose_name='Наличие DRAM-буфера')
    size_dram_buffer = models.IntegerField(verbose_name='Размер DRAM-буфера', help_text='МБ')

    class Meta:
        verbose_name = 'Конфигурация накопителя'
        verbose_name_plural = 'Конфигурация накопителя'


class PerformanceIndicatorsSolidStateDriveSpecifications(models.Model):
    """
    Показатели производительности
    """
    max_sequential_read_speed = models.IntegerField(verbose_name='Максимальная скорость последовательного чтения')
    max_sequential_write_speed = models.IntegerField(verbose_name='Максимальная скорость последовательной записи')
    random_read_speed_qd32 = models.IntegerField(verbose_name='Скорость произвольного чтения 4 Кб файлов (QD32)')
    random_write_speed_qd32 = models.IntegerField(verbose_name='Скорость произвольной записи 4 Кб файлов (QD32)')

    class Meta:
        verbose_name = 'Показатели производительности'
        verbose_name_plural = 'Показатели производительности'


class ReliabilitySolidStateDriveSpecifications(models.Model):
    """
    Надежность
    """
    tbw = models.IntegerField(verbose_name='Максимальный ресурс записи (TBW)', help_text='ТБ')
    dwpd = models.FloatField(verbose_name='DWPD')
    max_overload = models.IntegerField(verbose_name='Максимальная перегрузка', help_text='G')

    class Meta:
        verbose_name = 'Надежность'
        verbose_name_plural = 'Надежность'


class DimensionsSolidStateDriveSpecifications(models.Model):
    """
    Габариты, вес
    """
    length = models.IntegerField(verbose_name='Длина', help_text='мм.')
    width = models.IntegerField(verbose_name='Ширина', help_text='мм.')
    height = models.IntegerField(verbose_name='Высота', help_text='мм.')
    weight = models.IntegerField(verbose_name='Вес', help_text='г.')

    class Meta:
        verbose_name = 'Габариты, вес'
        verbose_name_plural = 'Габариты, вес'


class SolidStateDriveSpecifications(models.Model):
    """
    Расширенные характеристики для ССД
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')
    factory_data = models.ForeignKey(
        FactoryDataSolidStateDriveSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Заводские данные',
        related_name='+',
    )
    common_data = models.ForeignKey(
        CommonParametersSolidStateDriveSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Общие данные',
    )
    main_characteristics = models.ForeignKey(
        MainCharacteristicsSolidStateDriveSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Основные характеристики',
    )
    drive_configuration = models.ForeignKey(
        DriveConfigurationSolidStateDriveSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Конфигурация накопителя',
    )
    performance_indicators = models.ForeignKey(
        PerformanceIndicatorsSolidStateDriveSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Показатели производительности',
    )
    reliability = models.ForeignKey(
        ReliabilitySolidStateDriveSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Надежность',
    )
    dimensions = models.ForeignKey(
        DimensionsSolidStateDriveSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Габариты, вес',
    )

    def __str__(self):
        return f'Расширенные характеристики для ССД {self.product}'

    class Meta:
        verbose_name = 'Расширенные характеристики для ССД'
        verbose_name_plural = 'Расширенные характеристики для ССД'
        ordering = ['product', ]







