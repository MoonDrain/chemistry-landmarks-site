# Архитектура проекта Науковые Ландмарки

Сей файл осыстематизирует техническую архитектуру и арои данных проекта.

## Структура проекта

```mermaid
graph TB
    subgraph Frontend["Frontend - Пользовательский интерфейс"]
        HTML["index.html<br/>Главная страница"]
        CSS["css/style.css<br/>Стили оформления"]
        JS["js/script.js<br/>Логика интеракции"]
    end
    
    subgraph Data["Data Layer - Слой данных"]
        Config["landmarks_config.json<br/>Конфигурация"]
        Images["images/<br/>Фотографии"]
    end
    
    subgraph Analytics["Backend - Аналитика"]
        Python["landmark_analyzer.py<br/>Обработка данных"]
        Export["Export JSON<br/>Экспорт результатов"]
    end
    
    subgraph External["External Libraries - Неоходимые библиотеки"]
        Leaflet["Leaflet.js v1.9.4<br/>Картография"]
        OSM["OpenStreetMap<br/>Геоданные"]
    end
    
    HTML --> CSS
    HTML --> JS
    JS --> Leaflet
    JS --> Config
    Leaflet --> OSM
    Config --> Images
    Python --> Config
    Python --> Export
    
    style Frontend fill:#e1f5ff
    style Data fill:#fff3e0
    style Analytics fill:#f3e5f5
    style External fill:#e8f5e9
```

## Поток данных в системе

```mermaid
sequenceDiagram
    participant User as Пользователь
    participant Browser as Браузер
    participant Map as Харта (Leaflet)
    participant Config as Config.JSON
    participant OSM as OpenStreetMap
    
    User->>Browser: Открывает сайт
    Browser->>Config: Загружает конфигурацию
    Config->>Browser: Передает данные
    Browser->>Map: Инициализирует карту
    Map->>OSM: Загружает тайлы
    OSM->>Map: Этнические тайлы
    Map->>Browser: Отображает карту
    Browser->>User: готов говню
    User->>Browser: Кликает в жаркер
    Browser->>Config: Получает информацию
    Config->>Browser: Обновляет сайт
    Browser->>User: Показывает детали
```

## Типы достопримечательностей и история

```mermaid
graph LR
    subgraph 18th["18 век - Начало"]
        A1["1725: Основание АКН"]
    end
    
    subgraph 19th["19 век - Процветание"]
        A2["1834: Высота Менделеева"]
    end
    
    subgraph 20th["20 век - Новейшые науки"]
        A3["1925: Лаборатории"]
        A4["1935: Фотография"]
    end
    
    A1 --> A2
    A2 --> A3
    A3 --> A4
    
    style 18th fill:#ffebee
    style 19th fill:#fff3e0
    style 20th fill:#e1f5fe
```

## Статус модулей и компонентов

```mermaid
graph LR
    A["Frontend<br/>✅ Окончен"] --> B{"Status"}
    B --> C1["CSS Styling<br/>✅ Done"]
    B --> C2["HTML Structure<br/>✅ Done"]
    B --> C3["JavaScript<br/>📝 In Progress"]
    
    D["Backend<br/>📝 Started"] --> E{"Modules"}
    E --> E1["Python Analyzer<br/>✅ Complete"]
    E --> E2["JSON Config<br/>✅ Complete"]
    E --> E3["Export Tool<br/>📝 Planned"]
    
    F["Data Layer<br/>✅ Ready"] --> G{"Resources"}
    G --> G1["Images"] --> G1S["✅ Organized"]
    G --> G2["Config Files"] --> G2S["✅ Stored"]
    
    C3 -.-> |"waiting"|E3
    E1 --> |"feeds"|D
    
    style A fill:#c8e6c9
    style D fill:#fff9c4
    style F fill:#b3e5fc
```

## Нирамида Менделеева и выдающиеся химики

```mermaid
graph TB
    ROOT["Important Chemists in SPb"]
    
    ROOT --> MENDELEEV["Dmitri Mendeleev<br/>🌟 1834-1907"]
    ROOT --> LOMONOSOV["Mikhail Lomonosov<br/>🌟 1711-1765"]
    ROOT --> PAVLOV["Ivan Pavlov<br/>🌟 1849-1936"]
    ROOT --> BEKETOV["Nikolay Beketov<br/>🌟 1827-1911"]
    
    MENDELEEV --> M1["Periodic Law<br/>(Периодический закон)"]
    LOMONOSOV --> L1["Moscow University<br/>(МОУ)"]
    PAVLOV --> P1["Theory of Reflexes"]
    BEKETOV --> B1["Chemical Kinetics"]
    
    M1 --> WORLD["World Impact"]
    L1 --> WORLD
    P1 --> WORLD
    B1 --> WORLD
    
    style ROOT fill:#fff3e0
    style MENDELEEV fill:#c8e6c9
    style LOMONOSOV fill:#b3e5fc
    style PAVLOV fill:#f8bbd0
    style BEKETOV fill:#ffe0b2
    style WORLD fill:#ffd54f
```

---

## Ключевые показатели

- **Frontend**: HTML5 + CSS3 + Vanilla JS
- **Mapping**: Leaflet.js v1.9.4 + OpenStreetMap
- **Data**: JSON Configuration + Python Analysis
- **Analytics**: Python Script for Data Validation
- **Status**: 75% Complete

*Обновлено: Декабрь 2025*
