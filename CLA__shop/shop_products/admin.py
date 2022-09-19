from django.contrib import admin

from django.utils.safestring import mark_safe

from admin_numeric_filter.admin import RangeNumericFilter, NumericFilterModelAdmin

from .models import *


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):

    def get_html_photo(self, object_):
        if object_.photo:
            return mark_safe(f'<img src="{object_.photo.url}" width=100>')

    list_display = ('id', 'name', 'get_html_photo', )
    list_display_links = ('name', 'get_html_photo')

    fields = ('id', 'name', 'photo', 'get_html_photo', )
    readonly_fields = ('id', 'get_html_photo', )

    search_fields = ('name', )

    get_html_photo.short_description = 'Фото'


@admin.register(BrandProduct)
class BrandProductAdmin(admin.ModelAdmin):

    def get_html_photo(self, object_):
        if object_.photo:
            return mark_safe(f'<img src="{object_.photo.url}" width=100>')

    list_display = ('id', 'name', 'get_html_photo', 'email', 'show')
    list_display_links = ('name', 'get_html_photo', 'email')

    fields = ('id', 'name', 'photo', 'get_html_photo', 'email', 'categories', 'description', 'show')
    readonly_fields = ('id', 'get_html_photo')

    search_fields = ('name', 'categories')
    list_filter = ('categories', 'show', )

    list_editable = ('show', )


class ProductPhotoInline(admin.StackedInline):
    model = PhotoProduct
    verbose_name = 'Фото товара'
    verbose_name_plural = 'Фото товаров'


# Инлайны для категории "Корпус"

class FactoryDataComputerCaseSpecificationsInline(admin.StackedInline):
    model = FactoryDataComputerCaseSpecifications
    verbose_name = 'Заводские данные для товара категории "Корпус"'
    verbose_name_plural = 'Заводские данные для товара категории "Корпус"'


class CommonParametersComputerCaseSpecificationsInline(admin.StackedInline):
    model = CommonParametersComputerCaseSpecifications
    verbose_name = 'Общие данные для товара категории "Корпус"'
    verbose_name_plural = 'Общие данные для товара категории "Корпус"'


class FormFactorComputerCaseSpecificationsInline(admin.StackedInline):
    model = FormFactorComputerCaseSpecifications
    verbose_name = 'Форм-фактор и габариты товара для категории "Корпус"'
    verbose_name_plural = 'Форм-фактор и габариты товара для категории "Корпус"'


class AppearanceComputerCaseSpecificationsInline(admin.StackedInline):
    model = AppearanceComputerCaseSpecifications
    verbose_name = 'Внешний вид для товара категории "Корпус"'
    verbose_name_plural = 'Внешний вид для товара категории "Корпус"'


class CompatibilityComputerCaseSpecificationsInline(admin.StackedInline):
    model = CompatibilityComputerCaseSpecifications
    verbose_name = 'Совместимость для товара категории "Корпус"'
    verbose_name_plural = 'Совместимость для товара категории "Корпус"'


class CoolingComputerCaseSpecificationsInline(admin.StackedInline):
    model = CoolingComputerCaseSpecifications
    verbose_name = 'Охлаждение для товара категории "Корпус"'
    verbose_name_plural = 'Охлаждение для товара категории "Корпус"'


class FrontPanelConnectorsComputerCaseSpecificationsInline(admin.StackedInline):
    model = FrontPanelConnectorsComputerCaseSpecifications
    verbose_name = 'Разъемы и интерфейсы лицевой панели для товара категории "Корпус"'
    verbose_name_plural = 'Разъемы и интерфейсы лицевой панели для товара категории "Корпус"'


class ServiceComputerCaseSpecificationsInline(admin.StackedInline):
    model = ServiceComputerCaseSpecifications
    verbose_name = 'Обслуживание для товара категории "Корпус"'
    verbose_name_plural = 'Обслуживание для товара категории "Корпус"'


# Инлайны для категории "Кулер"

class FactoryDataCoolerSpecificationsInline(admin.StackedInline):
    model = FactoryDataCoolerSpecifications
    verbose_name = 'Заводские данные для товара категории "Кулер"'
    verbose_name_plural = 'Заводские данные для товара категории "Кулер"'


class CommonParametersCoolerSpecifications(admin.StackedInline):
    model = CommonParametersCoolerSpecifications
    verbose_name = 'Общие данные для товара категории "Кулер"'
    verbose_name_plural = 'Общие данные для товара категории "Кулер"'


