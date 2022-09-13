from django.db import models

from ..products import Product


class FactoryDataRamSpecifications(models.Model):
    """
    Заводские данные
    """
    warranty = models.IntegerField(verbose_name='Страна-производитель')

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'


class CommonParametersRamSpecifications(models.Model):
    """
    Общие параметры
    """
    type = models.CharField(max_length=50, default='Оперативная память', verbose_name='Тип')
    model = models.CharField(max_length=50, verbose_name='Модель')
    manufacturer_code = models.CharField(max_length=50, verbose_name='Код производителя')

    class Meta:
        verbose_name = 'Общие параметры'
        verbose_name_plural = 'Общие параметры'


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
    number_modules_included = models.IntegerField(default=1, verbose_name='Количество модулей в комплекте')
    register_memory = models.BooleanField(default=False, verbose_name='Регистровая память')
    ecc_memory = models.BooleanField(default=False, verbose_name='ECC-память')

    class Meta:
        verbose_name = 'Объем и состав комплекта'
        verbose_name_plural = 'Объем и состав комплекта'


class PerformanceRamSpecifications(models.Model):
    """
    Быстродействие
    """
    clock_frequency = models.IntegerField(verbose_name='Тактовая частота', help_text='МГц')
    xmp_profiles = models.CharField(max_length=25, verbose_name='Профили XMP')

    class Meta:
        verbose_name = 'Быстродействие'
        verbose_name_plural = 'Быстродействие'


class TimingsRamSpecifications(models.Model):
    """
    Тайминги
    """
    cl = models.IntegerField(verbose_name='CAS Latency (CL)')
    trcd = models.IntegerField(verbose_name='RAS to CAS Delay (tRCD)')
    trp = models.IntegerField(verbose_name='Row Precharge Delay (tRP)')
    tras = models.IntegerField(verbose_name='Activate to Precharge Delay (tRAS)')

    class Meta:
        verbose_name = 'Тайминги'
        verbose_name_plural = 'Тайминги'


class DesignRamSpecifications(models.Model):
    """
    Конструкция
    """
    presence_radiator = models.BooleanField(default=False, verbose_name='Наличие радиатора')
    radiator_color = models.CharField(max_length=25, verbose_name='Цвет радиатора')
    illumination_board_elements = models.BooleanField(default=False, verbose_name='Подсветка элементов')
    height = models.IntegerField(verbose_name='Высота', help_text='мм.')
    low_profile = models.BooleanField(default=False, verbose_name='Низкопрофильная')

    class Meta:
        verbose_name = 'Конструкция'
        verbose_name_plural = 'Конструкция'


class RamSpecifications(models.Model):
    """
    Расширенные характеристики для оперативной памяти
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')
    factory_data = models.ForeignKey(
        FactoryDataRamSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Заводские данные',
        related_name='+',
    )
    common_parameters = models.ForeignKey(
        CommonParametersRamSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Общие данные',
    )
    composition = models.ForeignKey(
        FactoryDataRamSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Заводские данные',
    )
    performance = models.ForeignKey(
        PerformanceRamSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Быстродействие',
    )
    timings = models.ForeignKey(
        TimingsRamSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Тайминги',
    )
    design = models.ForeignKey(
        DesignRamSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Конструкция',
    )

    def __str__(self):
        return f'Расширенные характеристики оперативной памяти {self.product}'

    class Meta:
        verbose_name = 'Расширенные характеристики для оперативной памяти'
        verbose_name_plural = 'Расширенные характеристики для оперативной памяти'
        ordering = ['product', ]






