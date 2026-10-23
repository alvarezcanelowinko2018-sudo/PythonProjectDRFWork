from django.apps import AppConfig  # Импортируем базовый класс для настроек приложения


class PizzaShopConfig(AppConfig):  # Создаем класс конфигурации специально для приложения pizza_shop
    default_auto_field = 'django.db.models.BigAutoField'  # Указываем тип поля по умолчанию для автоматических ID (большие числа)
    name = 'apps.pizza_shop'  # Указываем точный путь к приложению, чтобы Django мог правильно его зарегистрировать