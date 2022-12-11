import os
import random
import sys

from datetime import date
from shutil import copy
from string import ascii_letters

import django

from settings import *

sys.path.append('/home/konstantin/Dropbox/Python_Lerning/Django/CLA__internet_shop_technique/CLA__shop')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

django.setup()


from shop_products.models import (
    BrandProduct, CategoryProduct, PhotoProduct, Product, specifications,
)

COUNT_PRODUCTS_FOR_ONE_CATEGORY = 15  # Количество товаров в одной категории
# Описание ко всем товарам
DESCRIPTION = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget nullam non nisi est sit. Orci nulla pellentesque dignissim enim sit amet venenatis urna. Est ante in nibh mauris cursus mattis molestie. Pharetra diam sit amet nisl suscipit adipiscing bibendum. Turpis massa sed elementum tempus. Hac habitasse platea dictumst quisque sagittis purus sit. Tortor at risus viverra adipiscing. Ac auctor augue mauris augue. Nunc aliquet bibendum enim facilisis.'

ALL_BRANDS = BrandProduct.objects.all()
ALL_CATEGORIES = CategoryProduct.objects.all()

CATEGORIES_AND_PHOTO_PRODUCTS = {
    'Корпус': 'computer_case',
    'Кулер': 'cooler',
    'Жесткий диск': 'hdd',
    'Материнская плата': 'mother_board',
    'Блок питания': 'power_supply',
    'Процессор': 'processor',
    'Оперативная память': 'ram',
    'ССД': 'ssd',
    'Видеокарта': 'video_card',
}

COLORS = [
    'морская волна',
    'черный',
    'голубой',
    'фуксин',
    'серый',
    'зеленый',
    'ярко-зеленый',
    'темно-бордовый',
    'темно-синий',
    'оливковый',
    'фиолетовый',
    'расный',
    'серебряный',
    'серо-зеленый',
    'белый',
    'желтый',
]

MATERIALS = ['металл', 'стекло', 'пластик']


def create_product(cur_category: CategoryProduct) -> Product:
    """
    Функция создания нового товара соответствующей категории
    :param cur_category: Категория, в которой необходимо создать продукт
    :return: Возвращает созданный продукт
    """
    cur_brand = random.choice(avail_brands)
    new_product = Product(
        name=' '.join([cur_brand.name, category.name]) + ' ' + ''.join(random.choice(ascii_letters) for i in range(40)),
        price=random.randint(1_000, 100_000),
        count=random.randint(10, 100),
        brand=cur_brand,
        category=category,
        description=DESCRIPTION,
        show=True,
    )
    # Сохраняем объект в БД
    new_product.save()
    return new_product


def add_photo_for_product(product) -> list:
    """
    Функция создает список с объектами, которые содержат фото для соответствующего товара
    :param product: Товар, для которого необходимо добавить фото
    :return: Возвращает список с объектами, которые содержат фото для соответствующего товара
    """
    # Определяем номер продукта из заранее заготовленных (всего 5)
    num_product_for_photo = random.randint(0, 4)
    # Определяем количество фото для данного продукта
    path_product = PATH_ALL_PHOTO+f'products/{CATEGORIES_AND_PHOTO_PRODUCTS[product.category.name]}/{num_product_for_photo}/'
    photos_files = os.listdir(path_product)
    # Создаем объекты с фото
    output_lst = []
    max_num_photo = random.randint(0, len(photos_files))
    max_num_photo = 1 if not max_num_photo else max_num_photo
    for cur_num_photo in range(0, max_num_photo):
        # Путь до файла
        src = path_product+photos_files[cur_num_photo]
        # Путь до фотографии в media
        photo_media_path = f'/products/{product}/{photos_files[cur_num_photo]}'
        dst = str(django.conf.settings.MEDIA_ROOT) + photo_media_path
        # Копируем фото в медиа
        os.makedirs('/'.join(dst.split('/')[0:-1]), exist_ok=True)
        copy(src, dst)
        # Создаем объект и копируем его в БД
        photo_product = PhotoProduct(product=product, photo=photo_media_path)
        output_lst.append(photo_product)
        photo_product.save()
    return output_lst


