from rest_framework import \
    serializers  # Импортируем инструменты для работы с сериализаторами из Django REST Framework (DRF)

from apps.pizza.models import PizzaModel  # Импортируем нашу модель пиццы, чтобы сериализатор знал, с чем работает


class PizzaSerializer(
    serializers.ModelSerializer):  # Создаем класс сериализатора, который наследуется от умного ModelSerializer
    class Meta:  # Класс настроек, где мы говорим DRF, как именно обрабатывать нашу модель
        model = PizzaModel  # Указываем, что этот сериализатор жестко привязан к таблице PizzaModel
        fields = ('id', 'name', 'size', 'price', 'updated_at',
                  'created_at')  # Перечисляем поля, которые нужно конвертировать в JSON (и обратно)


    # ModelSerializer (который мы использовали выше) делает всё это автоматически

    # id = serializers.IntegerField(read_only=True)  # Ручное создание поля id (read_only значит, что мы его только читаем)
    # name = serializers.CharField(max_length=30)  # Ручное создание текстового поля
    # size = serializers.IntegerField()  # Ручное создание числового поля
    # price = serializers.FloatField()  # Ручное создание поля для цены
    #
    # created_at = serializers.DateTimeField(read_only=True)  # Дата создания (только для чтения)
    # updated_at = serializers.DateTimeField(read_only=True)  # Дата обновления (только для чтения)
    #
    # def create(self, validated_data:dict):  # Метод для сохранения новой пиццы в базу
    #     return PizzaModel.objects.create(**validated_data)  # Распаковываем проверенные данные и создаем запись
    #
    # def update(self, instance,  validated_data:dict):  # Метод для обновления существующей пиццы
    #     for k, v in validated_data.items():  # Перебираем все переданные для обновления поля
    #         setattr(instance, k, v)  # Устанавливаем новые значения (v) для соответствующих полей (k) нашего объекта (instance)
    #     instance.save()  # Сохраняем обновленный объект в базу данных
    #     return instance  # Возвращаем обновленную пиццу