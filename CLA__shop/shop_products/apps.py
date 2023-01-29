from django.apps import AppConfig


class ShopProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop_products'

    verbose_name = 'Товары магазина'

    def ready(self):
        import shop_products.signals
