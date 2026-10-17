from django.db import models  # Импортируем инструменты Django для создания структуры базы данных

from core.models import BaseModel  # Импортируем нашу базовую модель

class PizzaModel(BaseModel):  # Создаем класс модели Пиццы, который наследует логику от BaseModel
    class Meta:  # Специальный класс Meta для дополнительных настроек таблицы
        db_table = 'pizzas'  # Указываем, что в базе данных эта таблица должна строго называться 'pizzas'

    name = models.CharField(max_length=30)  # Создаем колонку для названия пиццы (максимум 30 символов)
    size = models.IntegerField()  # Создаем колонку для размера (целое число)
    price = models.FloatField()  # Создаем колонку для цены (число с плавающей точкой/дробное)