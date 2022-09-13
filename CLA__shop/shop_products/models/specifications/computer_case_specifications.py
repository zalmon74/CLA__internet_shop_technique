from django.db import models

from ..products import Product


class FactoryDataComputerCaseSpecifications(models.Model):
    """
    Заводские данные
    """
    warranty = models.IntegerField(verbose_name='Гарантия от производителя')

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'


class CommonParametersComputerCaseSpecifications(models.Model):
    """
    Общие параметры
    """
    type = models.CharField(max_length=25, default='Корпус', verbose_name='Тип')
    model = models.CharField(max_length=25, verbose_name='Модель')
    manufacturer_code = models.CharField(max_length=25, verbose_name='Код производителя')

    class Meta:
        verbose_name = 'Общие параметры'
        verbose_name_plural = 'Общие параметры'


class FormFactorComputerCaseSpecifications(models.Model):
    """
    Форм-фактор и габариты
    """

    class MotherBoardOrientationChoices(models.TextChoices):
        """
        Выбор ориентации материнской платы
        """
        horizontal = 'Горизонтально'
        vertical = 'Вертикально'

    frame_size = models.CharField(max_length=25, verbose_name='Типоразмер корпуса')
    motherboard_orientation = models.CharField(
        max_length=13,
        choices=MotherBoardOrientationChoices.choices,
        verbose_name='Ориентация материнской платы',
    )
    length = models.IntegerField(verbose_name='Длина', help_text='мм.')
    width = models.IntegerField(verbose_name='Ширина', help_text='мм.')
    height = models.IntegerField(verbose_name='Высота', help_text='мм.')
    weight = models.IntegerField(verbose_name='Вес', help_text='г.')

    class Meta:
        verbose_name = 'Форм-фактор и габариты'
        verbose_name_plural = 'Форм-фактор и габариты'


class AppearanceComputerCaseSpecifications(models.Model):
    """
    Внешний вид
    """

    class BacklightColorChoices(models.TextChoices):
        """
        Типы подсветки корпусов
        """
        led = 'LED'
        rgb = 'RGB'
        argb = 'ARGB'
        drgb = 'DRGB'
        frgb = 'FRGB'

    main_color = models.CharField(max_length=25, verbose_name='Основной цвет')
    housing_material = models.CharField(max_length=25, verbose_name='Материал корпуса')
    metal_thickness = models.IntegerField(verbose_name='Толщина метала')
    window_side_wall = models.BooleanField(default=False, verbose_name='Наличие окна на боковой стенки')
    window_material = models.CharField(max_length=25, verbose_name='Материал окна')
    front_panel_material = models.CharField(max_length=25, verbose_name='Материал на передней панели')
    backlight_type = models.CharField(
        max_length=10,
        choices=BacklightColorChoices.choices,
        verbose_name='Тип подсветки',
    )
    backlight_color = models.CharField(max_length=25, verbose_name='Цвет подсветки')
    backlight_source = models.CharField(max_length=10, verbose_name='Источник подсветки')

    class Meta:
        verbose_name = 'Внешний вид'
        verbose_name_plural = 'Внешний вид'


class CompatibilityComputerCaseSpecifications(models.Model):
    """
    Совместимость
    """

    class PlacementPowerSupplyChoices(models.TextChoices):
        """
        Расположение блока питания
        """
        up = 'Верхнее'
        down = 'Нижнее'

    compatible_board_form_factor = models.CharField(max_length=50, verbose_name='Форм-фактор совместимых плат')
    form_factor_compatible_power_supplies = models.CharField(
        max_length=50,
        verbose_name='Форм фактор совместимых блоков питания',
    )
    placement_power_supply = models.CharField(
        max_length=7,
        choices=PlacementPowerSupplyChoices.choices,
        verbose_name='Расположение блока питания',
    )
    horizontal_expansion_slots = models.IntegerField(verbose_name='Горизонтальные слоты расширения')
    vertical_expansion_slots = models.IntegerField(verbose_name='Вертикальные слоты расширения')
    max_length_installed_video_card = models.IntegerField(
        verbose_name='Максимальная длина устанавливаемой видеокарты',
        help_text='мм.',
    )
    max_cpu_cooler_height = models.IntegerField(
        verbose_name='Максимальная высота устанавливаемого кулера',
        help_text='мм.',
    )
    number_2_5_drive_bays = models.IntegerField(verbose_name='Количество отсеков 2.5\" накопителей', help_text='шт')
    number_internal_3_5_bays = models.IntegerField(verbose_name='Количество внутренних отсеков 3.5\" ', help_text='шт')
    number_external_3_5_bays = models.IntegerField(verbose_name='Количество внешних отсеков 3.5\" ', help_text='шт')
    number_bays_5_25 = models.IntegerField(verbose_name='Число отсеков 5.25\"', help_text='шт')

    class Meta:
        verbose_name = 'Совместимость'
        verbose_name_plural = 'Совместимость'


