from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class AgricultureMaterialsVocabularyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.entries = {
            "field": ("ChangeExtent«TransferLifeMatter»Region", "core.agriculture.field", 6),
            "seed": ("BeginLifePart«ChangeExtentLifeMatter»", "core.biology.seed", 7),
            "leaf": ("SurfacePart«ChangeExtentLifeMatter»", "core.biology.leaf", 6),
            "fruit": ("«TransferLifeMatter»Part«ChangeExtentLifeMatter»", "core.biology.fruit", 8),
            "crop/cultivated plant": ("Control«ChangeExtentLifeMatter»Thing", "core.agriculture.crop", 6),
            "grain": ("«BeginLifePart«ChangeExtentLifeMatter»»«TransferLifeMatter»", "core.resources.grain", 10),
            "milk": ("Female«MoveLifeThing»«TransferLifeMatter»Matter", "core.resources.milk", 8),
            "egg": ("BeginLife«MoveLifeThing»Thing", "core.biology.egg", 6),
            "salt": ("Gustation«HardMatter»", "core.materials.salt", 3),
            "clay": ("ChangeForm««ChangeExtentLifeMatter»HaveMatter»", "core.materials.clay", 8),
            "cloth/textile": ("JoinedLowExtentMatter", "core.materials.textile", 4),
            "leather/hide": ("Matter«Surface«LifeMatter»Part»", "core.materials.leather", 5),
            "glass": ("HeatChange«LowExtent«HardMatter»»", "core.materials.glass", 6),
            "fuel": ("Preserve«HeatLightThing»Matter", "core.resources.fuel", 5),
        }

    def test_agriculture_material_words_are_old_names_not_base_roots(self):
        for gloss, (sign, _, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                surface = gloss.split("/", 1)[0].split()[0].capitalize()
                self.assertIsNone(self.language.entry(surface))
                matches = self.language.old_name_entries(sign)
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["gloss"], gloss)

    def test_agriculture_material_old_names_resolve_as_world_kinds(self):
        for gloss, (sign, concept_id, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                result = self.parser.check(f"«{sign}» This.")
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(
                    f"Concept({concept_id})",
                    result.ast.children[0].canonical(),
                )

    def test_agriculture_material_historical_costs_are_recursive_and_frozen(self):
        for gloss, (sign, _, expected_cost) in self.entries.items():
            with self.subTest(gloss=gloss):
                self.assertEqual(
                    self.language.old_name_cost(sign),
                    expected_cost,
                )

    def test_farm_is_a_persistent_agricultural_entity_not_place_or_event_union(self):
        farm = self.language.world_concepts["core.institutions.farm"]
        self.assertEqual(farm["domain"], "agriculture")
        self.assertIn("persistent world Entity", farm["description"])
        self.assertIn("fields", farm["description"])

    def test_culture_relative_staple_is_not_forced_into_universal_core(self):
        self.assertNotIn("core.resources.staple_food", self.language.world_concepts)
        self.assertFalse(self.language.old_name_entries("StapleFood"))
        self.assertEqual(len(self.language.entries), 210)


if __name__ == "__main__":
    unittest.main()
