from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"
    verbose_name = "Доска объявлений"

    # Чтобы создание сигнала и регистрация обработчки выполнялись сразу после инициализации приложения
    def ready(self):
        from . import signals