def create_computer_case_specifications(product):
    """
    Функция создает объекты с расширенными параметрами для товара категории "Корпус"
    :param product: Товар, для которого необходимо создать расширенные характеристики
    :return: Возвращает объекты с расширенными параметрами для входного товара
    """
    # Создаем объекты с расширенными настройками
    factory_data = specifications.computer_case_specifications.FactoryDataComputerCaseSpecifications(
        warranty=random.randint(1, 10),
        product=product,
    )
    common_parameters = specifications.computer_case_specifications.CommonParametersComputerCaseSpecifications(
        model=''.join(random.choice(ascii_letters) for i in range(25)),
        manufacturer_code=''.join(random.choice(ascii_letters) for i in range(25)),
        product=product,
    )
    form_factor = specifications.computer_case_specifications.FormFactorComputerCaseSpecifications(
        frame_size=''.join(random.choice(ascii_letters) for i in range(25)),
        motherboard_orientation=random.choice(specifications.computer_case_specifications.FormFactorComputerCaseSpecifications.MotherBoardOrientationChoices.choices)[0],
        length=random.randint(200, 300),
        width=random.randint(50, 100),
        height=random.randint(300, 500),
        weight=random.randint(400, 800),
        product=product,
    )
    appearance = specifications.computer_case_specifications.AppearanceComputerCaseSpecifications(
        main_color=random.choice(COLORS),
        housing_material=random.choice(MATERIALS),
        metal_thickness=random.randint(1, 5),
        window_side_wall=random.choice([False, True]),
        window_material=random.choice(MATERIALS),
        front_panel_material=random.choice(MATERIALS),
        backlight_type=random.choice(specifications.computer_case_specifications.AppearanceComputerCaseSpecifications.BacklightColorChoices.choices)[0],
        backlight_color=random.choice(COLORS),
        backlight_source=''.join(random.choice(ascii_letters) for i in range(10)),
        product=product
    )
    compatibility = specifications.computer_case_specifications.CompatibilityComputerCaseSpecifications(
        compatible_board_form_factor=', '.join([random.choice(specifications.motherboard_specifications.FormFactorDimensionsMotherboardSpecifications.FormFactorChoices.choices)[0] for _ in range(3)]),
        placement_power_supply=random.choice(specifications.computer_case_specifications.CompatibilityComputerCaseSpecifications.PlacementPowerSupplyChoices.choices)[0],
        horizontal_expansion_slots=random.randint(0, 10),
        vertical_expansion_slots=random.randint(1, 10),
        max_length_installed_video_card=random.randint(100, 300),
        max_cpu_cooler_height=random.randint(50, 200),
        number_2_5_drive_bays=random.randint(0, 5),
        number_internal_3_5_bays=random.randint(0, 5),
        number_external_3_5_bays=random.randint(0, 5),
        number_bays_5_25=random.randint(0, 5),
        product=product
    )
    cooling = specifications.computer_case_specifications.CoolingComputerCaseSpecifications(
        fans_included=random.choice([False, True]),
        front_fan_support=''.join(random.choice(ascii_letters) for i in range(25)),
        rear_fan_support=''.join(random.choice(ascii_letters) for i in range(25)),
        top_fan_support=''.join(random.choice(ascii_letters) for i in range(25)),
        bottom_fan_support=''.join(random.choice(ascii_letters) for i in range(25)),
        side_fan_support=''.join(random.choice(ascii_letters) for i in range(25)),
        installing_liquid_cooling_system=random.choice([False, True]),
        rear_mounting_dimension_radiator=''.join(random.choice(ascii_letters) for i in range(25)),
        side_mounting_dimension_radiator=''.join(random.choice(ascii_letters) for i in range(25)),
        product=product,
    )
    front_panel = specifications.computer_case_specifications.FrontPanelConnectorsComputerCaseSpecifications(
        connectors=''.join(random.choice(ascii_letters) for i in range(50)),
        built_card_reader=random.choice([False, True]),
        product=product,
    )
    service = specifications.computer_case_specifications.ServiceComputerCaseSpecifications(
        cutout_area_mounting_cpu_cooler=random.choice([False, True]),
        rear_cable_routing=random.choice([False, True]),
        dust_filter=random.choice([False, True]),
        product=product,
    )
    # Сохраняем объекты в БД
    factory_data.save()
    common_parameters.save()
    form_factor.save()
    appearance.save()
    compatibility.save()
    cooling.save()
    front_panel.save()
    service.save()
    return factory_data, common_parameters, form_factor, appearance, compatibility, cooling, front_panel, service