class RadiatorCoolerSpecificationsInline(admin.StackedInline):
    model = RadiatorCoolerSpecifications
    verbose_name = 'Радиатор для товара категории "Кулер"'
    verbose_name_plural = 'Радиатор для товара категории "Кулер"'


class FanCoolerSpecificationsInline(admin.StackedInline):
    model = FanCoolerSpecifications
    verbose_name = 'Вентилятор для товара категории "Кулер"'
    verbose_name_plural = 'Вентилятор для товара категории "Кулер"'


class DimensionsCoolerSpecificationsInline(admin.StackedInline):
    model = DimensionsCoolerSpecifications
    verbose_name = 'Габариты для товара категории "Кулер"'
    verbose_name_plural = 'Габариты для товара категории "Кулер"'


# Инлайны для категории "Жесткие диски"

class FactoryDataHDDSpecificationsInline(admin.StackedInline):
    model = FactoryDataHDDSpecifications
    verbose_name = 'Заводские параметры для товара категории "Жесткие диски"'
    verbose_name_plural = 'Заводские параметры для товара категории "Жесткие диски"'


class CommonParametersHDDSpecificationsInline(admin.StackedInline):
    model = CommonParametersHDDSpecifications
    verbose_name = 'Общие параметры для товара категории "Жесткие диски"'
    verbose_name_plural = 'Общие параметры для товара категории "Жесткие диски"'


class StorageDeviceHDDSpecificationsInline(admin.StackedInline):
    model = StorageDeviceHDDSpecifications
    verbose_name = 'Накопитель для товара категории "Жесткие диски"'
    verbose_name_plural = 'Накопитель для товара категории "Жесткие диски"'


class MechanicsReliabilityHDDSpecificationsInline(admin.StackedInline):
    model = MechanicsReliabilityHDDSpecifications
    verbose_name = 'Механика и надежность для товара категории "Жесткие диски"'
    verbose_name_plural = 'Механика и надежность для товара категории "Жесткие диски"'


class DimensionsHDDSpecificationsInline(admin.StackedInline):
    model = DimensionsHDDSpecifications
    verbose_name = 'Габариты, вес для товара категории "Жесткие диски"'
    verbose_name_plural = 'Габариты, вес для товара категории "Жесткие диски"'


# Инлайны для категории "Материнская плата"

class FactoryDataMotherboardSpecificationsInline(admin.StackedInline):
    model = FactoryDataMotherboardSpecifications
    verbose_name = 'Заводские данные для товара категории "Материнская плата"'
    verbose_name_plural = 'Заводские данные для товара категории "Материнская плата"'


class CommonParametersMotherboardSpecificationsInline(admin.StackedInline):
    model = CommonParametersMotherboardSpecifications
    verbose_name = 'Общие параметры для товара категории "Материнская плата"'
    verbose_name_plural = 'Общие параметры для товара категории "Материнская плата"'


class FormFactorDimensionsMotherboardSpecificationsInline(admin.StackedInline):
    model = FormFactorDimensionsMotherboardSpecifications
    verbose_name = 'Форм-фактор и размеры для товара категории "Материнская плата"'
    verbose_name_plural = 'Форм-фактор и размеры для товара категории "Материнская плата"'


class ProcessorChipsetMotherboardSpecificationsInline(admin.StackedInline):
    model = ProcessorChipsetMotherboardSpecifications
    verbose_name = 'Процессор и чипсет для товара категории "Материнская плата"'
    verbose_name_plural = 'Процессор и чипсет для товара категории "Материнская плата"'


class MemoryMotherboardSpecificationsInline(admin.StackedInline):
    model = MemoryMotherboardSpecifications
    verbose_name = 'Память для товара категории "Материнская плата"'
    verbose_name_plural = 'Память для товара категории "Материнская плата"'


class StorageControllersMotherboardSpecificationsInline(admin.StackedInline):
    model = StorageControllersMotherboardSpecifications
    verbose_name = 'Контроллеры накопителей для товара категории "Материнская плата"'
    verbose_name_plural = 'Контроллеры накопителей для товара категории "Материнская плата"'


class ExpansionSlotsMotherboardSpecificationsInline(admin.StackedInline):
    model = ExpansionSlotsMotherboardSpecifications
    verbose_name = 'Слоты расширения для товара категории "Материнская плата"'
    verbose_name_plural = 'Слоты расширения для товара категории "Материнская плата"'


