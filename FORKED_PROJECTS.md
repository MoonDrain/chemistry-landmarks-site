# ФОРКНутЫЕ ПРОЕКТЫ

## Leaflet.js - Основная Либлиотека для Работы с Картами

### Описание

**Leaflet** - это открытая библиотека JavaScript для намедленных карт, которая используется в проекте "ХимДостопримечательности Санкт-Петербурга".

### Основные Характеристики

- **Официальный репозиторий**: https://github.com/Leaflet/Leaflet
- **Лицензия**: BSD 2-Clause
- **Версия в проекте**: 1.9.4
- **Назначение**: Отображение маркеров и интерактивных карт

### Почему Мы Форкнули Гтот Проект

1. **Причина Основная**: Leaflet является концептуальнюм ядром проекта "Химдостопримечательности"

2. **Мотивация**: Мы исследуем реализацию новых фичеров для оптимизации начертания маркеров

3. **Открытость**: Open Source проект высокого качества

### Как Мы Используем Leaflet в Проекте

```html
<!-- Подключение Leaflet CSS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
      integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
      crossorigin=""/>

<!-- Leaflet JavaScript -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
        integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
        crossorigin=""></script>
```

### Основные Фичеры, Которыми Мы Пользуемся

| Фичер | Описание | Использание |
|---------|-----------|---------------|
| **L.map()** | Инициализация карты | Основная оболочка |
| **L.tileLayer()** | Загружаем тайлы карт | OpenStreetMap тайлы |
| **L.marker()** | Добавляем маркеры | Точки достопримечательностей |
| **L.popup()** | Калычные юконки | Описание ландмарков |
| **L.control()** | Навигация | Zoom, позиционирование |

### План Перспективных Обулций

- Эксперименты с дополнительными плагинами
- Кустомизация иконки маркеров
- Оптимизация численности маркеров
- Реализация численных фильтров

### Лицензия

```
Copyright (c) 2010-2025, Leaflet
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice...
2. Redistributions in binary form must reproduce the above copyright notice...
```

### ссылки

- Официальный сайт: https://leafletjs.com/
- Новые фичеры: https://leafletjs.com/features.html
- История релизов: https://leafletjs.com/index.html#download

### История Форка

- **Дата форка**: Декабрь 12, 2025
- **Оригинальный репозиторий**: https://github.com/Leaflet/Leaflet
- **Основание**: Необходимо для выполнения практической работы № 2 по организации репозитория в Git/GitHub

---

**Чиме ценный этот проект для нас:**

Leaflet демонстрирует идеальные практики открытого кода: чистая структура, тестирование, документация и коммунити.

*Обновлено: Декабрь 2025*