def create_cooler_specifications(product):
    """
    Функция создает объекты с расширенными параметрами для товара категории "Кулер"
    :param product: Товар, для которого необходимо создать расширенные характеристики
    :return: Возвращает объекты с расширенными параметрами для входного товара
    """
    # Создаем объекты с расширенными настройками
    factory_data = specifications.cooler_specifications.FactoryDataCoolerSpecifications(
        warranty=random.randint(1, 10),
        product=product,
    )
    common_data = specifications.cooler_specifications.CommonParametersCoolerSpecifications(
        model=''.join((random.choice(ascii_letters)) for _ in range(25)),
        socket=''.join((random.choice(ascii_letters)) for _ in range(100)),
        power_dissipation=random.randint(25, 100),
        construction_type=''.join((random.choice(ascii_letters)) for _ in range(25)),
        product=product,
    )
    radiator = specifications.cooler_specifications.RadiatorCoolerSpecifications(
        base_material=random.choice(MATERIALS),
        radiator_material=random.choice(MATERIALS),
        number_heat_pipes=random.randint(1, 6),
        heat_pipe_diameter=random.randint(5, 20),
        nickel_plated=''.join((random.choice(ascii_letters)) for _ in range(50)),
        radiator_color=random.choice(COLORS),
        product=product,
    )
    fan_cooler = specifications.cooler_specifications.FanCoolerSpecifications(
        number_fans_included=random.randint(1, 4),
        max_number_installed_fans=random.randint(2, 4),
        dimensions_complete_fans=''.join((random.choice(ascii_letters)) for _ in range(50)),
        fan_color=random.choice(COLORS),
        max_rotation_speed=random.randint(500, 5000),
        min_rotation_speed=random.randint(250, 500),
        max_airflow=random.random(),
        max_static_pressure=random.random(),
        max_noise_level=random.random(),
        rated_current=random.random(),
        rated_voltage=random.randint(1, 12),
        bearing_type=''.join((random.choice(ascii_letters)) for _ in range(50)),
        product=product,
    )
    dimensions = specifications.cooler_specifications.DimensionsCoolerSpecifications(
        length=random.randint(200, 300),
        width=random.randint(200, 300),
        height=random.randint(300, 500),
        weight=random.randint(500, 700),
        product=product,
    )
    # Сохраняем объекты в БД
    factory_data.save()
    common_data.save()
    radiator.save()
    fan_cooler.save()
    dimensions.save()
    return factory_data, common_data, radiator, fan_cooler, dimensions


def create_hdd_specifications(product):
    """
    Функция создает объекты с расширенными параметрами для товара категории "Жесткий диск"
    :param product: Товар, для которого необходимо создать расширенные характеристики
    :return: Возвращает объекты с расширенными параметрами для входного товара
    """
    # Создаем объекты с расширенными настройками
    factory_data = specifications.hdd_specifications.FactoryDataHDDSpecifications(
        warranty=random.randint(1, 10),
        product=product,
    )
    common_parameters = specifications.hdd_specifications.CommonParametersHDDSpecifications(
        model=''.join((random.choice(ascii_letters)) for _ in range(50)),
        manufacturer_code=''.join((random.choice(ascii_letters)) for _ in range(50)),
        product=product,
    )
    storage_device = specifications.hdd_specifications.StorageDeviceHDDSpecifications(
        hdd_volume=random.randint(512, 32768),
        cache_size=random.randint(4, 124),
        spindle_speed=random.randint(1000, 20000),
        max_data_rate=random.randint(32, 128),
        average_latency=random.random(),
        optimization_raid_arrays=random.choice([False, True]),
        product=product,
    )
    mechanics_reliability = specifications.hdd_specifications.MechanicsReliabilityHDDSpecifications(
        shock_resistance_wort=random.random(),
        with_helium_filling=random.choice([False, True]),
        product=product,
    )
    dimensions = specifications.hdd_specifications.DimensionsHDDSpecifications(
        length=random.randint(150, 250),
        width=random.randint(75, 150),
        height=random.randint(50, 100),
        weight=random.randint(500, 700),
        product=product,
    )
    # Сохраняем данные в БД
    factory_data.save()
    common_parameters.save()
    storage_device.save()
    mechanics_reliability.save()
    dimensions.save()
    return factory_data, common_parameters, storage_device, mechanics_reliability, dimensions


