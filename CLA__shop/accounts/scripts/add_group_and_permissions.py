import os
import sys

from shutil import copy

import django

sys.path.append('/home/konstantin/Dropbox/Python_Lerning/Django/CLA__internet_shop_technique/CLA__shop')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

django.setup()


from accounts.models import CustomUser
from django.contrib.auth.models import Group, Permission


def create_administrators_group():
    """ Функция создает группу "Администраторы" в соответствующей таблице
    """
    group, f_created = Group.objects.get_or_create(name='Администраторы')
    if isinstance(group, Group):
        print('Создана группа "Администраторы"')
    else:
        print('Во время создания группы "Администраторы" возникла ошибка')
    return group

def add_permissions_for_administrators_group(group):
    """ Добавляет права для группы "Администраторы"

    Args:
        obj: объект группы "Администраторы", для которой необходимо добавить права
    """
    all_permissions = Permission.objects.all()
    lst_id_permissions = []
    # Добавляем права на работу с таблицами связанные с брендом
    lst_id_permissions.extend([obj.id for obj in all_permissions.filter(codename__icontains='brand')])
    # Добавляем права на работу с таблицами связанные с "связаться с нами"
    lst_id_permissions.extend([obj.id for obj in all_permissions.filter(codename__icontains='contactform')])
    # Добавляем права на работу с таблицами связанные с "товарами"
    lst_id_permissions.extend([obj.id for obj in all_permissions.filter(codename__iendswith='_product')])
    # Добавляем права на работу с таблицами связанные с "фото для товаров"
    lst_id_permissions.extend([obj.id for obj in all_permissions.filter(codename__icontains='photoproduct')])
    # Добавляем права на работу с таблицами связанные с "расширенными параметрами для товаров"
    lst_id_permissions.extend([obj.id for obj in all_permissions.filter(codename__icontains='specifications')])
    group.permissions.set(lst_id_permissions)
    
    
if __name__ == '__main__':
    group = create_administrators_group()
    add_permissions_for_administrators_group(group)
