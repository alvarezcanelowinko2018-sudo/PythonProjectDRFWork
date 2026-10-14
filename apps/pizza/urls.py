from django.urls import path  # Импортируем функцию path, которая связывает URL-адреса с нашим кодом
from .views import PizzaRetrieveUpdateDestroyView, PizzaListCreateView  # Импортируем наши классы-представления, которые будут обрабатывать запросы пользователей

urlpatterns = [  # Создаем список всех URL-адресов (маршрутов) для этого приложения
    path("", PizzaListCreateView.as_view()),  # Пустой путь (базовый URL, например /pizzas/): привязываем его к классу, который выдает список всех пицц или создает новую (метод as_view() обязателен для классов)

    path("<int:pk>", PizzaRetrieveUpdateDestroyView.as_view()),  # Путь с числом (например, /pizzas/5): <int:pk> ловит ID (primary key) конкретной пиццы из ссылки и передает классу, который ее покажет, обновит или удалит
]