def create_motherboard_specifications(product):
    """
    Функция создает объекты с расширенными параметрами для товара категории "Материнская плата"
    :param product: Товар, для которого необходимо создать расширенные характеристики
    :return: Возвращает объекты с расширенными параметрами для входного товара
    """
    # Создаем объекты с расширенными настройками
    factory_data = specifications.motherboard_specifications.FactoryDataMotherboardSpecifications(
        manufacturer_warranty=random.randint(1, 10),
        producing_country=''.join(random.choice(ascii_letters) for _ in range(100)),
        product=product,
    )
    common_data = specifications.motherboard_specifications.CommonParametersMotherboardSpecifications(
        model=''.join(random.choice(ascii_letters) for _ in range(50)),
        product=product,
    )
    form_factor_dimensions = specifications.motherboard_specifications.FormFactorDimensionsMotherboardSpecifications(
        form_factor=random.choice(specifications.motherboard_specifications.FormFactorDimensionsMotherboardSpecifications.FormFactorChoices.choices)[0],
        height=random.randint(250, 700),
        width=random.randint(250, 700),
        product=product,
    )
    processor_chipset = specifications.motherboard_specifications.ProcessorChipsetMotherboardSpecifications(
        socket=''.join(random.choice(ascii_letters) for _ in range(50)),
        chipset=''.join(random.choice(ascii_letters) for _ in range(50)),
        compatible_processor_cores=''.join(random.choice(ascii_letters) for _ in range(100)),
        product=product,
    )
    memory = specifications.motherboard_specifications.MemoryMotherboardSpecifications(
        numbers_slot=random.randint(2, 10),
        form_factor=random.choice(specifications.motherboard_specifications.MemoryMotherboardSpecifications.FormFactorMemoryChoices.choices)[0],
        supported_memory=random.choice(specifications.motherboard_specifications.MemoryMotherboardSpecifications.SupportedMemoryChoices.choices)[0],
        number_channels=random.randint(1, 6),
        maximum_memory=random.randint(16, 512),
        maximum_memory_frequency=random.randint(1800, 4000),
        frequency_overclocking=random.randint(1800, 5000),
        product=product,
    )
    storage_controllers = specifications.motherboard_specifications.StorageControllersMotherboardSpecifications(
        number_m2_connectors=random.randint(0, 4),
        m2_connectors=''.join(random.choice(ascii_letters) for _ in range(50)),
        number_sata_ports=random.randint(1, 10),
        sata_raid_mode=''.join(random.choice(ascii_letters) for _ in range(50)),
        nvme_support=random.choice([False, True]),
        product=product,
    )
    expansion_slot = specifications.motherboard_specifications.ExpansionSlotsMotherboardSpecifications(
        pci_express_version=3.2,
        number_x16_slots=random.randint(1, 4),
        sli_crossfire_support=''.join(random.choice(ascii_letters) for _ in range(25)),
        number_cards_sli=random.randint(0, 3),
        number_x1_slots=random.randint(0, 3),
        other_expansions_slots=''.join(random.choice(ascii_letters) for _ in range(100)),
        product=product,
    )
    back_panel = specifications.motherboard_specifications.BackPanelMotherboardSpecifications(
        number_type_usb=''.join(random.choice(ascii_letters) for _ in range(100)),
        video_outputs=''.join(random.choice(ascii_letters) for _ in range(50)),
        number_network_ports=random.randint(1, 3),
        number_analog_audio=random.randint(1, 5),
        digital_audio_ports=''.join(random.choice(ascii_letters) for _ in range(50)),
        other_connectors=''.join(random.choice(ascii_letters) for _ in range(150)),
        product=product,
    )
    internal_connectors = specifications.motherboard_specifications.InternalConnectorsMotherboardSpecifications(
        internal_usb_connectors=''.join(random.choice(ascii_letters) for _ in range(100)),
        cpu_cooler_power=''.join(random.choice(ascii_letters) for _ in range(50)),
        pin_pwm_fan_4=random.randint(1, 10),
        pin_fan_3=random.randint(1, 5),
        pin_led_3=random.randint(0, 4),
        pin_led_4=random.randint(0, 10),
        m2_e_key=random.choice([False, True]),
        lpt_interface=random.choice([False, True]),
        product=product,
    )
    audio = specifications.motherboard_specifications.AudioMotherboardSpecifications(
        sound_scheme=''.join(random.choice(ascii_letters) for _ in range(10)),
        audio_adapter=''.join(random.choice(ascii_letters) for _ in range(50)),
        product=product
    )
    net = specifications.motherboard_specifications.NetMotherboardSpecifications(
        network_adapter_speed=random.randint(16, 1024),
        network_adapter_chipset=''.join(random.choice(ascii_letters) for _ in range(50)),
        wifi_adapter=''.join(random.choice(ascii_letters) for _ in range(50)),
        wifi_controller=''.join(random.choice(ascii_letters) for _ in range(50)),
        bluetooth=''.join(random.choice(ascii_letters) for _ in range(25)),
        product=product,
    )
    cooling_power = specifications.motherboard_specifications.CoolingPowerMotherboardSpecifications(
        main_power_connector=''.join(random.choice(ascii_letters) for _ in range(10)),
        cpu_power_connector=''.join(random.choice(ascii_letters) for _ in range(10)),
        number_power_phases=random.randint(5, 20),
        passive_cooling=random.choice([False, True]),
        active_cooling=random.choice([False, True]),
        product=product,
    )
    factory_data.save()
    common_data.save()
    form_factor_dimensions.save()
    processor_chipset.save()
    memory.save()
    storage_controllers.save()
    expansion_slot.save()
    back_panel.save()
    internal_connectors.save()
    audio.save()
    net.save()
    cooling_power.save()
    return factory_data, common_data, form_factor_dimensions, processor_chipset, memory, storage_controllers, expansion_slot, back_panel, internal_connectors, audio, net, cooling_power


