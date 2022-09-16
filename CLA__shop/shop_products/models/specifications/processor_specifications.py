from django.db import models

from ..products import Product


class FactoryDataProcessorSpecifications(models.Model):
    """
    Заводские данные
    """
    guarantee = models.IntegerField(verbose_name='Гарантия от производителя')
    producing_country = models.CharField(max_length=50, verbose_name='Страна производитель')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Заводские данные для товара {self.product} категории "Процессор"'

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'
        ordering = ['product', ]


class CommonParametersProcessorSpecifications(models.Model):
    """
    Стандартные параметры
    """

    model = models.CharField(
        max_length=50,
        unique=True,
        db_index=True,
        verbose_name='Модель процессора',
    )
    socket = models.CharField(max_length=50, verbose_name='Сокет', )
    manufacturer_code = models.CharField(max_length=50, verbose_name='Код производителя', )
    release_year = models.DateField(verbose_name='Дата производства')
    cooling_system = models.BooleanField(
        default=False,
        verbose_name='Система охлаждения',
        help_text='Наличие охлаждения в комплекте',
    )
    thermal_interface = models.BooleanField(
        default=False,
        verbose_name='Термоинтерфейс',
        help_text='Наличие термоинтерфейса в комплекте',
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Общие параметры для товара {self.product} категории "Процессор"'

    class Meta:
        verbose_name = 'Общие параметры'
        verbose_name_plural = 'Общие параметры'
        ordering = ['product', ]


class CoreArchitectureProcessorSpecifications(models.Model):
    """
    Ядро и архитектура процессора
    """

    count_cores = models.IntegerField(verbose_name='Количество ядер')
    maximum_threads = models.IntegerField(verbose_name='Количество потоков')
    number_performance = models.IntegerField(verbose_name='Количество производительных ядер')
    number_energy_efficient = models.IntegerField(verbose_name='Количество энергоэффективных ядер')
    l2_cache_size = models.IntegerField(verbose_name='Объем кэша L2')
    l3_cache_size = models.IntegerField(verbose_name='Объем кэша L3')
    process_technology = models.IntegerField(verbose_name='Техпроцесс')
    nucleus = models.CharField(max_length=50, verbose_name='Ядро', help_text='Название ядра')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Ядро и архитектура для товара {self.product} категории "Процессор"'

    class Meta:
        verbose_name = 'Ядро и архитектура процессора'
        verbose_name_plural = 'Ядра и архитектура процессора'
        ordering = ['product', ]


class FrequencyOverclockingProcessorSpecifications(models.Model):
    """
    Частота и возможность разгона
    """

    cpu_base_frequency = models.IntegerField(verbose_name='Базовая частота процессора', help_text='Гц')
    maximum_turbo_frequency = models.IntegerField(
        verbose_name='Максимальная частота процессора в турбо режиме',
        help_text='Гц',
    )
    base_frequency_efficient_cores = models.IntegerField(
        verbose_name='Базовая частота энергоэффективных ядер процессора',
        help_text='Гц',
    )
    turbo_frequency_efficient_cores = models.IntegerField(
        verbose_name='Максимальная частота энергоэффективных ядер процессора в турбо режиме',
        help_text='Гц',
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Частота и возможность разгона для товара {self.product} категории "Процессор"'

    class Meta:
        verbose_name = 'Частота и возможность разгона'
        verbose_name_plural = 'Частота и возможность разгона'
        ordering = ['product', ]


class RamOptionsProcessorSpecifications(models.Model):
    """
    Параметры оперативной памяти
    """
    memory_type = models.CharField(
        max_length=4,
        verbose_name='Тип оперативной памяти',
        help_text='Тип оперативной памяти, который поддерживает данный процессор'
    )
    maximum_supported_memory = models.IntegerField(
        verbose_name='Максимальный объем оперативной памяти',
        help_text='Максимальный объем оперативной памяти, который поддерживает данный процессор',
    )
    number_channels = models.IntegerField(
        verbose_name='Количество каналов',
        help_text='Количество каналов оперативной памяти, который поддерживает данный процессор',
    )
    maximum_ram_frequency = models.IntegerField(
        verbose_name='Максимальная частота',
        help_text='Максимальная частота оперативной памяти, который поддерживает данный процессор',
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Параметры оперативной памяти для товара {self.product} категории "Процессор"'

    class Meta:
        verbose_name = 'Параметры оперативной памяти'
        verbose_name_plural = 'Параметры оперативной памяти'
        ordering = ['product', ]


class ThermalCharacteristicsProcessorSpecifications(models.Model):
    """
    Тепловые характеристики
    """
    tdp = models.IntegerField(verbose_name='Тепловыделение (TDP)')
    base_heat_dissipation = models.IntegerField(verbose_name='Базовое тепловыделение')
    max_cpu_temperature = models.IntegerField(verbose_name='Максимальная температура процессора')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Тепловые характеристики для товара {self.product} категории "Процессор"'

    class Meta:
        verbose_name = 'Тепловые характеристики'
        verbose_name_plural = 'Тепловые характеристики'
        ordering = ['product', ]


class GraphicsCoreProcessorSpecifications(models.Model):
    """
    Графическое ядро
    """
    integrated_graphics_core = models.BooleanField(default=False, verbose_name='Встроенное графическое ядро')
    gpu_model = models.CharField(max_length=50, verbose_name='Модель графического ядра')
    maximum_frequency = models.IntegerField(verbose_name='Частота графического ядра', help_text='Гц')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Графическое ядро для товара {self.product} категории "Процессор"'

    class Meta:
        verbose_name = 'Графическое ядро'
        verbose_name_plural = 'Графические ядра'
        ordering = ['product', ]


class BusControllersProcessorSpecifications(models.Model):
    """
    Шина и контроллеры
    """
    integrated_pci_controller = models.CharField(max_length=50, verbose_name='Встроенный контроллер PCI Express')
    number_pci_lanes = models.IntegerField(verbose_name='Число линий PCI Express')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Шина и контроллеры для товара {self.product} категории "Процессор"'

    class Meta:
        verbose_name = 'Шина и контроллеры'
        verbose_name_plural = 'Шина и контроллеры'
        ordering = ['product', ]


