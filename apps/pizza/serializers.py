from rest_framework import serializers

from apps.pizza.models import PizzaModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = (
            'id',
            'name',
            'size',
            'price',
            'pizza_shop',  # Поле обязательно для привязки к магазину
            'updated_at',
            'created_at',
        )