def create_power_supply_specifications(product):
    """
    Функция создает объекты с расширенными параметрами для товара категории "Блок питания"
    :param product: Товар, для которого необходимо создать расширенные характеристики
    :return: Возвращает объекты с расширенными параметрами для входного товара
    """
    # Создаем объекты с расширенными настройками
    factory_data = specifications.power_supply_specifications.FactoryDataPowerSupplySpecifications(
        warranty=random.randint(1, 10),
        product=product,
    )
    common_data = specifications.power_supply_specifications.CommonParametersPowerSupplySpecifications(
        model=''.join(random.choice(ascii_letters) for _ in range(50)),
        manufacturer_code=''.join(random.choice(ascii_letters) for _ in range(50)),
        power=random.randint(250, 2000),
        product=product,
    )
    appearance = specifications.power_supply_specifications.AppearancePowerSupplySpecifications(
        form_factor=random.choice(specifications.power_supply_specifications.AppearancePowerSupplySpecifications.FormFactorChoices.choices)[0],
        color=random.choice(COLORS),
        datachable_cables=random.choice([False, True]),
        wire_braid=random.choice([False, True]),
        backlight_type=random.choice([False, True]),
        wire_colors=''.join(random.choice(ascii_letters) for _ in range(25)),
        product=product,
    )
    cables_connectors = specifications.power_supply_specifications.CablesConnectorsPowerSupplySpecifications(
        main_power_connector=''.join(random.choice(ascii_letters) for _ in range(25)),
        processor_power=''.join(random.choice(ascii_letters) for _ in range(10)),
        video_card_power=''.join(random.choice(ascii_letters) for _ in range(10)),
        number_connectors_15pin_sata=random.randint(1, 3),
        number_4pin_molex=random.randint(1, 6),
        connector_4pin_floppy=random.choice([False, True]),
        product=product,
    )
    electrical_parameters = specifications.power_supply_specifications.ElectricalParametersPowerSupplySpecifications(
        current_plus_12=random.random(),
        current_3_3=random.random(),
        current_5=random.random(),
        standby_current=random.random(),
        line_current_minus_12=random.random(),
        product=product,

    )
    cooling_system = specifications.power_supply_specifications.CoolingSystemPowerSupplySpecifications(
        cooling_system=''.join(random.choice(ascii_letters) for _ in range(25)),
        fan_dimensions=''.join(random.choice(ascii_letters) for _ in range(25)),
        speed_control=''.join(random.choice(ascii_letters) for _ in range(25)),
        product=product,
    )
    certification = specifications.power_supply_specifications.CertificationPowerSupplySpecifications(
        certificate_80_plus=random.choice(specifications.power_supply_specifications.CertificationPowerSupplySpecifications.Certificate80Choices.choices)[0],
        pfc=''.join(random.choice(ascii_letters) for _ in range(25)),
        protection_technologies=''.join(random.choice(ascii_letters) for _ in range(25)),
        product=product,
    )
    dimensions = specifications.power_supply_specifications.DimensionsWeightPowerSupplySpecifications(
        length=random.randint(200, 400),
        width=random.randint(200, 400),
        height=random.randint(200, 300),
        weight=random.randint(400, 800),
        product=product,
    )
    # Сохраняем данные в БД
    factory_data.save()
    common_data.save()
    appearance.save()
    cables_connectors.save()
    electrical_parameters.save()
    cooling_system.save()
    certification.save()
    dimensions.save()
    return factory_data, common_data, appearance, cables_connectors, electrical_parameters, cooling_system, certification, dimensions


