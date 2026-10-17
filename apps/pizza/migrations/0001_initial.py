from django.db import migrations, models  # Импортируем инструменты Django: migrations и models

class Migration(migrations.Migration):  # Создаем класс, который говорит Django, как изменить базу данных

    initial = True  # Это самая первая миграция для этого приложения

    dependencies = [  # Список зависимостей. Так как миграция первая, он пустой
    ]

    operations = [  # Список операций для базы данных
        migrations.CreateModel(  # Операция создания новой таблицы
            name='PizzaModel',  # Имя модели в коде
            fields=[  # Список полей  в таблице
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Уникальный номер, создается автоматически
                ('name', models.CharField(max_length=30)),  # Текстовое поле для названия (ограничение 30 символов)
                ('size', models.IntegerField()),  # Поле для хранения целых чисел (размер)
                ('price', models.FloatField()),  # Поле для хранения дробных чисел (цена)
                ('created_at', models.DateTimeField(auto_now_add=True)),  # Дата создания
                ('updated_at', models.DateTimeField(auto_now=True)),  # Дата обновления
            ],
            options={  # Дополнительные настройки для таблицы
                'db_table': 'pizzas',  # имя таблицы в базе данных MySQL
            },
        ),
    ]