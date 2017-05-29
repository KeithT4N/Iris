from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        from stalls import signals