def create_processor_specifications(product):
    """
    Функция создает объекты с расширенными параметрами для товара категории "Процессор"
    :param product: Товар, для которого необходимо создать расширенные характеристики
    :return: Возвращает объекты с расширенными параметрами для входного товара
    """
    # Создаем объекты с расширенными настройками
    factory_data = specifications.processor_specifications.FactoryDataProcessorSpecifications(
        guarantee=random.randint(1, 10),
        producing_country=''.join(random.choice(ascii_letters) for _ in range(50)),
        product=product,
    )
    common_parameters = specifications.processor_specifications.CommonParametersProcessorSpecifications(
        model=''.join(random.choice(ascii_letters) for _ in range(50)),
        socket=''.join(random.choice(ascii_letters) for _ in range(50)),
        manufacturer_code=''.join(random.choice(ascii_letters) for _ in range(50)),
        release_year=date(2022, 1, 1),
        cooling_system=random.choice([False, True]),
        thermal_interface=random.choice([False, True]),
        product=product,
    )
    core_architecture = specifications.processor_specifications.CoreArchitectureProcessorSpecifications(
        count_cores=random.randint(2, 16),
        maximum_threads=random.randint(2, 32),
        number_performance=random.randint(2, 16),
        number_energy_efficient=random.randint(2, 16),
        l2_cache_size=random.randint(32, 128),
        l3_cache_size=random.randint(32, 128),
        process_technology=random.randint(6, 16),
        nucleus=''.join(random.choice(ascii_letters) for _ in range(50)),
        product=product,
    )
    frequency_overclocking = specifications.processor_specifications.FrequencyOverclockingProcessorSpecifications(
        cpu_base_frequency=random.randint(1200, 8800),
        maximum_turbo_frequency=random.randint(3600, 9900),
        base_frequency_efficient_cores=random.randint(100, 800),
        turbo_frequency_efficient_cores=random.randint(2400, 8800),
        product=product,
    )
    ram_options = specifications.processor_specifications.RamOptionsProcessorSpecifications(
        memory_type=random.choice(['DDR2', 'DDR3', 'DDR4']),
        maximum_supported_memory=random.randint(16, 256),
        number_channels=random.randint(4, 32),
        maximum_ram_frequency=random.randint(2000, 5000),
        product=product,
    )
    thermal_characteristics = specifications.processor_specifications.ThermalCharacteristicsProcessorSpecifications(
        tdp=random.randint(128, 1000),
        base_heat_dissipation=random.randint(128, 1000),
        max_cpu_temperature=random.randint(90, 130),
        product=product,
    )
    graphics_core = specifications.processor_specifications.GraphicsCoreProcessorSpecifications(
        integrated_graphics_core=random.choice([False, True]),
        gpu_model=''.join(random.choice(ascii_letters) for _ in range(50)),
        maximum_frequency=random.randint(2400, 8800),
        product=product,
    )
    bus_controllers = specifications.processor_specifications.BusControllersProcessorSpecifications(
        integrated_pci_controller=''.join(random.choice(ascii_letters) for _ in range(50)),
        number_pci_lanes=random.randint(5, 30),
        product=product,
    )
    # Сохраняем объекты в БД
    factory_data.save()
    common_parameters.save()
    core_architecture.save()
    frequency_overclocking.save()
    ram_options.save()
    thermal_characteristics.save()
    graphics_core.save()
    bus_controllers.save()
    return factory_data, common_parameters, core_architecture, frequency_overclocking, ram_options, thermal_characteristics, graphics_core, bus_controllers


