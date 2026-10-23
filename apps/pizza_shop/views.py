from rest_framework import status  # Импортируем статусы ответов (например, 201 Created)
from rest_framework.generics import RetrieveUpdateDestroyAPIView  # Импортируем готовые классы представлений
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response  # Импортируем класс для отправки готового ответа пользователю

from apps.pizza.models import (  # Импортируем модель пиццы (в этом коде напрямую не используется, можно удалить)
    PizzaModel,
)
from apps.pizza.serializers import PizzaSerializer  # Импортируем сериализатор пиццы для создания новой записи
from apps.pizza_shop.models import PizzaShopModel  # Импортируем модель пиццерии
from apps.pizza_shop.serializer import PizzaShopSerializer  # Импортируем сериализатор пиццерии


class PizzaShopListView(
    ListCreateAPIView):  # Класс "из коробки" для выдачи списка пиццерий (GET) и создания новых (POST)
    serializer_class = PizzaShopSerializer  # Указываем сериализатор для перевода данных
    queryset = PizzaShopModel.objects.all()  # Базовый запрос к БД: берем абсолютно все пиццерии


class PizzaShopAddPizzaView(GenericAPIView):  # Кастомный класс для добавления новой пиццы в конкретную пиццерию
    queryset = PizzaShopModel.objects.all()  # Базовый запрос, который нужен встроенному методу get_object() для поиска пиццерии

    def post(self, *args, **kwargs):  # Вручную описываем логику создания (POST-запрос)
        pizza_shop = self.get_object()  # Автоматически находим конкретную пиццерию по ID из URL
        data = self.request.data  # Достаем JSON-данные, которые пользователь прислал в теле запроса
        serializer = PizzaSerializer(
            data=data)  # Передаем эти данные в сериализатор ПИЦЦЫ (мы создаем пиццу, а не пиццерию)
        serializer.is_valid(
            raise_exception=True)  # Проверяем, корректны ли присланные данные (если нет — выбрасываем 400 Bad Request)
        serializer.save(
            pizza_shop=pizza_shop)  # Сохраняем новую пиццу в БД и принудительно привязываем её к найденной пиццерии

        shop_serializer = PizzaShopSerializer(
            pizza_shop)  # Собираем свежие данные пиццерии (теперь в ней есть новая пицца)
        return Response(shop_serializer.data,
                        status=status.HTTP_201_CREATED)  # Возвращаем пользователю обновленную пиццерию и статус "Создано"