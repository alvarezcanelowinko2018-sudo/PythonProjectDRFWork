from rest_framework.request import Request  # Импортируем тип запроса из DRF для аннотации
from apps.pizza.filter import filter_pizza  # Импортируем нашу исправленную функцию фильтрации
from apps.pizza.models import PizzaModel  # Импортируем модель пиццы для базового запроса
from apps.pizza.serializers import PizzaSerializer  # Импортируем сериализатор для перевода данных в JSON
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView  # Импортируем мощные готовые классы DRF

class PizzaListCreateView(ListCreateAPIView):  # Класс "из коробки" сам обрабатывает GET (выдача списка) и POST (создание). Сам отдает статусы 200 OK и 201 Created.
    serializer_class = PizzaSerializer  # Указываем сериализатор, который "из коробки" будет проверять и конвертировать данные

    def get_queryset(self):  # Метод "из коробки", мы его переопределяем, чтобы не просто выдать все пиццы, а применить фильтр
        request: Request = self.request  # Получаем текущий запрос (в нём лежат параметры из адресной строки)
        return filter_pizza(request.query_params)  # Передаем эти параметры в нашу функцию и возвращаем отфильтрованный результат


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):  # Класс "из коробки" сам обрабатывает GET (одна запись), PUT (обновление) и DELETE (удаление).
    # "Из коробки" использует метод get_object(), чтобы найти пиццу по ID из URL. Сам выдает статусы 200 OK, 204 No Content или 404 Not Found.
    serializer_class = PizzaSerializer  # Указываем сериализатор для работы с одной записью
    queryset = PizzaModel.objects.all()  # Базовый запрос, внутри которого метод get_object() будет искать нужную пиццу
    http_method_names = ['get', 'put', 'delete']  # Явно разрешаем принимать только эти три метода