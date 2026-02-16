#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from dataclasses import dataclass
from typing import List, Dict, Tuple
from datetime import datetime
from collections import defaultdict


@dataclass
class ChemicalLandmark:
    id: str
    name: str
    latitude: float
    longitude: float
    year_discovered: int
    description: str
    scientists: List[str]
    discovery_type: str
    importance_level: int  

    def validate(self) -> Tuple[bool, str]:
        if not (-90 <= self.latitude <= 90):
            return False, f"Invalid latitude: {self.latitude}"
        if not (-180 <= self.longitude <= 180):
            return False, f"Invalid longitude: {self.longitude}"
        if not (1 <= self.importance_level <= 5):
            return False, f"Invalid importance level: {self.importance_level}"
        if self.year_discovered < 1600 or self.year_discovered > datetime.now().year:
            return False, f"Invalid year: {self.year_discovered}"
        return True, "Data is valid"

    def to_dict(self) -> Dict:
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
    def __init__(self):
        self.landmarks: List[ChemicalLandmark] = []
        self.errors: List[str] = []

    def add_landmark(self, landmark: ChemicalLandmark) -> bool:
        is_valid, message = landmark.validate()
        if not is_valid:
            self.errors.append(f"Error for {landmark.name}: {message}")
            return False
        self.landmarks.append(landmark)
        return True

    def get_statistics(self) -> Dict:
        if not self.landmarks:
            return {"total": 0, "message": "No data"}

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
        return [lm for lm in self.landmarks if lm.discovery_type == discovery_type]

    def export_to_json(self, filename: str) -> bool:
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
            self.errors.append(f"Export error: {str(e)}")
            return False

    def print_report(self) -> str:
        if not self.landmarks:
            return "No landmarks in database"

        stats = self.get_statistics()
        report = [
            "\n=== CHEMICAL LANDMARKS REPORT ===",
            f"\nTotal landmarks: {stats['total_landmarks']}",
            f"Average importance: {stats['average_importance']}/5",
            f"Discovery range: {stats['earliest_discovery']}-{stats['latest_discovery']}",
            f"\nDiscovery types: {stats['discovery_types_distribution']}",
            f"\nTop 3 most important landmarks:"
        ]
        for i, landmark_name in enumerate(stats['most_important_landmarks'], 1):
            report.append(f"  {i}. {landmark_name}")

        return "\n".join(report)


def main():
    analyzer = LandmarkAnalyzer()

    landmarks_data = [
        ChemicalLandmark(
            id="land_001",
            name="Mendeleev Memorial",
            latitude=59.9311,
            longitude=30.3644,
            year_discovered=1834,
            description="Monument to the greatest Russian chemist",
            scientists=["Dmitri Mendeleev"],
            discovery_type="monument",
            importance_level=5
        ),
        ChemicalLandmark(
            id="land_002",
            name="Science Laboratory",
            latitude=59.9395,
            longitude=30.3161,
            year_discovered=1925,
            description="Birthplace of chemistry revolution",
            scientists=["Ivan Pavlov", "Nikolay Beketov"],
            discovery_type="synthesis",
            importance_level=4
        ),
        ChemicalLandmark(
            id="land_003",
            name="Academy of Sciences",
            latitude=59.9311,
            longitude=30.3850,
            year_discovered=1775,
            description="First major scientific discoveries center",
            scientists=["Mikhail Lomonosov"],
            discovery_type="discovery",
            importance_level=5
        )
    ]

    for landmark in landmarks_data:
        analyzer.add_landmark(landmark)

    print(analyzer.print_report())

    print("\nMonuments:")
    for landmark in analyzer.get_landmarks_by_type("monument"):
        print(f"  - {landmark.name}")

    if analyzer.export_to_json('landmarks_export.json'):
        print("\nData successfully exported to landmarks_export.json")

    if analyzer.errors:
        print("\nErrors:")
        for error in analyzer.errors:
            print(f"  ⚠️ {error}")


if __name__ == "__main__":
    main()
