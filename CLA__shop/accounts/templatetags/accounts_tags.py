from django import template

register = template.Library()


@register.inclusion_tag('accounts/show_tags/profile_menu.html')
def show_profile_menu():
    """
    Тэг, который формирует меню в профиле пользователя
    """

    menu = [
        {'name': 'Профиль', 'url_name': 'user_profile'},
        {'name': 'Любимые товары', 'url_name': 'user_favorite_products'},
        {'name': 'Любимые бренды', 'url_name': 'user_favorite_brands'},
        {'name': 'История покупок', 'url_name': 'user_profile'},
    ]

    return {'list_menu': menu}


@register.inclusion_tag('accounts/show_tags/show_std_form.html')
def show_std_form(form, title, text_button):
    """
    Тэг, который формирует отображение стандартного меню
    """
    return {'form': form, 'title': title, 'text_button': text_button, }