class BackPanelMotherboardSpecificationsInline(admin.StackedInline):
    model = BackPanelMotherboardSpecifications
    verbose_name = 'Задняя панель для товара категории "Материнская плата"'
    verbose_name_plural = 'Задняя панель для товара категории "Материнская плата"'


class InternalConnectorsMotherboardSpecificationsInline(admin.StackedInline):
    model = InternalConnectorsMotherboardSpecifications
    verbose_name = 'Внутренние коннекторы для товара категории "Материнская плата"'
    verbose_name_plural = 'Внутренние коннекторы для товара категории "Материнская плата"'


class AudioMotherboardSpecificationsInline(admin.StackedInline):
    model = AudioMotherboardSpecifications
    verbose_name = 'Аудио для товара категории "Материнская плата"'
    verbose_name_plural = 'Аудио для товара категории "Материнская плата"'


class NetMotherboardSpecificationsInline(admin.StackedInline):
    model = NetMotherboardSpecifications
    verbose_name = 'Сеть для товара категории "Материнская плата"'
    verbose_name_plural = 'Сеть для товара категории "Материнская плата"'


class CoolingPowerMotherboardSpecificationsInline(admin.StackedInline):
    model = CoolingPowerMotherboardSpecifications
    verbose_name = 'Охлаждение и питание для товара категории "Материнская плата"'
    verbose_name_plural = 'Охлаждение и питание для товара категории "Материнская плата"'


# Инлайны для категории "Блок питания"

class FactoryDataPowerSupplySpecificationsInline(admin.StackedInline):
    model = FactoryDataPowerSupplySpecifications
    verbose_name = 'Заводские данные для товара категории "Блок питания"'
    verbose_name_plural = 'Заводские данные для товара категории "Блок питания"'


class CommonParametersPowerSupplySpecificationsInline(admin.StackedInline):
    model = CommonParametersPowerSupplySpecifications
    verbose_name = 'Общие параметры для товара категории "Блок питания"'
    verbose_name_plural = 'Общие параметры для товара категории "Блок питания"'


class AppearancePowerSupplySpecificationsInline(admin.StackedInline):
    model = AppearancePowerSupplySpecifications
    verbose_name = 'Внешний вид для товара категории "Блок питания"'
    verbose_name_plural = 'Внешний вид для товара категории "Блок питания"'


class CablesConnectorsPowerSupplySpecificationsInline(admin.StackedInline):
    model = CablesConnectorsPowerSupplySpecifications
    verbose_name = 'Кабели и разъемы для товара категории "Блок питания"'
    verbose_name_plural = 'Кабели и разъемы для товара категории "Блок питания"'


class ElectricalParametersPowerSupplySpecificationsInline(admin.StackedInline):
    model = ElectricalParametersPowerSupplySpecifications
    verbose_name = 'Электрические параметры для товара категории "Блок питания"'
    verbose_name_plural = 'Электрические параметры для товара категории "Блок питания"'


class CoolingSystemPowerSupplySpecificationsInline(admin.StackedInline):
    model = CoolingSystemPowerSupplySpecifications
    verbose_name = 'Система охлаждения для товара категории "Блок питания"'
    verbose_name_plural = 'Система охлаждения для товара категории "Блок питания"'


class CertificationPowerSupplySpecificationsInline(admin.StackedInline):
    model = CertificationPowerSupplySpecifications
    verbose_name = 'Сертификация для товара категории "Блок питания"'
    verbose_name_plural = 'Сертификация для товара категории "Блок питания"'


class DimensionsWeightPowerSupplySpecificationsInline(admin.StackedInline):
    model = DimensionsWeightPowerSupplySpecifications
    verbose_name = 'Габариты и вес для товара категории "Блок питания"'
    verbose_name_plural = 'Габариты и вес для товара категории "Блок питания"'


# Инлайны для категории "Процессор"

class FactoryDataProcessorSpecificationsInline(admin.StackedInline):
    model = FactoryDataProcessorSpecifications
    verbose_name = 'Заводские данные для товара категории "Процессор"'
    verbose_name_plural = 'Заводские данные для товара категории "Процессор"'


class CommonParametersProcessorSpecificationsInline(admin.StackedInline):
    model = CommonParametersProcessorSpecifications
    verbose_name = 'Стандартные параметры для товара категории "Процессор"'
    verbose_name_plural = 'Стандартные параметры для товара категории "Процессор"'


