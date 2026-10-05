from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class GeographyWeatherVocabularyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.entries = {
            "land": ("SolidMatterRegion", "core.geography.land", 3),
            "soil": ("«ChangeExtentLifeMatter»HaveMatter", "core.materials.soil", 6),
            "sand": ("LowExtent«HardMatter»", "core.materials.sand", 4),
            "river": ("Move«LiquidMatter»Path", "core.geography.river", 4),
            "lake": ("LowExtent«LiquidMatter»Region", "core.geography.lake", 5),
            "sea/ocean": ("HighExtent«LiquidMatter»Region", "core.geography.sea", 5),
            "mountain": ("HighExtent«HardMatter»Region", "core.geography.mountain", 5),
            "hill": ("LowExtent«HighExtent«HardMatter»Region»", "core.geography.hill", 7),
            "island": ("«SolidMatterRegion»In«LiquidMatter»", "core.geography.island", 6),
            "shore/coast": ("Touch«LiquidMatter»«SolidMatterRegion»", "core.geography.shore", 6),
            "forest": ("Group«HighExtentHard«ChangeExtentLifeMatter»»Region", "core.geography.forest", 9),
            "sky": ("High«LifeGasMatter»Region", "core.geography.sky", 5),
            "cloud": ("«LiquidMatter»In«LifeGasMatter»Thing", "core.weather.cloud", 7),
            "rain": ("Fall«LiquidMatter»Thing", "core.weather.rain", 4),
            "ice": ("Solid«LiquidMatter»Thing", "core.materials.ice", 4),
            "snow": ("Fall«Solid«LiquidMatter»Thing»", "core.weather.snow", 5),
            "wind": ("Move«LifeGasMatter»Thing", "core.weather.wind", 5),
            "storm": ("HighExtent«Move«LifeGasMatter»Thing»", "core.weather.storm", 7),
        }

    def test_geography_weather_words_are_old_names_not_base_roots(self):
        for gloss, (sign, _, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                surface = gloss.split("/", 1)[0].capitalize()
                self.assertIsNone(self.language.entry(surface))
                matches = self.language.old_name_entries(sign)
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["gloss"], gloss)

    def test_geography_weather_old_names_resolve_as_world_kinds(self):
        for gloss, (sign, concept_id, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                result = self.parser.check(f"«{sign}» This.")
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(
                    f"Concept({concept_id})",
                    result.ast.children[0].canonical(),
                )

    def test_geography_weather_historical_costs_are_recursive_and_frozen(self):
        for gloss, (sign, _, expected_cost) in self.entries.items():
            with self.subTest(gloss=gloss):
                self.assertEqual(
                    self.language.old_name_cost(sign),
                    expected_cost,
                )

    def test_geography_weather_batch_does_not_change_base_inventory(self):
        self.assertEqual(len(self.language.entries), 213)


if __name__ == "__main__":
    unittest.main()
