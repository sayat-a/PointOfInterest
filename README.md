# Point Of Interest

## Description
Point of Interest - это Django-приложение для управления точками интереса (Points of Interest, POI). Приложение предоставляет RESTful API для добавления, просмотра, обновления, удаления и фильтрации POI.

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
![demo](https://asciinema.org/a/qNZMkKpxFR1grEhBIgWaqCfJ9)

**Просмотр всех точек, точки по id, точки по категории**
![demo](https://asciinema.org/a/ZfrSAiKarzcRjHmNmhRhSfEXn)