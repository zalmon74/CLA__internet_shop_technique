from accounts.models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def post_save_add_user_in_group_administrators(*args, **kwargs):
    """ Сигнал добавляет созданного пользователя в администраторы по флагу is_staff
    """
    instance = kwargs['instance']
    if instance.is_staff:
        group = Group.objects.get(name='Администраторы')
        instance.groups.add(group)

    
