#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Landmark Data Analyzer
Настоящий модуль используется для анализа и валидации
данных о химических достопримечательностях Санкт-Петербурга.

Основные функции:
- Проверка наличия географических координат
- Количественные аналитика данных
- Статистика по датам открытий
"""

import json
import re
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
from datetime import datetime
from collections import defaultdict


@dataclass
class ChemicalLandmark:
    """Класс для репрезентации химической достопримечательности"""
    id: str
    name: str
    latitude: float
    longitude: float
    year_discovered: int
    description: str
    scientists: List[str]
    discovery_type: str  # тип: 'synthesis', 'analysis', 'discovery', 'monument'
    importance_level: int  # 1-5, где 5 - наивысшая

    def validate(self) -> Tuple[bool, str]:
        """Проверить корректность данных"""
        if not (-90 <= self.latitude <= 90):
            return False, f"Некорректная широта: {self.latitude}"
        if not (-180 <= self.longitude <= 180):
            return False, f"Некорректная долгота: {self.longitude}"
        if not (1 <= self.importance_level <= 5):
            return False, f"Опасная степень значимости: {self.importance_level}"
        if self.year_discovered < 1600 or self.year_discovered > datetime.now().year:
            return False, f"Нереалистичный год: {self.year_discovered}"
        return True, "Данные корректные"

    def to_dict(self) -> Dict:
        """Преобразовать в словарь"""
        return {
            'id': self.id,
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'year_discovered': self.year_discovered,
            'description': self.description,
            'scientists': self.scientists,
            'discovery_type': self.discovery_type,
            'importance_level': self.importance_level
        }


class LandmarkAnalyzer:
    """Класс для анализа и обработки данных достопримечательностей"""

    def __init__(self):
        self.landmarks: List[ChemicalLandmark] = []
        self.errors: List[str] = []

    def add_landmark(self, landmark: ChemicalLandmark) -> bool:
        """Добавить новую достопримечательность"""
        is_valid, message = landmark.validate()
        if not is_valid:
            self.errors.append(f"Ошибка для {landmark.name}: {message}")
            return False
        self.landmarks.append(landmark)
        return True

    def get_statistics(self) -> Dict:
        """Получить статистику по достопримечательностям"""
        if not self.landmarks:
            return {"total": 0, "message": "Нет данных"}

        discovery_types = defaultdict(int)
        avg_importance = 0
        years = []

        for landmark in self.landmarks:
            discovery_types[landmark.discovery_type] += 1
            avg_importance += landmark.importance_level
            years.append(landmark.year_discovered)

        return {
            "total_landmarks": len(self.landmarks),
            "average_importance": round(avg_importance / len(self.landmarks), 2),
            "earliest_discovery": min(years),
            "latest_discovery": max(years),
            "discovery_types_distribution": dict(discovery_types),
            "most_important_landmarks": [
                lm.name for lm in sorted(
                    self.landmarks,
                    key=lambda x: x.importance_level,
                    reverse=True
                )[:3]
            ]
        }

    def get_landmarks_by_type(self, discovery_type: str) -> List[ChemicalLandmark]:
        """Получить достопримечательности по типу"""
        return [lm for lm in self.landmarks if lm.discovery_type == discovery_type]

    def export_to_json(self, filename: str) -> bool:
        """Экспортировать данные в JSON"""
        try:
            data = {
                'landmarks': [lm.to_dict() for lm in self.landmarks],
                'statistics': self.get_statistics(),
                'export_date': datetime.now().isoformat()
            }
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            self.errors.append(f"Ошибка ЭКСПОРТА: {str(e)}")
            return False

    def print_report(self) -> str:
        """Набечатать отчёт
        НОВОЕ ПОКОЛЕНИЕ ХИМИЧЕСКИХ ОТКРЫТИЙ
        """
        if not self.landmarks:
            return "ЭОНОМНая база данных!"

        stats = self.get_statistics()
        report = [
            "\n=== ОТЧЁТ О ХИМИЧЕСКИХ ДОСТОПРИМЕЧАТЕЛЬНОСТПХ ===",
            f"\nВсего достопримечательностей: {stats['total_landmarks']}",
            f"Средняя важность: {stats['average_importance']}/5",
            f"Нашие открытия: {stats['earliest_discovery']}-{stats['latest_discovery']}",
            f"\nОряд исоредіжх работ: {stats['discovery_types_distribution']}",
            f"\nТоп-3 важнейших достопримечательностей:"
        ]
        for i, landmark_name in enumerate(stats['most_important_landmarks'], 1):
            report.append(f"  {i}. {landmark_name}")

        return "\n".join(report)


def main():
    """Основная функция для тестирования"""
    analyzer = LandmarkAnalyzer()

    # Примеры данных
    landmarks_data = [
        ChemicalLandmark(
            id="land_001",
            name="Наментов трон (Партгиеноу)",
            latitude=59.9311,
            longitude=30.3644,
            year_discovered=1834,
            description="Памятник крупнейшему русскому химику",
            scientists=["Dmitri Mendeleev"],
            discovery_type="monument",
            importance_level=5
        ),
        ChemicalLandmark(
            id="land_002",
            name="Лаборатория Науки",
            latitude=59.9395,
            longitude=30.3161,
            year_discovered=1925,
            description="Место где начиналась революция в химии",
            scientists=["Ivan Pavlov", "Nikolay Beketov"],
            discovery_type="synthesis",
            importance_level=4
        ),
        ChemicalLandmark(
            id="land_003",
            name="Академия васпитания",
            latitude=59.9311,
            longitude=30.3850,
            year_discovered=1775,
            description="Первая поля численных открытий",
            scientists=["Mikhail Lomonosov"],
            discovery_type="discovery",
            importance_level=5
        )
    ]

    for landmark in landmarks_data:
        analyzer.add_landmark(landmark)

    # Овывод наиденных неопределённых
    print(analyzer.print_report())

    # Оайск типов
    print("\nОткрытия монументов:")
    for landmark in analyzer.get_landmarks_by_type("monument"):
        print(f"  - {landmark.name}")

    # Экспорт
    if analyzer.export_to_json('landmarks_export.json'):
        print("\nДанные успешно экспортированы в landmarks_export.json")

    if analyzer.errors:
        print("\nОшибки:")
        for error in analyzer.errors:
            print(f"  ⚠️ {error}")


if __name__ == "__main__":
    main()
