# Point Of Interest

## Описание
Point of Interest - это Django-приложение для управления точками интереса (Points of Interest, POI). Приложение предоставляет RESTful API для добавления, просмотра, обновления, удаления и фильтрации POI.

## Технологии
* Python 3.12
* Django 5.1.3
* Django REST Framework
* sqlite

## Установка и запуск
1. Клонируйте репозиторий:
```
git clone git@github.com:sayat-a/PointOfInterest.git
cd <папка проекта>
```
2. Установите зависимости и настройте базу данных:
```
make install
```
3. Запустите сервер разработки:
```
make run
```

## Функциональность
API поддерживает следующие операции:
**Добавление новых точек интереса**
```
POST /api/poi/
```

**Просмотр всех точек интереса**
```
GET /api/poi/
```

**Просмотр конкретной точки интереса**
```
GET /api/poi/<id>/
```

**Обновление точки интереса**

Полное: ```PUT /api/poi/<id>/```
Частичное: ```PATCH /api/poi/<id>/```

**Удаление точки интереса**
```
DELETE /api/poi/<id>/
```

Фильтрация точек по категории
```
GET /api/poi/?search=<category>
```
  
## Примеры использования API

**Создание точек**
[![asciicast](https://asciinema.org/a/qNZMkKpxFR1grEhBIgWaqCfJ9.svg)](https://asciinema.org/a/qNZMkKpxFR1grEhBIgWaqCfJ9)


**Просмотр всех точек, точки по id, точки по категории**
[![asciicast](https://asciinema.org/a/ZfrSAiKarzcRjHmNmhRhSfEXn.svg)](https://asciinema.org/a/ZfrSAiKarzcRjHmNmhRhSfEXn)
