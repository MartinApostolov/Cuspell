from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class CalendarDailyLifeVocabularyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.entries = {
            "day/calendar day": ("AwakeSleepExtent", "core.time.day", 3),
            "night": ("SleepExtent", "core.time.night", 2),
            "season": ("ChangeHeatExtent", "core.time.season", 3),
            "year": ("Repeat«ChangeHeatExtent»", "core.time.year", 4),
            "month/calendar month": ("Part«Repeat«ChangeHeatExtent»»", "core.time.month", 5),
            "date/calendar date": ("Name«RepeatDuration«PersistSignThing»»", "core.information.date", 6),
        }

    def test_calendar_words_are_old_names_not_base_roots(self):
        for gloss, (sign, _, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                surface = gloss.split("/", 1)[0].split()[0].capitalize()
                self.assertIsNone(self.language.entry(surface))
                matches = self.language.old_name_entries(sign)
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["gloss"], gloss)

    def test_calendar_historical_costs_are_recursive_and_frozen(self):
        for gloss, (sign, _, expected_cost) in self.entries.items():
            with self.subTest(gloss=gloss):
                self.assertEqual(self.language.old_name_cost(sign), expected_cost)

    def test_calendar_period_kinds_classify_time_intervals(self):
        for sign, concept_id in (
            ("AwakeSleepExtent", "core.time.day"),
            ("SleepExtent", "core.time.night"),
            ("ChangeHeatExtent", "core.time.season"),
            ("Repeat«ChangeHeatExtent»", "core.time.year"),
            ("Part«Repeat«ChangeHeatExtent»»", "core.time.month"),
        ):
            with self.subTest(sign=sign):
                result = self.parser.check(f"«{sign}» ThisInterval.")
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(
                    f"Concept({concept_id})",
                    result.ast.children[0].canonical(),
                )

    def test_date_kind_classifies_information_not_time_itself(self):
        sign = "Name«RepeatDuration«PersistSignThing»»"
        result = self.parser.check(f"«{sign}» ThisInformation.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIn(
            "Concept(core.information.date)",
            result.ast.children[0].canonical(),
        )

    def test_calendar_kinds_reject_wrong_subject_domains(self):
        self.assertFalse(self.parser.check("«AwakeSleepExtent» This.").valid)
        self.assertFalse(
            self.parser.check(
                "«Name«RepeatDuration«PersistSignThing»» ThisInterval."
            ).valid
        )

    def test_current_day_is_compositionally_selectable(self):
        node = self.parser.parse_phrase(
            "Unique Collect d:TimeInterval "
            "And {«AwakeSleepExtent» $d,During Now $d}",
            expected_type="TimeInterval",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "TimeInterval")

    def test_age_remains_explicit_elapsed_time_not_a_root(self):
        self.assertIsNone(self.language.entry("Age"))
        elapsed = self.parser.parse_phrase(
            "Extent Interval Begin ThisEvent Now",
            expected_type="Quantity:Time",
        )
        self.assertNotIsInstance(elapsed, Diagnostic, elapsed)
        self.assertEqual(elapsed.type, "Quantity:Time")
        claim = self.parser.check(
            "Equal Extent Interval Begin ThisEvent Now «DurationUnit» @@."
        )
        self.assertTrue(claim.valid, claim.diagnostics)
        self.assertEqual(len(self.language.entries), 217)


if __name__ == "__main__":
    unittest.main()
