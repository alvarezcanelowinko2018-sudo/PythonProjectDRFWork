from rest_framework import serializers  # Импортируем инструменты DRF для создания сериализаторов (переводчиков в JSON)

from apps.pizza.serializers import (  # Импортируем сериализатор пиццы, чтобы показывать список пицц внутри пиццерии
    PizzaSerializer,
)
from apps.pizza_shop.models import PizzaShopModel  # Импортируем саму модель пиццерии, которую будем переводить


class PizzaShopSerializer(
    serializers.ModelSerializer):  # Создаем класс-переводчик, который автоматически подстраивается под модель
    pizzas = PizzaSerializer(many=True,
                             read_only=True)  # Добавляем вложенный список пицц. many=True означает, что их много (список). read_only=True значит, что мы только показываем их, но не можем создать пиццу при создании пиццерии.

    class Meta:  # внутренний класс для настроек сериализатора
        model = PizzaShopModel  # Указываем, с какой конкретно моделью работает этот переводчик
        fields = ('id', 'name', 'pizzas')  # Перечисляем поля, которые хотим выводить и принимать в формате JSON
        # depth = 1  # настройка, которая могла бы автоматически "раскрывать" вложенные объекты без ручного добавления PizzaSerializer