from django.db.models import QuerySet  # импортируем тип QuerySet (он означает список объектов из базы)
from django.http import QueryDict  # Импортируем тип данных словаря, в котором хранятся параметры URL

from rest_framework.exceptions import ValidationError  # импортируем ошибку из DRF, а не из встроенного Django

from apps.pizza.models import PizzaModel  # Импортируем нашу модель пиццы


def filter_pizza(query: QueryDict) -> QuerySet:  # функция возвращает список записей
    qs = PizzaModel.objects.all()  # Делаем базовый запрос: получаем абсолютно все пиццы из базы данных

    for k, v in query.items():  # Запускаем цикл по всем переданным параметрам
        match k:  # Проверяем название параметра
            case 'price_gt':  # Если параметр называется "цена больше чем"
                qs = qs.filter(price__gt=v)  # Фильтруем: оставляем только те, что дороже v
            case 'price_lt':  # Если параметр называется "цена меньше чем"
                qs = qs.filter(price__lt=v)  # Фильтруем: оставляем только те, что дешевле v
            case _:  # Если прислали любой другой (неразрешенный) параметр
                raise ValidationError({'detail': f'"{k}" not allowed'})  # Выбрасываем ошибку валидации из DRF

    return qs  # Возвращаем итоговый отфильтрованный список пицц