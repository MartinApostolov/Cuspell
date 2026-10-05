from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class ArtRitualCultureVocabularyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.entries = {
            "temple": ("Worship«JoinedInThing»", "core.religion.temple", 4),
            "shrine": ("Worship«UseThing»", "core.religion.shrine", 3),
            "priest": ("WorshipAuthority«Know«MoveLifeThing»»", "core.roles.priest", 6),
            "ritual/ceremony": ("RuleSequence", "core.events.ritual", 2),
            "prayer": ("SayWorship", "core.events.prayer", 2),
            "sacrifice/offering": ("TransferEndHaveWorship", "core.events.sacrifice", 4),
            "dance": ("RepeatMove", "core.events.dance", 2),
            "performance": ("SensePurpose", "core.events.performance", 2),
            "game/sport": ("RuleAttempt", "core.events.game", 2),
            "festival/feast": ("GroupHappyEat", "core.events.festival", 3),
            "story/tale": ("Sequence«MeaningSign»", "core.information.story", 3),
            "music/composition": ("HearingSequence", "core.information.music", 2),
            "song": ("Say«HearingSequence»", "core.information.song", 3),
            "musical instrument": ("«HearingSequence»«UseThing»", "core.artifacts.musical_instrument", 4),
            "image/painting": ("Vision«PersistSignThing»", "core.artifacts.image", 4),
            "sculpture": ("Form«PersistSignThing»", "core.artifacts.sculpture", 4),
        }

    def test_art_ritual_words_are_old_names_not_base_roots(self):
        for gloss, (sign, _, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                surface = gloss.split("/", 1)[0].split()[0].capitalize()
                self.assertIsNone(self.language.entry(surface))
                matches = self.language.old_name_entries(sign)
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["gloss"], gloss)

    def test_historical_costs_are_recursive_and_frozen(self):
        for gloss, (sign, _, expected_cost) in self.entries.items():
            with self.subTest(gloss=gloss):
                self.assertEqual(self.language.old_name_cost(sign), expected_cost)

    def test_entity_kinds_keep_normal_entity_predication(self):
        result = self.parser.check("«Worship«JoinedInThing»» This.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIn(
            "Concept(core.religion.temple)",
            result.ast.children[0].canonical(),
        )

    def test_event_kinds_classify_event_specs(self):
        result = self.parser.check("«RuleSequence» Move Self Here.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIn(
            "Concept(core.events.ritual)",
            result.ast.children[0].canonical(),
        )

    def test_event_kinds_classify_actual_events(self):
        result = self.parser.check("«RuleSequence» ThisEvent.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIn(
            "Concept(core.events.ritual)",
            result.ast.children[0].canonical(),
        )

    def test_information_kinds_classify_information_values(self):
        result = self.parser.check("«Sequence«MeaningSign»» Question True.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIn(
            "Concept(core.information.story)",
            result.ast.children[0].canonical(),
        )

    def test_typed_kinds_reject_wrong_subject_domain_without_new_roots(self):
        wrong = self.parser.check("«RuleSequence» This.")
        self.assertFalse(wrong.valid)
        self.assertEqual(len(self.language.entries), 215)
        self.assertEqual(
            self.language.world_concepts["core.events.ritual"]["classifies_types"],
            ["EventSpec", "Event"],
        )


if __name__ == "__main__":
    unittest.main()
