from django.apps import AppConfig


class InflowersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inflowers'

    def ready(self):
        import inflowers.signals

