from django.db import models

from ..products import Product


class FactoryDataMotherboardSpecifications(models.Model):
    """
    Заводские данные
    """

    manufacturer_warranty = models.IntegerField(verbose_name='Гарантия от производителя')
    producing_country = models.CharField(max_length=100, verbose_name='Страна-производитель')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Заводские данные для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'
        ordering = ['product', ]


class CommonParametersMotherboardSpecifications(models.Model):
    """
    Общие параметры
    """

    type = models.CharField(max_length=50, default='Материнская плата', verbose_name='Тип')
    model = models.CharField(max_length=50, db_index=True, verbose_name='Модель')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Общие параметры для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Общие параметры'
        verbose_name_plural = 'Общие параметры'
        ordering = ['product', ]


class FormFactorDimensionsMotherboardSpecifications(models.Model):
    """
    Форм-фактор и размеры
    """

    class FormFactorChoices(models.TextChoices):
        """
        Значения для форм-фактора
        """
        eatx = 'EATX'
        atx = 'ATX'
        micro_atx = 'micro-ATX'
        mini_itx = 'mini-ITX'

    form_factor = models.CharField(max_length=10, choices=FormFactorChoices.choices, verbose_name='Форм-фактор')
    height = models.IntegerField(verbose_name='Высота', help_text='мм.')
    width = models.IntegerField(verbose_name='Ширина', help_text='мм.')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Форм-фактор и размеры для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Форм-фактор и размеры'
        verbose_name_plural = 'Форм-фактор и размеры'
        ordering = ['product', ]


class ProcessorChipsetMotherboardSpecifications(models.Model):
    """
    Процессор и чипсет
    """

    socket = models.CharField(max_length=50, verbose_name='Сокет')
    chipset = models.CharField(max_length=50, verbose_name='Чипсет')
    compatible_processor_cores = models.CharField(max_length=100, verbose_name='Совместимые ядра процессоров')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Процессор и чипсет для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Процессор и чипсет'
        verbose_name_plural = 'Процессор и чипсет'
        ordering = ['product', ]


