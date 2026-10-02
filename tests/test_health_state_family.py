from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class HealthStateFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_health_and_pain_are_ordered_attributes(self):
        for surface in ("Health", "Pain"):
            with self.subTest(surface=surface):
                entry = self.language.entry(surface)
                self.assertIsNotNone(entry)
                self.assertEqual(entry.data.get("atom_type"), "AttributeDescriptor")
                self.assertEqual(entry.data.get("descriptor_value_type"), "EvaluationValue")

        self.valid("More Health This Health Self.")
        self.valid("More Pain This Pain Self.")
        self.valid("HighHealth This.")
        self.valid("LowPain This.")

    def test_ill_is_a_persistent_pathological_state(self):
        ill = self.language.entry("Ill")
        self.assertIsNotNone(ill)
        self.assertEqual(ill.category, "Property")
        self.assertTrue(ill.data.get("state_predicate"))

        self.valid("Ill This.")
        self.valid("Happen Begin Ill This.")
        self.valid("Happen End Ill This.")

    def test_health_pain_damage_and_ill_remain_distinct(self):
        meanings = {
            "health": self.valid("LowHealth This.").ast.children[0].canonical(),
            "pain": self.valid("HighPain This.").ast.children[0].canonical(),
            "damage": self.valid("HighDamage This.").ast.children[0].canonical(),
            "ill": self.valid("Ill This.").ast.children[0].canonical(),
        }
        self.assertEqual(len(set(meanings.values())), len(meanings))

    def test_cross_combinations_are_not_forced_contradictions(self):
        for source in (
            "And {HighPain This,LowDamage This}.",
            "And {HighDamage This,LowPain This}.",
            "And {Ill This,HighHealth This}.",
            "And {Not Ill This,LowHealth This}.",
        ):
            with self.subTest(source=source):
                self.valid(source)

    def test_heal_remains_compositional_not_a_core_root(self):
        self.assertIsNone(self.language.entry("Heal"))


if __name__ == "__main__":
    unittest.main()
