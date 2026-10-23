from django.urls import path  # Импортируем функцию path для создания веб-маршрутов (ссылок)

from .views import (  # Импортируем наши классы-обработчики из соседнего файла views.py
    PizzaShopAddPizzaView,
    PizzaShopListView,
)

urlpatterns = [  # Создаем список всех доступных адресов внутри приложения pizza_shop
    path('', PizzaShopListView.as_view()),  # Пустой маршрут (базовый адрес приложения). Метод .as_view() обязателен — он "включает" наш класс, чтобы Django мог с ним работать.

    path('/<int:pk>/pizzas', PizzaShopAddPizzaView.as_view()),  # Маршрут для добавления пиццы. <int:pk> перехватывает число из ссылки (ID пиццерии) и передает его в класс.
]