class MemoryMotherboardSpecifications(models.Model):
    """
    Память
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

    class SupportedMemoryChoices(models.TextChoices):
        ddr = 'DDR'
        ddr_2 = 'DDR2'
        ddr_3 = 'DDR3'
        ddr_4 = 'DDR4'
        ddr_5 = 'DDR5'

    numbers_slot = models.IntegerField(verbose_name='Количество слотов поддерживаемой памяти')
    form_factor = models.CharField(
        max_length=15,
        choices=FormFactorMemoryChoices.choices,
        verbose_name='Форм фактор поддерживаемой памяти',
    )
    supported_memory = models.CharField(
        max_length=5,
        choices=SupportedMemoryChoices.choices,
        verbose_name='Тип поддерживаемой памяти',
    )
    number_channels = models.IntegerField(verbose_name='Количество каналов памяти')
    maximum_memory = models.IntegerField(verbose_name='Максимальный поддерживаемый объем памяти')
    maximum_memory_frequency = models.IntegerField(verbose_name='Максимальная частота памяти', help_text='Без разгона')
    frequency_overclocking = models.IntegerField(verbose_name='Максимальная частота памяти с учетом разгона')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Память для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Память'
        verbose_name_plural = 'Память'
        ordering = ['product', ]


class StorageControllersMotherboardSpecifications(models.Model):
    """
    Контроллеры накопителей
    """
    number_m2_connectors = models.IntegerField(verbose_name='Количество разъемов M2')
    m2_connectors = models.CharField(max_length=50, verbose_name='Разъемы M2')
    number_sata_ports = models.IntegerField(verbose_name='Количество разъемов SATA')
    sata_raid_mode = models.CharField(max_length=50, verbose_name='Режим работы SATA RAID')
    nvme_support = models.BooleanField(default=False, verbose_name='Поддержка NVMe')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Контроллеры накопителей для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Контроллеры накопителей'
        verbose_name_plural = 'Контроллеры накопителей'
        ordering = ['product', ]


class ExpansionSlotsMotherboardSpecifications(models.Model):
    """
    Слоты расширения
    """
    pci_express_version = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Версия PCI Express')
    number_x16_slots = models.IntegerField(verbose_name='Количество слотов PCI-E x16')
    sli_crossfire_support = models.CharField(max_length=25, verbose_name='Поддержка SLI/Crossfire')
    number_cards_sli = models.IntegerField(verbose_name='Количество карт в SLI/Crossfire', help_text='шт.')
    number_x1_slots = models.IntegerField(verbose_name='Количество слотов PCI-E x1')
    other_expansions_slots = models.CharField(max_length=100, verbose_name='Поддержка других слотов')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Слоты расширения для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Слоты расширения'
        verbose_name_plural = 'Слоты расширения'
        ordering = ['product', ]


class BackPanelMotherboardSpecifications(models.Model):
    """
    Задняя панель
    """
    number_type_usb = models.CharField(max_length=100, verbose_name='Количество и тип USB на задней панели')
    video_outputs = models.CharField(max_length=50, verbose_name='Видеовыходы')
    number_network_ports = models.IntegerField(verbose_name='Количество сетевых портов (RJ-45)')
    number_analog_audio = models.IntegerField(verbose_name='Количество аналоговых аудио разъемов')
    digital_audio_ports = models.CharField(max_length=50, verbose_name='Цифровые аудио порты (S/PDIF)')
    other_connectors = models.CharField(max_length=150, verbose_name='Другие разъемы на задней панели')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Задняя панель для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Задняя панель'
        verbose_name_plural = 'Задняя панель'
        ordering = ['product', ]


class InternalConnectorsMotherboardSpecifications(models.Model):
    """
    Внутренние коннекторы
    """
    internal_usb_connectors = models.CharField(max_length=100, verbose_name='Внутренние коннекторы USB на плате')
    cpu_cooler_power = models.CharField(max_length=50, verbose_name='Разъем питания процессорного кулера')
    pin_pwm_fan_4 = models.IntegerField(verbose_name='4-Pin PWM коннекторы для вентиляторов')
    pin_fan_3 = models.IntegerField(verbose_name='3-Pin коннекторы для вентиляторов')
    pin_led_3 = models.IntegerField(verbose_name='Разъем светодиодов 3-Pin (+5V-D-G)')
    pin_led_4 = models.IntegerField(verbose_name='Разъем светодиодов 4-Pin (+12V-G-R-B)')
    m2_e_key = models.BooleanField(default=False, verbose_name='M.2 ключ Е')
    lpt_interface = models.BooleanField(default=False, verbose_name='Интерфейс LPT')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Внутренние коннекторы для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Внутренние коннекторы'
        verbose_name_plural = 'Внутренние коннекторы'
        ordering = ['product', ]


class AudioMotherboardSpecifications(models.Model):
    """
    Аудио
    """
    sound_scheme = models.CharField(max_length=10, verbose_name='Звуковая схема')
    audio_adapter = models.CharField(max_length=50, verbose_name='Чипсет звукового адаптера')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Аудио для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио'
        ordering = ['product', ]


class NetMotherboardSpecifications(models.Model):
    """
    Сеть
    """
    network_adapter_speed = models.IntegerField(verbose_name='Скорость сетевого адаптера', help_text='Гбит/с')
    network_adapter_chipset = models.CharField(max_length=50, verbose_name='Чипсет сетевого адаптера')
    wifi_adapter = models.CharField(max_length=50, verbose_name='Встроенный адаптер Wi-Fi')
    wifi_controller = models.CharField(max_length=50, verbose_name='Контроллер Wi-Fi')
    bluetooth = models.CharField(max_length=25, verbose_name='Bluetooth')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Сеть для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Сеть'
        ordering = ['product', ]


class CoolingPowerMotherboardSpecifications(models.Model):
    """
    Охлаждение и питание
    """
    main_power_connector = models.CharField(max_length=10, verbose_name='Основной разъем питания')
    cpu_power_connector = models.CharField(max_length=10, verbose_name='Разъем питания процессора')
    number_power_phases = models.IntegerField(verbose_name='Количество фаз питания')
    passive_cooling = models.BooleanField(default=False, verbose_name='Пассивное охлаждение')
    active_cooling = models.BooleanField(default=False, verbose_name='Активное охлаждение')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Охлаждение и питание для товара {self.product} категории "Материнская плата"'

    class Meta:
        verbose_name = 'Охлаждение и питание'
        verbose_name_plural = 'Охлаждение и питание'
        ordering = ['product', ]





