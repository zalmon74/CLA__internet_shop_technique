import os
import sys
from shutil import copy

import django

from settings import *

sys.path.append('/home/konstantin/Dropbox/Python_Lerning/Django/CLA__internet_shop_technique/CLA__shop')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

django.setup()

from shop_products.models import CategoryProduct, BrandProduct


# Категории расположены (по умолчанию в следующем порядке: [0] = Блок питания, [1] = Видеокарта,
# [2] = Жесткий диск, [3] = Корпус, [4] = Кулер, [5] = Оперативная память, [6] = Процессор, [7] = ССД)
all_categories = CategoryProduct.objects.all()

# name, name_file_photo, categories, description, email, show
all_brands = [
    ('computer', 'computer.png', (0, 1, 2, 5, 6), 'Hello company name is computer', 'computer@mailwork.ru', True),
    ('scientic', 'scientic.png', (2, 5, 7), 'Hello company name is scientic', 'scientic@mailwork.ru', True),
    ('hyncer', 'hyncer.png', (3, 4), 'hello company name is hyncer', 'hynser@mailwork.ru', True),
    ('chynsho', 'chynsho.png', (0,), 'hello company name is chunsho', 'chunsho@mailwork.ru', True),
    ('necpon', 'necpon.png', (0, 1, 2, 4, 5, 6, 7), 'hello company name is necpong', 'necpon@mwork.ru', True),
]

# Добавляем каждый бренд

for name_brand, name_file, categories, desc, email, f_show in all_brands:
    # Путь с расположением лого компании
    src = PATH_ALL_PHOTO+f'brands/{name_file}'
    # Путь до лого в media
    photo_media_path = f'/brands/images/{name_brand}/{name_file}'
    dst = str(django.conf.settings.MEDIA_ROOT)+photo_media_path
    # Копируем лого в медиа
    os.makedirs('/'.join(dst.split('/')[0:-1]), exist_ok=True)
    copy(src, dst)
    # Добавляем в БД
    brand = BrandProduct(name=name_brand, photo=photo_media_path, description=desc, email=email, show=f_show)
    brand.save()
    for ind_cat in categories:
        brand.categories.add(all_categories[ind_cat])






