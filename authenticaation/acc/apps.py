from django.apps import AppConfig


class AccConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'acc'
    def ready(self):
        import acc.signals