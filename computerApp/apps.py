from django.apps import AppConfig

from computermngt.settings import DEFAULT_AUTO_FIELD


class ComputerappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'computerApp'
