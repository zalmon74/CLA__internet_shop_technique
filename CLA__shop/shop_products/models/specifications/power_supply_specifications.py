from django.db import models

from ..products import Product


class FactoryDataPowerSupplySpecifications(models.Model):
    """
    Заводские данные
    """
    warranty = models.IntegerField(verbose_name='Гарантия от производителя')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Заводские данные для товара {self.product} категории "Блок питания"'

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'
        ordering = ['product', ]


class CommonParametersPowerSupplySpecifications(models.Model):
    """
    Общие параметры
    """
    type = models.CharField(max_length=50, default='Блок питания', verbose_name='Тип')
    model = models.CharField(max_length=50, verbose_name='Модель')
    manufacturer_code = models.CharField(max_length=50, verbose_name='Код производителя')
    power = models.IntegerField(verbose_name='Мощность', help_text='Вт')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Общие параметры для товара {self.product} категории "Блок питания"'

    class Meta:
        verbose_name = 'Общие параметры'
        verbose_name_plural = 'Общие параметры'
        ordering = ['product', ]


class AppearancePowerSupplySpecifications(models.Model):
    """
    Внешний вид
    """

    class FormFactorChoices(models.TextChoices):
        """
        Форм-фактор для блоков питания
        """
        atx = 'ATX'
        sfx = 'SFX'
        tfx = 'TFX'
        flex = 'FLEX'

    form_factor = models.CharField(max_length=10, choices=FormFactorChoices.choices, verbose_name='Форм-фактор')
    color = models.CharField(max_length=25, verbose_name='Цвет')
    datachable_cables = models.BooleanField(default=False, verbose_name='Отстегивающиеся провода')
    wire_braid = models.BooleanField(default=False, verbose_name='Наличие оплетки проводов')
    backlight_type = models.BooleanField(default=False, verbose_name='Тип подсветки')
    wire_colors = models.CharField(max_length=25, verbose_name='Цвет проводов')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Внешний вид для товара {self.product} категории "Блок питания"'

    class Meta:
        verbose_name = 'Внешний вид'
        verbose_name_plural = 'Внешний вид'
        ordering = ['product', ]


class CablesConnectorsPowerSupplySpecifications(models.Model):
    """
    Кабели и разъемы
    """
    main_power_connector = models.CharField(max_length=25, verbose_name='Основной разъем питания')
    processor_power = models.CharField(max_length=10, verbose_name='Разъемы питания для процессора')
    video_card_power = models.CharField(max_length=10, verbose_name='Разъемы питания для видеокарты')
    number_connectors_15pin_sata = models.IntegerField(verbose_name='Количество разъемов 15-pin SATA')
    number_4pin_molex = models.IntegerField(verbose_name='Количество разъемов 4-pin Molex')
    connector_4pin_floppy = models.BooleanField(default=False, verbose_name='Наличие кабеля питания для дисковода')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Кабели и разъемы для товара {self.product} категории "Блок питания"'

    class Meta:
        verbose_name = 'Кабели и разъемы'
        verbose_name_plural = 'Кабели и разъемы'
        ordering = ['product', ]


class ElectricalParametersPowerSupplySpecifications(models.Model):
    """
    Электрические параметры
    """
    current_plus_12 = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        verbose_name='Ток по линии +12 В',
        help_text='Вт',
    )
    current_3_3 = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        verbose_name='Ток по линии 3.3 В',
        help_text='Вт',
    )
    current_5 = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        verbose_name='Ток по линии 5 В',
        help_text='Вт',
    )
    standby_current = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        verbose_name='Ток дежурного источника (+5 В Standby)',
        help_text='Вт',
    )
    line_current_minus_12 = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        verbose_name='Ток по линии -12 В',
        help_text='Вт',
    )
    mains_input_voltage_range = models.CharField(
        max_length=25,
        default='100-240 В. 50/60 Гц',
        verbose_name='Диапазон входного напряжения сети',
        help_text='Вт',
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Электрические параметры для товара {self.product} категории "Блок питания"'

    class Meta:
        verbose_name = 'Электрические параметры'
        verbose_name_plural = 'Электрические параметры'
        ordering = ['product', ]


class CoolingSystemPowerSupplySpecifications(models.Model):
    """
    Система охлаждения
    """
    cooling_system = models.CharField(max_length=25, verbose_name='Система охлаждения')
    fan_dimensions = models.CharField(max_length=25, verbose_name='Размеры вентиляторов')
    speed_control = models.CharField(max_length=25, verbose_name='Регулировка оборотов вентиляторов')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Система охлаждения для товара {self.product} категории "Блок питания"'

    class Meta:
        verbose_name = 'Система охлаждения'
        verbose_name_plural = 'Система охлаждения'
        ordering = ['product', ]


class CertificationPowerSupplySpecifications(models.Model):
    """
    Сертификация
    """

    class Certificate80Choices(models.TextChoices):
        """
        Существующие сертификаты
        """
        plus = 'PLUS'
        bronze = 'Bronze'
        silver = 'Silver'
        gold = 'Gold'
        platinum = 'Platinum'
        titanium = 'Titanium'

    certificate_80_plus = models.CharField(
        max_length=8,
        choices=Certificate80Choices.choices,
        verbose_name='Сертификат 80 PLUS',
    )
    pfc = models.CharField(max_length=25, verbose_name='Корректор коэффициента мощности')
    protection_technologies = models.CharField(max_length=25, verbose_name='Технологии защиты')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Сертификация для товара {self.product} категории "Блок питания"'

    class Meta:
        verbose_name = 'Сертификация'
        verbose_name_plural = 'Сертификация'
        ordering = ['product', ]


class DimensionsWeightPowerSupplySpecifications(models.Model):
    """
    Габариты и вес
    """
    length = models.IntegerField(verbose_name='Длина', help_text='мм.')
    width = models.IntegerField(verbose_name='Ширина', help_text='мм.')
    height = models.IntegerField(verbose_name='Высота', help_text='мм.')
    weight = models.IntegerField(verbose_name='Вес', help_text='г.')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Габариты и вес для товара {self.product} категории "Блок питания"'

    class Meta:
        verbose_name = 'Габариты и вес'
        verbose_name_plural = 'Габариты и вес'
        ordering = ['product', ]