class CoolingComputerCaseSpecifications(models.Model):
    """
    Охлаждение
    """
    fans_included = models.BooleanField(default=False, verbose_name='Наличие вентиляторов в комплекте')
    front_fan_support = models.CharField(max_length=25, verbose_name='Поддержка фронтальных вентиляторов')
    rear_fan_support = models.CharField(max_length=25, verbose_name='Поддержка тыловых вентиляторов')
    top_fan_support = models.CharField(max_length=25, verbose_name='Поддержка верхних вентиляторов')
    bottom_fan_support = models.CharField(max_length=25, verbose_name='Поддержка нижних вентиляторов')
    side_fan_support = models.CharField(max_length=25, verbose_name='Поддержка боковых вентиляторов')
    installing_liquid_cooling_system = models.BooleanField(
        default=False,
        verbose_name='Возможно установки системы жидкостного охлаждения',
    )
    rear_mounting_dimension_radiator = models.CharField(
        max_length=25,
        verbose_name='Тыловой монтажный размер радиатора СВО'
    )
    side_mounting_dimension_radiator = models.CharField(
        max_length=25,
        verbose_name='Боковой монтажный размер радиатора СВО'
    )

    class Meta:
        verbose_name = 'Охлаждение'
        verbose_name_plural = 'Охлаждение'


class FrontPanelConnectorsComputerCaseSpecifications(models.Model):
    """
    Разъемы и интерфейсы лицевой панели
    """
    io_panel_layout = models.CharField(max_length=7, default='Спереди', verbose_name='Расположение I/O панели')
    connectors = models.CharField(max_length=100, verbose_name='Разъемы')
    built_card_reader = models.BooleanField(default=False, verbose_name='Наличие кард-ридера')

    class Meta:
        verbose_name = 'Разъемы и интерфейсы лицевой панели'
        verbose_name_plural = 'Разъемы и интерфейсы лицевой панели'


class ServiceComputerCaseSpecifications(models.Model):
    """
    Обслуживание
    """
    fixing_side_panels = models.CharField(max_length=10, default='Сбоку', verbose_name='Фиксация боковых панелей')
    cutout_area_mounting_cpu_cooler = models.BooleanField(default=False, verbose_name='Вырез в районе крепления кулера')
    rear_cable_routing = models.BooleanField(default=False, verbose_name='Прокладка кабелей за задней стенкой')
    dust_filter = models.BooleanField(default=False, verbose_name='Пылевой фильтр')

    class Meta:
        verbose_name = 'Обслуживание'
        verbose_name_plural = 'Обслуживание'


class ComputerCaseSpecifications(models.Model):
    """
    Расширенные характеристики для корпуса
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')
    factory_data = models.ForeignKey(
        FactoryDataComputerCaseSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Заводские данные',
        related_name='+',
    )
    common_data = models.ForeignKey(
        CommonParametersComputerCaseSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Общие данные',
    )
    form_factor = models.ForeignKey(
        FormFactorComputerCaseSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Форм-фактор и габариты',
    )
    appearance = models.ForeignKey(
        AppearanceComputerCaseSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Внешний вид',
    )
    compatibility = models.ForeignKey(
        CompatibilityComputerCaseSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Совместимость',
    )
    cooling = models.ForeignKey(
        CoolingComputerCaseSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Охлаждение',
    )
    front_panel_connector = models.ForeignKey(
        FrontPanelConnectorsComputerCaseSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Разъемы и интерфейсы лицевой панели',
    )
    service = models.ForeignKey(
        ServiceComputerCaseSpecifications,
        on_delete=models.CASCADE,
        verbose_name='Обслуживание',
    )

    def __str__(self):
        return f'Расширенные характеристики для корпуса {self.product}'

    class Meta:
        verbose_name = 'Расширенные характеристики для корпуса'
        verbose_name_plural = 'Расширенные характеристики для корпуса'
        ordering = ['product', ]