def create_ram_specifications(product):
    """
    Функция создает объекты с расширенными параметрами для товара категории "Оперативная память"
    :param product: Товар, для которого необходимо создать расширенные характеристики
    :return: Возвращает объекты с расширенными параметрами для входного товара
    """
    # Создаем объекты с расширенными настройками
    factory_data = specifications.ram_specifications.FactoryDataRamSpecifications(
        warranty=random.randint(1, 10),
        product=product,
    )
    common_parameters = specifications.ram_specifications.CommonParametersRamSpecifications(
        model=''.join((random.choice(ascii_letters)) for _ in range(50)),
        manufacturer_code=''.join((random.choice(ascii_letters)) for _ in range(50)),
        product=product,
    )
    composition_ram = specifications.ram_specifications.CompositionRamSpecifications(
        type=random.choice(specifications.ram_specifications.CompositionRamSpecifications.TypeMemoryChoices.choices)[0],
        form_factor=random.choice(specifications.ram_specifications.CompositionRamSpecifications.FormFactorMemoryChoices.choices)[0],
        one_memory_module=random.randint(2, 32),
        number_modules_included=random.randint(1, 4),
        register_memory=random.choice([False, True]),
        ecc_memory=random.choice([False, True]),
        product=product,
    )
    performance = specifications.ram_specifications.PerformanceRamSpecifications(
        clock_frequency=random.randint(2000, 5000),
        xmp_profiles=''.join((random.choice(ascii_letters)) for _ in range(25)),
        product=product,
    )
    timings = specifications.ram_specifications.TimingsRamSpecifications(
        cl=random.randint(1, 10),
        trcd=random.randint(100, 500),
        trp=random.randint(100, 500),
        tras=random.randint(100, 500),
        product=product,
    )
    design = specifications.ram_specifications.DesignRamSpecifications(
        presence_radiator=random.choice([False, True]),
        radiator_color=random.choice(COLORS),
        height=random.randint(70, 120),
        low_profile=random.choice([False, True]),
        product=product,
    )
    # Сохраняем данные в БД
    factory_data.save()
    common_parameters.save()
    composition_ram.save()
    performance.save()
    timings.save()
    design.save()
    return factory_data, common_parameters, composition_ram, performance, timings, design


def create_solid_state_drive_specifications(product):
    """
    Функция создает объекты с расширенными параметрами для товара категории "ССД"
    :param product: Товар, для которого необходимо создать расширенные характеристики
    :return: Возвращает объекты с расширенными параметрами для входного товара
    """
    # Создаем объекты с расширенными настройками
    factory_data = specifications.solid_state_drive_specifications.FactoryDataSolidStateDriveSpecifications(
        warranty=random.randint(1, 10),
        product=product,
    )
    common_parameters = specifications.solid_state_drive_specifications.CommonParametersSolidStateDriveSpecifications(
        model=''.join(random.choice(ascii_letters) for _ in range(50)),
        manufacturer_code=''.join(random.choice(ascii_letters) for _ in range(50)),
        product=product,
    )
    main_characteristics = specifications.solid_state_drive_specifications.MainCharacteristicsSolidStateDriveSpecifications(
        storage_capacity=random.randint(64, 8192),
        nvme=random.choice([False, True]),
        connection_connector=''.join(random.choice(ascii_letters) for _ in range(10)),
        product=product,
    )
    drive_configuration = specifications.solid_state_drive_specifications.DriveConfigurationSolidStateDriveSpecifications(
        number_bits_per_cell=random.randint(10, 100),
        memory_structure=''.join(random.choice(ascii_letters) for _ in range(25)),
        dram_buffer=random.choice([False, True]),
        size_dram_buffer=random.randint(10, 300),
        product=product,
    )
    performance = specifications.solid_state_drive_specifications.PerformanceIndicatorsSolidStateDriveSpecifications(
        max_sequential_read_speed=random.randint(1024, 10000),
        max_sequential_write_speed=random.randint(512, 4000),
        random_read_speed_qd32=random.randint(1024, 10000),
        random_write_speed_qd32=random.randint(512, 4000),
        product=product,
    )
    reliability = specifications.solid_state_drive_specifications.ReliabilitySolidStateDriveSpecifications(
        tbw=random.randint(100, 1000),
        dwpd=random.random(),
        max_overload=random.random(),
        product=product,
    )
    dimensions = specifications.solid_state_drive_specifications.DimensionsSolidStateDriveSpecifications(
        length=random.randint(100, 200),
        width=random.randint(100, 200),
        height=random.randint(300, 500),
        weight=random.randint(10, 50),
        product=product,
    )
    factory_data.save()
    common_parameters.save()
    main_characteristics.save()
    drive_configuration.save()
    performance.save()
    reliability.save()
    dimensions.save()
    return factory_data, common_parameters, main_characteristics, drive_configuration, performance, reliability, dimensions


