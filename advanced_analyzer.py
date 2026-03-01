#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Landmark Analyzer with Caching and Optimization
Модуль развитого анализа достопримечательностей с кэшированием
и оптимизацией.
"""

import json
import hashlib
from typing import Dict, List, Optional, Tuple
from functools import lru_cache
from datetime import datetime
import math


class GeoOptimizer:
    """Класс для географических вычислений"""

    @staticmethod
    @lru_cache(maxsize=128)
    def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Вычислить расстояние между двумя точками (формула Хаверсинус)
        Вовращает: расстояние в километрах
        """
        R = 6371  # радиус Вемли в km
        
        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        delta_lat = math.radians(lat2 - lat1)
        delta_lon = math.radians(lon2 - lon1)
        
        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        
        return R * c

    @staticmethod
    def find_nearest_landmarks(landmarks: List[Dict], center_lat: float, center_lon: float, radius_km: float = 10) -> List[Tuple[str, float]]:
        """
        Найти все достопримечательности в радиусе
        Возвращает: Лист кортежей (название, расстояние)
        """
        nearby = []
        for landmark in landmarks:
            dist = GeoOptimizer.calculate_distance(
                center_lat, center_lon,
                landmark['latitude'], landmark['longitude']
            )
            if dist <= radius_km:
                nearby.append((landmark['name'], dist))
        
        return sorted(nearby, key=lambda x: x[1])


class DataCache:
    """Класс для кэширования данных"""

    def __init__(self):
        self.cache = {}
        self.timestamps = {}
        self.cache_ttl = 3600  # 1 час

    def set(self, key: str, value: any) -> None:
        """Установить значение в кэш"""
        self.cache[key] = value
        self.timestamps[key] = datetime.now().timestamp()

    def get(self, key: str) -> Optional[any]:
        """Получить значение из кэша"""
        if key not in self.cache:
            return None
        
        # Проверить TTL
        if datetime.now().timestamp() - self.timestamps[key] > self.cache_ttl:
            del self.cache[key]
            del self.timestamps[key]
            return None
        
        return self.cache[key]

    def clear(self) -> None:
        """Очистить кэш"""
        self.cache.clear()
        self.timestamps.clear()

    def get_stats(self) -> Dict:
        """Получить статистику кэша"""
        return {
            'size': len(self.cache),
            'keys': list(self.cache.keys())
        }


class PerformanceMonitor:
    """Класс для мониторинга производительности"""

    def __init__(self):
        self.metrics = []

    def record_operation(self, operation_name: str, duration_ms: float, success: bool) -> None:
        """Отрасить факт операции"""
        self.metrics.append({
            'operation': operation_name,
            'duration_ms': duration_ms,
            'success': success,
            'timestamp': datetime.now().isoformat()
        })

    def get_average_duration(self, operation_name: str) -> float:
        """Получить среднюю длительность операции"""
        operations = [m for m in self.metrics if m['operation'] == operation_name]
        if not operations:
            return 0
        return sum(m['duration_ms'] for m in operations) / len(operations)

    def get_success_rate(self, operation_name: str) -> float:
        """Получить тасс успеха операции"""
        operations = [m for m in self.metrics if m['operation'] == operation_name]
        if not operations:
            return 0
        successful = sum(1 for m in operations if m['success'])
        return (successful / len(operations)) * 100

    def print_report(self) -> str:
        """Оставить детальный отчёт"""
        if not self.metrics:
            return "No metrics recorded"
        
        report = ["\n=== Отчёт Производительности ==="]
        
        # Найти все операции
        operations = set(m['operation'] for m in self.metrics)
        
        for op in operations:
            avg_duration = self.get_average_duration(op)
            success_rate = self.get_success_rate(op)
            report.append(f"\n{op}:")
            report.append(f"  Средняя длительность: {avg_duration:.2f}ms")
            report.append(f"  Тасс успеха: {success_rate:.1f}%")
        
        return "\n".join(report)


def main():
    """Пример усотребления"""
    
    # Тест геооптимизатора
    print("\n=== Тест Геооптимизации ===")
    
    distance = GeoOptimizer.calculate_distance(59.9311, 30.3609, 59.9250, 30.3650)
    print(f"\nРасстояние от центра: {distance:.2f} km")
    
    # Тест кэша
    print("\n=== Тест Кэша ===")
    cache = DataCache()
    cache.set('landmark_1', {'name': 'Monument', 'year': 1834})
    print(f"\nЗначение: {cache.get('landmark_1')}")
    print(f"Статистика: {cache.get_stats()}")
    
    # Тест мониторинга
    print("\n=== Тест Мониторинга ===")
    monitor = PerformanceMonitor()
    monitor.record_operation('load_data', 125.5, True)
    monitor.record_operation('load_data', 118.3, True)
    monitor.record_operation('validate', 45.2, False)
    monitor.record_operation('validate', 42.8, True)
    print(monitor.print_report())


if __name__ == "__main__":
    main()
