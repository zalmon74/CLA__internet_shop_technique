from django.db import models

from ..products import Product


class FactoryDataHDDSpecifications(models.Model):
    """
    Заводские данные
    """
    warranty = models.IntegerField(verbose_name='Гарантия от производителя')

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'


class CommonParametersHDDSpecifications(models.Model):
    """
    Общие параметры
    """
    type = models.CharField(max_length=15, default='HDD', verbose_name='Тип')
    model = models.CharField(max_length=50, verbose_name='Модель')
    manufacturer_code = models.CharField(max_length=50, verbose_name='Код производителя')

    class Meta:
        verbose_name = 'Общие параметры'
        verbose_name_plural = 'Общие параметры'


class StorageDeviceHDDSpecifications(models.Model):
    """
    Накопитель
    """
    hdd_volume = models.IntegerField(verbose_name='Объем', help_text='Гб')
    cache_size = models.IntegerField(verbose_name='Объем кэш-памяти', help_text='Мб')
    spindle_speed = models.IntegerField(verbose_name='Скорость вращения шпинделя', help_text='об/мин')
    max_data_rate = models.IntegerField(verbose_name='Максимальная скорость передачи данных', help_text='Мбайт/сек')
    average_latency = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Среднее время задержки')
    interface = models.CharField(max_length=15, default='SATA 3', verbose_name='Интерфейс')
    interface_bandwidth = models.IntegerField(
        default=6,
        verbose_name='Пропускная способность интерфейса',
        help_text='ГБит/с'
    )
    optimization_raid_arrays = models.BooleanField(default=False, verbose_name='Возможность оптимизации под RAID-масс.')

    class Meta:
        verbose_name = 'Накопитель'
        verbose_name_plural = 'Накопитель'


class MechanicsReliabilityHDDSpecifications(models.Model):
    """
    Механика и надежность
    """
    recording_technology = models.CharField(max_length=10, default='CMR', verbose_name='Технология записи')
    shock_resistance_wort = models.IntegerField(verbose_name='Ударность при падении', help_text='G')
    with_helium_filling = models.BooleanField(default=False, verbose_name='С гелиевым наполнением')

    class Meta:
        verbose_name = 'Механика и надежность'
        verbose_name_plural = 'Механика и надежность'


class DimensionsHDDSpecifications(models.Model):
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


class HDDSpecifications(models.Model):
    """
    Расширенные характеристики для HDD
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')
    factory_data = models.ForeignKey(
        FactoryDataHDDSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Заводские данные',
        related_name='+',
    )
    common_data = models.ForeignKey(
        CommonParametersHDDSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Общие данные',
    )
    storage_device = models.ForeignKey(
        StorageDeviceHDDSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Накопитель',
    )
    mechanics_reliability = models.ForeignKey(
        MechanicsReliabilityHDDSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Механика и надежность',
    )
    dimensions = models.ForeignKey(
        DimensionsHDDSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Габариты, вес',
    )

    def __str__(self):
        return f'Расширенные характеристики для HDD {self.product}'

    class Meta:
        verbose_name = 'Расширенные характеристики для HDD'
        verbose_name_plural = 'Расширенные характеристики для HDD'
        ordering = ['product', ]


