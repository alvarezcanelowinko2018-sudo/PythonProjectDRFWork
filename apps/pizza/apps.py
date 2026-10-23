from django.apps import AppConfig  # Импортируем базовый класс для настроек приложения


class PizzaConfig(AppConfig):  # Создаем класс настроек специально для приложения pizza
    name = 'apps.pizza'  # Указываем точный путь к приложению, чтобы система могла его найти