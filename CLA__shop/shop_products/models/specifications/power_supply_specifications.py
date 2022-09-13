from django.db import models

from ..products import Product


class FactoryDataPowerSupplySpecifications(models.Model):
    """
    Заводские данные
    """
    warranty = models.IntegerField(verbose_name='Гарантия от производителя')

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'


class CommonParametersPowerSupplySpecifications(models.Model):
    """
    Общие параметры
    """
    type = models.CharField(max_length=50, default='Блок питания', verbose_name='Тип')
    model = models.CharField(max_length=50, verbose_name='Модель')
    manufacturer_code = models.CharField(max_length=50, verbose_name='Код производителя')
    power = models.IntegerField(verbose_name='Мощность', help_text='Вт')

    class Meta:
        verbose_name = 'Общие параметры'
        verbose_name_plural = 'Общие параметры'


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

    class Meta:
        verbose_name = 'Внешний вид'
        verbose_name_plural = 'Внешний вид'


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

    class Meta:
        verbose_name = 'Кабели и разъемы'
        verbose_name_plural = 'Кабели и разъемы'


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

    class Meta:
        verbose_name = 'Электрические параметры'
        verbose_name_plural = 'Электрические параметры'


class CoolingSystemPowerSupplySpecifications(models.Model):
    """
    Система охлаждения
    """
    cooling_system = models.CharField(max_length=25, verbose_name='Система охлаждения')
    fan_dimensions = models.CharField(max_length=25, verbose_name='Размеры вентиляторов')
    speed_control = models.CharField(max_length=25, verbose_name='Регулировка оборотов вентиляторов')

    class Meta:
        verbose_name = 'Система охлаждения'
        verbose_name_plural = 'Система охлаждения'


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

    class Meta:
        verbose_name = 'Сертификация'
        verbose_name_plural = 'Сертификация'


class DimensionsWeightPowerSupplySpecifications(models.Model):
    """
    Габариты и вес
    """
    length = models.IntegerField(verbose_name='Длина', help_text='мм.')
    width = models.IntegerField(verbose_name='Ширина', help_text='мм.')
    height = models.IntegerField(verbose_name='Высота', help_text='мм.')
    weight = models.IntegerField(verbose_name='Вес', help_text='г.')

    class Meta:
        verbose_name = 'Габариты и вес'
        verbose_name_plural = 'Габариты и вес'


class PowerSupplySpecifications(models.Model):
    """
    Расширенные характеристики для блоков питания
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')
    factory_data = models.ForeignKey(
        FactoryDataPowerSupplySpecifications,
        on_delete=models.CASCADE,
        verbose_name='Заводские данные',
    )
    common_parameters = models.ForeignKey(
        CommonParametersPowerSupplySpecifications,
        on_delete=models.CASCADE,
        verbose_name='Общие данные',
    )
    appearance = models.ForeignKey(
        AppearancePowerSupplySpecifications,
        on_delete=models.CASCADE,
        verbose_name='Внешний вид',
    )
    cables_connectors = models.ForeignKey(
        CablesConnectorsPowerSupplySpecifications,
        on_delete=models.CASCADE,
        verbose_name='Кабели и разъемы',
    )
    electrical_parameters = models.ForeignKey(
        ElectricalParametersPowerSupplySpecifications,
        on_delete=models.CASCADE,
        verbose_name='Электрические параметры',
    )
    cooling_system = models.ForeignKey(
        CoolingSystemPowerSupplySpecifications,
        on_delete=models.CASCADE,
        verbose_name='Система охлаждения',
    )
    certifications = models.ForeignKey(
        CertificationPowerSupplySpecifications,
        on_delete=models.CASCADE,
        verbose_name='Сертификация',
    )
    dimensions_weight = models.ForeignKey(
        ElectricalParametersPowerSupplySpecifications,
        on_delete=models.CASCADE,
        verbose_name='Габариты и вес',
        related_name='+',
    )

    def __str__(self):
        return f'Расширенные характеристики блока питания {self.product}'

    class Meta:
        verbose_name = 'Расширенные характеристики для блоков питания'
        verbose_name_plural = 'Расширенные характеристики для блоков питания'
        ordering = ['product', ]

















