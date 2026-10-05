from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class AdvancedSpellPressureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_flat_concurrent_teleport_needs_no_parentheses(self):
        self.assert_valid("Concurrent EndAtSelfHere BeginAtSelfThere!")

    def test_existing_language_covers_several_advanced_effect_families(self):
        examples = {
            "dispel_magic": "EndMagic This!",
            "fear": "Begin FearYouThis!",
            "fly_like_capability": "Begin CanYouMoveYouThere!",
            "gaseous_form": "Change You Gas!",
            "dimension_door_like": "Concurrent EndAtYouHere BeginAtYouThere!",
            "polymorph_form_slice": "Change You Form FormThis!",
            "domination": "Begin ControlSelfYou!",
            "modify_memory_remove": "EndRememberYouThisInformation!",
            "modify_memory_add": "BeginRememberYouThisInformation!",
            "disintegrate_existence_slice": "EndExist This!",
            "raise_dead_life_slice": "BeginLife This!",
            "hold_monster_like": "Persist AtYouThere ThisInterval!",
        }
        for name, source in examples.items():
            with self.subTest(name=name, source=source):
                self.assert_valid(source)

    def test_advanced_pressure_does_not_silently_add_spell_named_roots(self):
        for surface in (
            "Counterspell",
            "Scrying",
            "Illusion",
            "Conjure",
            "Teleport",
            "TimeStop",
            "Wish",
        ):
            with self.subTest(surface=surface):
                self.assertIsNone(self.language.entry(surface))


if __name__ == "__main__":
    unittest.main()
