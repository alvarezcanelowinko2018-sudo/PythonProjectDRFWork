from django.db import models

from core.models import BaseModel


class PizzaModel(BaseModel):

    name = models.CharField(max_length=30)
    size = models.IntegerField()
    price = models.FloatField()


    pizza_shop = models.ForeignKey('pizza_shop.PizzaShopModel', on_delete=models.CASCADE, related_name='pizzas')


    class Meta:
        db_table = 'pizzas'