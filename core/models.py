from django.db import models  # Импортируем инструменты Django для работы с базой данных


class BaseModel(models.Model):  # Создаем наш базовый класс, который наследует стандартную логику моделей Django
    class Meta:  # Специальный класс для настроек самой модели
        abstract = True  # делаем эту модель абстрактной

    created_at = models.DateTimeField(
        auto_now_add=True)  # Поле даты и времени создания (автоматически записывается 1 раз при создании)
    updated_at = models.DateTimeField(
        auto_now=True)  # Поле даты и времени обновления (автоматически меняется при каждом сохранении)