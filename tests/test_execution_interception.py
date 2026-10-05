from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class ExecutionInterceptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_magic_can_classify_event_specs(self):
        result = self.assert_valid("Magic Move Self Here.")
        self.assertIn("Magic", result.ast.children[0].canonical())

    def test_magic_can_classify_realized_events(self):
        self.assert_valid("Magic ThisEvent.")

    def test_simple_prevent_frame_still_works(self):
        self.assert_valid("Prevent Move Self Here ThisInterval!")

    def test_bound_prevent_can_intercept_magical_execution_in_region(self):
        result = self.assert_valid(
            "Prevent e:EventSpec Magic $e ThisRegion ThisInterval!"
        )
        canonical = result.ast.children[0].canonical()
        self.assertIn("binder=e:EventSpec", canonical)
        self.assertIn("predicate=Magic", canonical)
        self.assertIn("region=ThisRegion", canonical)

    def test_bound_prevent_can_omit_region_explicitly(self):
        self.assert_valid(
            "Prevent e:EventSpec Magic $e _ ThisInterval!"
        )

    def test_bound_prevent_binder_is_eventspec_typed(self):
        result = self.parser.check(
            "Prevent e:Entity Magic $e ThisRegion ThisInterval!"
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "TypeMismatch")

    def test_bound_prevent_predicate_must_use_candidate(self):
        result = self.parser.check(
            "Prevent e:EventSpec Magic This ThisRegion ThisInterval!"
        )
        self.assertFalse(result.valid)
        self.assertTrue(
            any(
                diagnostic.code == "SemanticallyIncomplete"
                and "EventSpec binder" in diagnostic.message
                for diagnostic in result.diagnostics
            ),
            result.diagnostics,
        )

    def test_event_magic_classification_is_distinct_from_entity_magic_state(self):
        event_magic = self.assert_valid("Magic Move Self Here.")
        entity_magic = self.assert_valid("Magic This.")
        self.assertNotEqual(
            event_magic.ast.children[0].canonical(),
            entity_magic.ast.children[0].canonical(),
        )


if __name__ == "__main__":
    unittest.main()
