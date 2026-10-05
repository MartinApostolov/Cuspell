from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class BasicAnatomyVocabularyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.entries = {
            "head": ("Know«LifeMatter»Part", "core.anatomy.head", 4),
            "face": ("VisionSaySurface«Know«LifeMatter»Part»", "core.anatomy.face", 7),
            "arm": ("ControlMove«LifeMatter»Part", "core.anatomy.arm", 5),
            "leg": ("Move«LifeMatter»Part", "core.anatomy.leg", 4),
            "foot": ("MoveTouch«LifeMatter»Part", "core.anatomy.foot", 5),
            "finger": ("ControlPart«Control«LifeMatter»Part»", "core.anatomy.finger", 6),
            "nose": ("Olfaction«LifeMatter»Part", "core.anatomy.nose", 4),
            "tooth": ("HardEat«LifeMatter»Part", "core.anatomy.tooth", 5),
            "tongue": ("SayEat«LifeMatter»Part", "core.anatomy.tongue", 5),
            "heart": ("Move«LiquidLifeMatter»«Use«LifeMatter»Part»", "core.anatomy.heart", 8),
            "brain": ("Know«Use«LifeMatter»Part»", "core.anatomy.brain", 5),
            "hair": ("ChangeExtentSurface«LifeMatter»Part", "core.anatomy.hair", 6),
        }

    def test_basic_anatomy_words_are_old_names_not_base_roots(self):
        for gloss, (sign, _, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                self.assertIsNone(self.language.entry(gloss.capitalize()))
                matches = self.language.old_name_entries(sign)
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["gloss"], gloss)

    def test_basic_anatomy_old_names_resolve_as_world_kinds(self):
        for gloss, (sign, concept_id, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                result = self.parser.check(f"«{sign}» This.")
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(
                    f"Concept({concept_id})",
                    result.ast.children[0].canonical(),
                )

    def test_basic_anatomy_historical_costs_are_recursive_and_frozen(self):
        for gloss, (sign, _, expected_cost) in self.entries.items():
            with self.subTest(gloss=gloss):
                self.assertEqual(
                    self.language.old_name_cost(sign),
                    expected_cost,
                )

    def test_anatomy_batch_does_not_change_base_semantic_inventory(self):
        self.assertEqual(len(self.language.entries), 217)


if __name__ == "__main__":
    unittest.main()
