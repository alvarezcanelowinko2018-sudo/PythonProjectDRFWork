from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.pizza.filter import filter_pizza
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer

# --- ВАРИАНТ 1: Ручной APIView ---
# Отличие: Здесь всё делается полностью вручную. Мы сами пишем функции get и post,
# сами ищем пиццу в базе (try-except), сами вызываем сохранение. Кода получается очень много.

# class PizzaListCreateView(APIView):
#     def get(self, request: Request, *args, **kwargs):
#         qs = filter_pizza(request.query_params)
#         serializer = PizzaSerializer(qs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         serializer = PizzaSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# class PizzaRetrieveUpdateDestroyView(APIView):
#     def get(self, request, pk, *args, **kwargs):
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = PizzaSerializer(pizza)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# --- ВАРИАНТ 2: GenericAPIView + Mixins ---
# Отличие: Часть работы автоматизирована. За сохранение и выдачу отвечают готовые миксины,
# поэтому мы просто вызываем super().list() или super().create().
# Но мы всё ещё вынуждены вручную привязывать методы HTTP (def get) к этим миксинам.

# class PizzaListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     serializer_class = PizzaSerializer
#     def get_queryset(self):
#         return filter_pizza(self.request.query_params)
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)


# --- ВАРИАНТ 3: Готовые Generic Views (Финальный) ---
# Отличие: Максимальная автоматизация. Эти классы "из коробки" знают, что делать с GET и POST.
# Нам нужно указать им модель и сериализатор, остальное работает само.

class PizzaListCreateView(ListCreateAPIView):
    # Класс "из коробки" сам выдает список (GET) и создает записи (POST), проставляя нужные статусы (200, 201).
    serializer_class = PizzaSerializer

    def get_queryset(self):
        # Заменяем стандартный поиск объектов, чтобы прикрутить нашу кастомную функцию фильтрации
        request: Request = self.request
        return filter_pizza(request.query_params)


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # Класс "из коробки" сам обрабатывает чтение, обновление и удаление одной записи.
    # Сам берет ID из ссылки и выдает ошибку 404, если пицца не найдена в базе.
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['get', 'put', 'delete']