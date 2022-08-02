# API для Yatube. V1

*Общедоступный API для просмотра ленты постов проекта Yatube.
Авторизированные пользователи могут выкладывать публикации и комментировать.*
***


### Примеры запросов

|Действие|Тип запроса|Адрес|
|---|---|---|
|__Получение ленты постов__|GET|.../api/v1/posts/|
|__Публикация поста__|POST|.../api/v1/posts/|
|__Редактирование поста__|PUT / PUTCH|.../api/v1/posts/<id>/|
|__Добавить комментарий__|POST|.../api/v1/comments/|
|__Удалить комментарий__|DELETE|.../api/v1/comments/<id>/|
|__Проверить список подписок__|GET|.../api/v1/follow/|


### Технологии

- [Django] - веб-фреймворк на Python.
- [djoser] - REST- реализация системы аутентификации Django.
- [Django REST framework] - инструментарий для создания веб-API.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:natalie731/api_final_yatube.git
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Разработчики

[Банникова Наталья]

[Команда Яндекс.Практикум]

[//]: #

   [Django REST framework]: <https://www.django-rest-framework.org/>
   [Django]: <https://www.djangoproject.com/>
   [djoser]: <https://pypi.org/project/djoser/>

   [Банникова Наталья]: <https://github.com/natalie731>
   [Команда Яндекс.Практикум]: <https://practicum.yandex.ru/>
