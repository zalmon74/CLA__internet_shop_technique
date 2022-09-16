from django.db import models

from ..products import Product


class FactoryDataRamSpecifications(models.Model):
    """
    Заводские данные
    """
    warranty = models.IntegerField(verbose_name='Страна-производитель')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Заводские данные для товара {self.product} категории "Оперативная память"'

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'
        ordering = ['product', ]


class CommonParametersRamSpecifications(models.Model):
    """
    Общие параметры
    """
    type = models.CharField(max_length=50, default='Оперативная память', verbose_name='Тип')
    model = models.CharField(max_length=50, verbose_name='Модель')
    manufacturer_code = models.CharField(max_length=50, verbose_name='Код производителя')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Общие параметры для товара {self.product} категории "Оперативная память"'

    class Meta:
        verbose_name = 'Общие параметры'
        verbose_name_plural = 'Общие параметры'
        ordering = ['product', ]


class CompositionRamSpecifications(models.Model):
    """
    Объем и состав комплекта
    """

    class FormFactorMemoryChoices(models.TextChoices):
        """
        Форм-фактор оперативной памяти
        """
        ddr = 'DDR DIMM'
        sdram = 'SDRAM DIMM'
        simm_72 = 'SIMM (72-pin)'
        sipp = 'SIPP'
        simm_30 = 'SIMM (30-pin)'

    class TypeMemoryChoices(models.TextChoices):
        ddr = 'DDR'
        ddr_2 = 'DDR2'
        ddr_3 = 'DDR3'
        ddr_4 = 'DDR4'
        ddr_5 = 'DDR5'

    type = models.CharField(max_length=10, choices=TypeMemoryChoices.choices, verbose_name='Тип памяти')
    form_factor = models.CharField(max_length=15, choices=FormFactorMemoryChoices.choices, verbose_name='Форм-фактор')
    one_memory_module = models.IntegerField(verbose_name='Объем одного модуля памяти', help_text='Гб')
    number_modules_included = models.IntegerField(verbose_name='Количество модулей в комплекте')
    register_memory = models.BooleanField(default=False, verbose_name='Регистровая память')
    ecc_memory = models.BooleanField(default=False, verbose_name='ECC-память')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Объем и состав комплекта для товара {self.product} категории "Оперативная память"'

    class Meta:
        verbose_name = 'Объем и состав комплекта'
        verbose_name_plural = 'Объем и состав комплекта'
        ordering = ['product', ]


class PerformanceRamSpecifications(models.Model):
    """
    Быстродействие
    """
    clock_frequency = models.IntegerField(verbose_name='Тактовая частота', help_text='МГц')
    xmp_profiles = models.CharField(max_length=25, verbose_name='Профили XMP')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Быстродействие для товара {self.product} категории "Оперативная память"'

    class Meta:
        verbose_name = 'Быстродействие'
        verbose_name_plural = 'Быстродействие'
        ordering = ['product', ]


class TimingsRamSpecifications(models.Model):
    """
    Тайминги
    """
    cl = models.IntegerField(verbose_name='CAS Latency (CL)')
    trcd = models.IntegerField(verbose_name='RAS to CAS Delay (tRCD)')
    trp = models.IntegerField(verbose_name='Row Precharge Delay (tRP)')
    tras = models.IntegerField(verbose_name='Activate to Precharge Delay (tRAS)')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Тайминги для товара {self.product} категории "Оперативная память"'

    class Meta:
        verbose_name = 'Тайминги'
        verbose_name_plural = 'Тайминги'
        ordering = ['product', ]


class DesignRamSpecifications(models.Model):
    """
    Конструкция
    """
    presence_radiator = models.BooleanField(default=False, verbose_name='Наличие радиатора')
    radiator_color = models.CharField(max_length=25, verbose_name='Цвет радиатора')
    illumination_board_elements = models.BooleanField(default=False, verbose_name='Подсветка элементов')
    height = models.IntegerField(verbose_name='Высота', help_text='мм.')
    low_profile = models.BooleanField(default=False, verbose_name='Низкопрофильная')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Конструкция для товара {self.product} категории "Оперативная память"'

    class Meta:
        verbose_name = 'Конструкция'
        verbose_name_plural = 'Конструкция'
        ordering = ['product', ]







