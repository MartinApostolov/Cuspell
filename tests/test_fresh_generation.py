from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class FreshGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_create_allocates_fresh_entity_with_objective_profile(self):
        result = self.assert_valid(
            "Create x:Entity Matter $x And At $x Here And Control Self $x!"
        )
        canonical = result.ast.children[0].canonical()
        self.assertIn("Create(", canonical)
        self.assertIn("result=x:Entity", canonical)
        self.assertIn("Matter", canonical)
        self.assertIn("At", canonical)
        self.assertIn("Control", canonical)

    def test_create_can_use_named_kind_binder_plus_result_constraints(self):
        self.assert_valid(
            "Create x:«LowExtent«MoveLifeThing»» Life $x And At $x Here!"
        )

    def test_create_result_binder_must_be_entity_typed(self):
        result = self.parser.check(
            "Create i:Information About $i This!"
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "TypeMismatch")

    def test_create_profile_must_use_the_fresh_result(self):
        result = self.parser.check(
            "Create x:Entity AtSelfHere!"
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")

    def test_begin_exist_remains_reactivation_not_fresh_creation(self):
        created = self.assert_valid("Create x:Entity Matter $x And At $x Here!")
        restored = self.assert_valid("BeginExist This!")
        self.assertNotEqual(
            created.ast.children[0].canonical(),
            restored.ast.children[0].canonical(),
        )

    def test_create_can_establish_a_name_or_control_relation_in_profile(self):
        self.assert_valid(
            "Create x:Entity Matter $x And At $x Here And Control Self $x!"
        )

    def test_repeat_can_allocate_multiple_fresh_identities(self):
        self.assert_valid(
            "Repeat @@@ Create x:Entity Matter $x And At $x Here!"
        )

    def test_create_can_use_fresh_result_in_immediate_continuation(self):
        result = self.assert_valid(
            "Create x:Entity Matter $x And At $x Here Move $x There!"
        )
        canonical = result.ast.children[0].canonical()
        self.assertIn("continuation=", canonical)
        self.assertIn("Move", canonical)

    def test_create_binder_does_not_escape_into_sequence_sibling(self):
        result = self.parser.check(
            "Sequence Create x:Entity Matter $x And At $x Here SequenceEnd Move $x There!"
        )
        self.assertFalse(result.valid)


if __name__ == "__main__":
    unittest.main()