class CoreArchitectureProcessorSpecificationsInline(admin.StackedInline):
    model = CoreArchitectureProcessorSpecifications
    verbose_name = 'Ядро и архитектура процессора для товара категории "Процессор"'
    verbose_name_plural = 'Ядро и архитектура процессора для товара категории "Процессор"'


class FrequencyOverclockingProcessorSpecificationsInline(admin.StackedInline):
    model = FrequencyOverclockingProcessorSpecifications
    verbose_name = 'Частота и возможность разгона для товара категории "Процессор"'
    verbose_name_plural = 'Частота и возможность разгона для товара категории "Процессор"'


class RamOptionsProcessorSpecifications(admin.StackedInline):
    model = RamOptionsProcessorSpecifications
    verbose_name = 'Параметры оперативной памяти для товара категории "Процессор"'
    verbose_name_plural = 'Параметры оперативной памяти для товара категории "Процессор"'


class ThermalCharacteristicsProcessorSpecificationsInline(admin.StackedInline):
    model = ThermalCharacteristicsProcessorSpecifications
    verbose_name = 'Тепловые характеристики для товара категории "Процессор"'
    verbose_name_plural = 'Тепловые характеристики для товара категории "Процессор"'


class GraphicsCoreProcessorSpecificationsInline(admin.StackedInline):
    model = GraphicsCoreProcessorSpecifications
    verbose_name = 'Графическое ядро для товара категории "Процессор"'
    verbose_name_plural = 'Графическое ядро для товара категории "Процессор"'


class BusControllersProcessorSpecificationsInline(admin.StackedInline):
    model = BusControllersProcessorSpecifications
    verbose_name = 'Шина и контроллеры для товара категории "Процессор"'
    verbose_name_plural = 'Шина и контроллеры для товара категории "Процессор"'


# Инлайны для категории "Оперативная память"

class FactoryDataRamSpecificationsInline(admin.StackedInline):
    model = FactoryDataRamSpecifications
    verbose_name = 'Заводские данные для товара категории "Оперативная память"'
    verbose_name_plural = 'Заводские данные для товара категории "Оперативная память"'


class CommonParametersRamSpecificationsInline(admin.StackedInline):
    model = CommonParametersRamSpecifications
    verbose_name = 'Общие параметры для товара категории "Оперативная память"'
    verbose_name_plural = 'Общие параметры для товара категории "Оперативная память"'


class CompositionRamSpecificationsInline(admin.StackedInline):
    model = CompositionRamSpecifications
    verbose_name = 'Объем и состав комплекта для товара категории "Оперативная память"'
    verbose_name_plural = 'Объем и состав комплекта для товара категории "Оперативная память"'


class PerformanceRamSpecificationsInline(admin.StackedInline):
    model = PerformanceRamSpecifications
    verbose_name = 'Быстродействие для товара категории "Оперативная память"'
    verbose_name_plural = 'Быстродействие для товара категории "Оперативная память"'


class TimingsRamSpecificationsInline(admin.StackedInline):
    model = TimingsRamSpecifications
    verbose_name = 'Тайминги для товара категории "Оперативная память"'
    verbose_name_plural = 'Тайминги для товара категории "Оперативная память"'


class DesignRamSpecificationsInline(admin.StackedInline):
    model = DesignRamSpecifications
    verbose_name = 'Конструкция для товара категории "Оперативная память"'
    verbose_name_plural = 'Конструкция для товара категории "Оперативная память"'


# Инлайны для категории "ССД"

class FactoryDataSolidStateDriveSpecificationsInline(admin.StackedInline):
    model = FactoryDataSolidStateDriveSpecifications
    verbose_name = 'Заводские данные для товара категории "ССД"'
    verbose_name_plural = 'Заводские данные для товара категории "ССД"'


class CommonParametersSolidStateDriveSpecificationsInline(admin.StackedInline):
    model = CommonParametersSolidStateDriveSpecifications
    verbose_name = 'Общие параметры для товара категории "ССД"'
    verbose_name_plural = 'Общие параметры для товара категории "ССД"'


class MainCharacteristicsSolidStateDriveSpecificationsInline(admin.StackedInline):
    model = MainCharacteristicsSolidStateDriveSpecifications
    verbose_name = 'Основные характеристики для товара категории "ССД"'
    verbose_name_plural = 'Основные характеристики для товара категории "ССД"'