def create_videocart_specifications(product):
    """
    Функция создает объекты с расширенными параметрами для товара категории "ССД"
    :param product: Товар, для которого необходимо создать расширенные характеристики
    :return: Возвращает объекты с расширенными параметрами для входного товара
    """
    # Создаем объекты с расширенными настройками
    factory_data = specifications.videocart_specifications.FactoryDataVideoCartSpecifications(
        warranty=random.randint(1, 10),
        product=product,
    )
    common_parameters = specifications.videocart_specifications.CommonParametersVideoCartSpecifications(
        model=''.join(random.choice(ascii_letters) for _ in range(50)),
        manufacturer_code=''.join(random.choice(ascii_letters) for _ in range(50)),
        designed_mining=random.choice([False, True]),
        lhr=random.choice([False, True]),
        product=product,
    )
    main_parameters = specifications.videocart_specifications.MainParametersVideoCartSpecifications(
        gpu=''.join(random.choice(ascii_letters) for _ in range(50)),
        microarchitecture=''.join(random.choice(ascii_letters) for _ in range(50)),
        technical_process=random.randint(6, 16),
        product=product,
    )
    video_memory = specifications.videocart_specifications.VideoMemoryVideoCartSpecifications(
        video_memory_size=random.randint(512, 32768),
        memory_type=''.join(random.choice(ascii_letters) for _ in range(50)),
        memory_bus_width=random.randint(8, 128),
        maximum_memory_bandwidth=random.randint(1, 16),
        product=product,
    )
    video_processor = specifications.videocart_specifications.VideoProcessorVideoCartSpecifications(
        nominal_frequency=random.randint(1200, 8800),
        turbo_frequency=random.randint(3600, 9900),
        number_universal_processors=random.randint(1, 8),
        number_texture_units=random.randint(1000, 100000),
        number_rasterization_blocks=random.randint(1000, 100000),
        ray_tracing_support=random.choice([False, True]),
        hardware_accelerated_ray_tracing=random.randint(100, 1000),
        tensor_cores=random.randint(4, 26),
        shader_version=random.random(),
        product=product,
    )
    output_image = specifications.videocart_specifications.OutputImageVideoCartSpecifications(
        video_connectors=''.join(random.choice(ascii_letters) for _ in range(100)),
        hdmi_version=3.1,
        display_port_version=2.1,
        number_monitors=random.randint(1, 6),
        maximum_resolution=''.join(random.choice(ascii_letters) for _ in range(25)),
        product=product,
    )
    connection = specifications.videocart_specifications.ConnectionVideoCartSpecifications(
        interface=''.join(random.choice(ascii_letters) for _ in range(25)),
        connector_form_factor=''.join(random.choice(ascii_letters) for _ in range(25)),
        auxiliary_power_connectors=''.join(random.choice(ascii_letters) for _ in range(25)),
        recommended_power_supply=random.randint(256, 2000),
        product=product,
    )
    cooling_system = specifications.videocart_specifications.CoolingSystemVideoCartSpecifications(
        cooling_type=''.join(random.choice(ascii_letters) for _ in range(25)),
        number_installed_fans=random.randint(1, 5),
        liquid_cooling_radiator=random.choice([False, True]),
        product=product,
    )
    dimensions = specifications.videocart_specifications.DimensionsAndWightVideoCartSpecifications(
        low_profile=random.choice([False, True]),
        number_occupied_expansion_slots=random.randint(1, 3),
        length=random.randint(100, 600,),
        thickness=random.randint(100, 200),
        weight=random.randint(300, 700),
        product=product,
    )
    # Сохраняем данные в БД
    factory_data.save()
    common_parameters.save()
    main_parameters.save()
    video_memory.save()
    video_processor.save()
    output_image.save()
    connection.save()
    cooling_system.save()
    dimensions.save()
    return factory_data, common_parameters, main_parameters, video_memory, video_processor, output_image, connection, cooling_system, dimensions


CATEGORIES_AND_FUNCTIONS_SPECIFICATIONS = {
    'Корпус': create_computer_case_specifications,
    'Кулер': create_cooler_specifications,
    'Жесткий диск': create_hdd_specifications,
    'Материнская плата': create_motherboard_specifications,
    'Блок питания': create_power_supply_specifications,
    'Процессор': create_processor_specifications,
    'Оперативная память': create_ram_specifications,
    'ССД': create_solid_state_drive_specifications,
    'Видеокарта': create_videocart_specifications,
}


# Для каждой категории создаем товары
for category in ALL_CATEGORIES:
    # Получаем бренды, которые работают с данной категорией
    avail_brands = ALL_BRANDS.filter(categories=category)
    # Если для данной категории нет брендов, то пропускаем ее
    if len(avail_brands) == 0:
        print(category)
        continue
    for num_product in range(COUNT_PRODUCTS_FOR_ONE_CATEGORY):
        # Создаем новый товар
        new_product = create_product(category)
        # Добавляем фото для нового товара
        add_photo_for_product(new_product)
        # Создаем расширенные параметры зависимости от категории
        CATEGORIES_AND_FUNCTIONS_SPECIFICATIONS[category.name](new_product)



