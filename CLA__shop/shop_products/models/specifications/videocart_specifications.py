from django.db import models

from ..products import Product


class FactoryDataVideoCartSpecifications(models.Model):
    """
    Заводские данные
    """
    warranty = models.IntegerField(verbose_name='Гарантия от производителя')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Заводские данные для товара {self.product} категории "Видеокарта"'

    class Meta:
        verbose_name = 'Заводские данные'
        verbose_name_plural = 'Заводские данные'
        ordering = ['product', ]


class CommonParametersVideoCartSpecifications(models.Model):
    """
    Общие параметры
    """
    type = models.CharField(max_length=25, default='Видеокарта', verbose_name='Тип')
    model = models.CharField(max_length=50, verbose_name='Модель', db_index=True)
    manufacturer_code = models.CharField(max_length=50, verbose_name='Код производителя')
    designed_mining = models.BooleanField(default=False, verbose_name='Предназначена для майнинга')
    lhr = models.BooleanField(default=False, verbose_name='LHR')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Общие параметры для товара {self.product} категории "Видеокарта"'

    class Meta:
        verbose_name = 'Общие параметры'
        verbose_name_plural = 'Общие параметры'
        ordering = ['product', ]


class MainParametersVideoCartSpecifications(models.Model):
    """
    Основные параметры
    """
    gpu = models.CharField(max_length=50, verbose_name='Графический процессор')
    microarchitecture = models.CharField(max_length=50, verbose_name='Миркроархитектура')
    technical_process = models.IntegerField(verbose_name='Техпроцесс')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Основные параметры для товара {self.product} категории "Видеокарта"'

    class Meta:
        verbose_name = 'Основные параметры'
        verbose_name_plural = 'Основные параметры'
        ordering = ['product', ]


class VideoMemoryVideoCartSpecifications(models.Model):
    """
    Спецификация видеопамяти
    """
    video_memory_size = models.IntegerField(verbose_name='Объем видеопамяти', help_text='Гб')
    memory_type = models.CharField(max_length=50, verbose_name='Тип памяти')
    memory_bus_width = models.IntegerField(verbose_name='Разрядность шины памяти', help_text='бит')
    maximum_memory_bandwidth = models.IntegerField(
        verbose_name='Максимальная пропускная способность памяти',
        help_text='Гбайт/сек',
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Спецификация видеопамяти для товара {self.product} категории "Видеокарта"'

    class Meta:
        verbose_name = 'Спецификация видеопамяти'
        verbose_name_plural = 'Спецификация видеопамяти'
        ordering = ['product', ]


class VideoProcessorVideoCartSpecifications(models.Model):
    """
    Спецификация видеопроцессора
    """
    nominal_frequency = models.IntegerField(verbose_name='Частота процессора', help_text='МГц')
    turbo_frequency = models.IntegerField(verbose_name='Турбочастота', help_text='МГц')
    number_universal_processors = models.IntegerField(verbose_name='Количество универсальных процессоров')
    number_texture_units = models.IntegerField(verbose_name='Число текстурных блоков')
    number_rasterization_blocks = models.IntegerField(verbose_name='Число блоков растеризации')
    ray_tracing_support = models.BooleanField(default=False, verbose_name='Поддержка трассировки лучей')
    hardware_accelerated_ray_tracing = models.IntegerField(verbose_name='Аппаратное ускорение трассировки лучей')
    tensor_cores = models.IntegerField(verbose_name='Тензорные ядра')
    shader_version = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Версия шейдеров')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Спецификация видеопроцессора для товара {self.product} категории "Видеокарта"'

    class Meta:
        verbose_name = 'Спецификация видеопроцессора'
        verbose_name_plural = 'Спецификация видеопроцессора'
        ordering = ['product', ]


class OutputImageVideoCartSpecifications(models.Model):
    """
    Вывод изображения
    """
    video_connectors = models.CharField(max_length=100, verbose_name='Видеоразъемы')
    hdmi_version = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Версия HDMI')
    display_port_version = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Версия DisplayPort')
    number_monitors = models.IntegerField(verbose_name='Количество подключаемых одновременно мониторов')
    maximum_resolution = models.CharField(max_length=25, verbose_name='Максимальное разрешение')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Вывод изображения для товара {self.product} категории "Видеокарта"'

    class Meta:
        verbose_name = 'Вывод изображения'
        verbose_name_plural = 'Вывод изображения'
        ordering = ['product', ]


class ConnectionVideoCartSpecifications(models.Model):
    """
    Подключение
    """
    interface = models.CharField(max_length=25, verbose_name='Интерфейс подключения')
    connector_form_factor = models.CharField(max_length=25, verbose_name='Форм-фактор разъема подключения')
    auxiliary_power_connectors = models.CharField(max_length=25, verbose_name='Разъемы дополнительного питания')
    recommended_power_supply = models.IntegerField(verbose_name='Рекомендуемый блок питания', help_text='Вт')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Подключение для товара {self.product} категории "Видеокарта"'

    class Meta:
        verbose_name = 'Подключение'
        verbose_name_plural = 'Подключение'
        ordering = ['product', ]


class CoolingSystemVideoCartSpecifications(models.Model):
    """
    Система охлаждения
    """
    cooling_type = models.CharField(max_length=25, verbose_name='Тип система охлаждения')
    number_installed_fans = models.IntegerField(verbose_name='Количество установленных вентиляторов')
    liquid_cooling_radiator = models.BooleanField(default=False, verbose_name='Радиатор жидкостного охлаждения')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Система охлаждения для товара {self.product} категории "Видеокарта"'

    class Meta:
        verbose_name = 'Система охлаждения'
        verbose_name_plural = 'Система охлаждения'
        ordering = ['product', ]


class DimensionsAndWightVideoCartSpecifications(models.Model):
    """
    Габариты и вес
    """
    low_profile = models.BooleanField(default=False, verbose_name='Низкопрофильная карта')
    number_occupied_expansion_slots = models.IntegerField(verbose_name='Количество занимаемых слотов расширения')
    length = models.IntegerField(verbose_name='Длина', help_text='мм.')
    thickness = models.IntegerField(verbose_name='Толщина', help_text='мм.')
    weight = models.IntegerField(verbose_name='Вес', help_text='г.')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')

    def __str__(self):
        return f'Габариты и вес для товара {self.product} категории "Видеокарта"'

    class Meta:
        verbose_name = 'Габариты и вес'
        verbose_name_plural = 'Габариты и вес'
        ordering = ['product', ]