class DriveConfigurationSolidStateDriveSpecificationsInline(admin.StackedInline):
    model = DriveConfigurationSolidStateDriveSpecifications
    verbose_name = 'Конфигурация накопителя для товара категории "ССД"'
    verbose_name_plural = 'Конфигурация накопителя для товара категории "ССД"'


class PerformanceIndicatorsSolidStateDriveSpecificationsInline(admin.StackedInline):
    model = PerformanceIndicatorsSolidStateDriveSpecifications
    verbose_name = 'Показатели производительности для товара категории "ССД"'
    verbose_name_plural = 'Показатели производительности для товара категории "ССД"'


class ReliabilitySolidStateDriveSpecificationsInline(admin.StackedInline):
    model = ReliabilitySolidStateDriveSpecifications
    verbose_name = 'Надежность для товара категории "ССД"'
    verbose_name_plural = 'Надежность для товара категории "ССД"'


class DimensionsSolidStateDriveSpecificationsInline(admin.StackedInline):
    model = DimensionsSolidStateDriveSpecifications
    verbose_name = 'Габариты, вес для товара категории "ССД"'
    verbose_name_plural = 'Габариты, вес для товара категории "ССД"'


# Инлайны для категории "Видеокарта"

class FactoryDataVideoCartSpecificationsInline(admin.StackedInline):
    model = FactoryDataVideoCartSpecifications
    verbose_name = 'Заводские данные для товара категории "Видеокарта"'
    verbose_name_plural = 'Заводские данные для товара категории "Видеокарта"'


class CommonParametersVideoCartSpecificationsInline(admin.StackedInline):
    model = CommonParametersVideoCartSpecifications
    verbose_name = 'Общие параметры для товара категории "Видеокарта"'
    verbose_name_plural = 'Общие параметры для товара категории "Видеокарта"'


class MainParametersVideoCartSpecificationsInline(admin.StackedInline):
    model = MainParametersVideoCartSpecifications
    verbose_name = 'Основные параметры для товара категории "Видеокарта"'
    verbose_name_plural = 'Основные параметры для товара категории "Видеокарта"'


class VideoMemoryVideoCartSpecificationsInline(admin.StackedInline):
    model = VideoMemoryVideoCartSpecifications
    verbose_name = 'Спецификация видеопамяти для товара категории "Видеокарта"'
    verbose_name_plural = 'Спецификация видеопамяти для товара категории "Видеокарта"'


class VideoProcessorVideoCartSpecificationsInline(admin.StackedInline):
    model = VideoProcessorVideoCartSpecifications
    verbose_name = 'Спецификация видеопроцессора для товара категории "Видеокарта"'
    verbose_name_plural = 'Спецификация видеопроцессора для товара категории "Видеокарта"'


class OutputImageVideoCartSpecificationsInline(admin.StackedInline):
    model = OutputImageVideoCartSpecifications
    verbose_name = 'Вывод изображения для товара категории "Видеокарта"'
    verbose_name_plural = 'Вывод изображения для товара категории "Видеокарта"'


class ConnectionVideoCartSpecificationsInline(admin.StackedInline):
    model = ConnectionVideoCartSpecifications
    verbose_name = 'Подключение для товара категории "Видеокарта"'
    verbose_name_plural = 'Подключение для товара категории "Видеокарта"'


class CoolingSystemVideoCartSpecificationsInline(admin.StackedInline):
    model = CoolingSystemVideoCartSpecifications
    verbose_name = 'Система охлаждения для товара категории "Видеокарта"'
    verbose_name_plural = 'Система охлаждения для товара категории "Видеокарта"'


class DimensionsAndWightVideoCartSpecificationsInline(admin.StackedInline):
    model = DimensionsAndWightVideoCartSpecifications
    verbose_name = 'Габариты и вес для товара категории "Видеокарта"'
    verbose_name_plural = 'Габариты и вес для товара категории "Видеокарта"'


