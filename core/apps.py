from django.apps import AppConfig  # Импортируем класс для настройки приложения из ядра Django

class CoreConfig(AppConfig):  # Создаем класс конфигурации для нашего приложения, наследуясь от AppConfig
    name = 'core'