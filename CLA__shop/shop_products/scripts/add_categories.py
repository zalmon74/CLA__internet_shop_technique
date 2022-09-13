import os
import sys
from shutil import copy

import django

from settings import *

sys.path.append('/home/konstantin/Dropbox/Python_Lerning/Django/CLA__internet_shop_technique/CLA__shop')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

django.setup()

from shop_products.models import CategoryProduct


# Все категории
computer_case = 'Корпус'
cooler = 'Кулер'
hdd = 'Жесткий диск'
power_supply = 'Блок питания'
processor = 'Процессор'
ram = 'Оперативная память'
ssd = 'ССД'
video_card = 'Видеокарта'

# Имена фотографий каждой категории
computer_case_file = 'computer_case.jpeg'
cooler_file = 'cooler.jpeg'
hdd_file = 'hdd.jpeg'
power_supply_file = 'power_supply.jpeg'
processor_file = 'processor.jpeg'
ram_file = 'ram.jpeg'
ssd_file = 'ssd.jpeg'
video_card_file = 'video_card.jpeg'

all_categories = [
    (computer_case, computer_case_file),
    (cooler, cooler_file),
    (hdd, hdd_file),
    (power_supply, power_supply_file),
    (processor, processor_file),
    (ram, ram_file),
    (ssd, ssd_file),
    (video_card, video_card_file),
]

# Добавляем каждую категорию

for name_cat, name_file in all_categories:
    # Путь с расположением фотографии
    src = PATH_ALL_PHOTO+f'categories/{name_file}'
    # Путь до фотографии в media
    photo_media_path = f'/categories/images/{name_cat}/{name_file}'
    dst = str(django.conf.settings.MEDIA_ROOT)+photo_media_path
    # Копируем фото в медиа
    os.makedirs('/'.join(dst.split('/')[0:-1]), exist_ok=True)
    copy(src, dst)
    # Добавляем в БД
    CategoryProduct.objects.update_or_create(name=name_cat, photo=photo_media_path)