@admin.register(Product)
class ProductAdmin(NumericFilterModelAdmin):

    def get_html_photo(self, object_):
        if object_.photoproduct_set.first:
            return mark_safe(f'<img src="{object_.photoproduct_set.first().photo.url}" width=100>')

    list_display = ('id', 'name', 'get_html_photo', 'price', 'count', 'brand', 'category', 'show')
    list_display_links = ('name', 'get_html_photo')

    readonly_fields = ('id', 'get_html_photo', )

    search_fields = ('name', 'category', 'brand', )
    list_filter = (('price', RangeNumericFilter), ('count', RangeNumericFilter), 'category', 'brand', )

    list_editable = ('show', )

    get_html_photo.short_description = 'Фото'

    inlines = [
        ProductPhotoInline,
        # Категория "Корпус"
        FactoryDataComputerCaseSpecificationsInline,
        CommonParametersComputerCaseSpecificationsInline,
        FormFactorComputerCaseSpecificationsInline,
        AppearanceComputerCaseSpecificationsInline,
        CompatibilityComputerCaseSpecificationsInline,
        CoolingComputerCaseSpecificationsInline,
        FrontPanelConnectorsComputerCaseSpecificationsInline,
        ServiceComputerCaseSpecificationsInline,
        # Категория "Кулер"
        FactoryDataCoolerSpecificationsInline,
        CommonParametersCoolerSpecifications,
        RadiatorCoolerSpecificationsInline,
        FanCoolerSpecificationsInline,
        DimensionsCoolerSpecificationsInline,
        # Категория "Жесткие диски",
        FactoryDataHDDSpecificationsInline,
        CommonParametersHDDSpecificationsInline,
        StorageDeviceHDDSpecificationsInline,
        MechanicsReliabilityHDDSpecificationsInline,
        DimensionsHDDSpecificationsInline,
        # Инлайны для категории "Материнская плата"
        FactoryDataMotherboardSpecificationsInline,
        CommonParametersMotherboardSpecificationsInline,
        FormFactorDimensionsMotherboardSpecificationsInline,
        ProcessorChipsetMotherboardSpecificationsInline,
        MemoryMotherboardSpecificationsInline,
        StorageControllersMotherboardSpecificationsInline,
        ExpansionSlotsMotherboardSpecificationsInline,
        BackPanelMotherboardSpecificationsInline,
        InternalConnectorsMotherboardSpecificationsInline,
        AudioMotherboardSpecificationsInline,
        NetMotherboardSpecificationsInline,
        CoolingPowerMotherboardSpecificationsInline,
        # Инлайны для категории "Блок питания"
        FactoryDataPowerSupplySpecificationsInline,
        CommonParametersPowerSupplySpecificationsInline,
        AppearancePowerSupplySpecificationsInline,
        CablesConnectorsPowerSupplySpecificationsInline,
        ElectricalParametersPowerSupplySpecificationsInline,
        CoolingSystemPowerSupplySpecificationsInline,
        CertificationPowerSupplySpecificationsInline,
        DimensionsWeightPowerSupplySpecificationsInline,
        # Инлайны для категории "Процессор"
        FactoryDataProcessorSpecificationsInline,
        CommonParametersProcessorSpecificationsInline,
        CoreArchitectureProcessorSpecificationsInline,
        FrequencyOverclockingProcessorSpecificationsInline,
        RamOptionsProcessorSpecifications,
        ThermalCharacteristicsProcessorSpecificationsInline,
        GraphicsCoreProcessorSpecificationsInline,
        BusControllersProcessorSpecificationsInline,
        # Инлайны для категории "Оперативная память"
        FactoryDataRamSpecificationsInline,
        CommonParametersRamSpecificationsInline,
        CompositionRamSpecificationsInline,
        PerformanceRamSpecificationsInline,
        TimingsRamSpecificationsInline,
        DesignRamSpecificationsInline,
        # Инлайны для категории "ССД"
        FactoryDataSolidStateDriveSpecificationsInline,
        CommonParametersSolidStateDriveSpecificationsInline,
        MainCharacteristicsSolidStateDriveSpecificationsInline,
        DriveConfigurationSolidStateDriveSpecificationsInline,
        PerformanceIndicatorsSolidStateDriveSpecificationsInline,
        ReliabilitySolidStateDriveSpecificationsInline,
        DimensionsSolidStateDriveSpecificationsInline,
        # Инлайны для категории "Видеокарта"
        FactoryDataVideoCartSpecificationsInline,
        CommonParametersVideoCartSpecificationsInline,
        MainParametersVideoCartSpecificationsInline,
        VideoMemoryVideoCartSpecificationsInline,
        VideoProcessorVideoCartSpecificationsInline,
        OutputImageVideoCartSpecificationsInline,
        ConnectionVideoCartSpecificationsInline,
        CoolingSystemVideoCartSpecificationsInline,
        DimensionsAndWightVideoCartSpecificationsInline,
    ]
