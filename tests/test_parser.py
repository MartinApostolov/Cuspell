from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class ParserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def assert_valid(self, source: str, meaning: str, mana: int | None = None):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIsNotNone(result.ast)
        node = result.ast.children[0]
        self.assertEqual(node.canonical(), meaning)
        if mana is not None:
            self.assertEqual(result.mana, mana)

    def test_kind_predication(self):
        self.assert_valid("«LowExtent«MoveLifeThing»» Self.", "InstanceOf(Self,Concept(core.biology.cat))", 6)

    def test_move_command(self):
        self.assert_valid("!Move This Here.", "Move(theme=This,goal=Here)", 3)

    def test_debug_pipe_spacing(self):
        self.assert_valid("!Move | This | Here.", "Move(theme=This,goal=Here)", 3)

    def test_debug_pipe_matches_space_form(self):
        spaced = self.parser.check("!Move This Here.")
        piped = self.parser.check("!Move|This|Here.")
        self.assertTrue(spaced.valid, spaced.diagnostics)
        self.assertTrue(piped.valid, piped.diagnostics)
        self.assertEqual(spaced.ast.children[0].canonical(), piped.ast.children[0].canonical())

    def test_debug_pipe_group_closes_before_following_space(self):
        result = self.parser.check("!Move|This Here.")
        self.assertFalse(result.valid)
        self.assertIn(result.diagnostics[0].code, {"SyntaxError", "BoundGroupError", "TypeMismatch"})


    def test_debug_pipe_does_not_turn_trailing_space_into_sequence(self):
        result = self.parser.check("!Move|This|Here There.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SyntaxError")
        self.assertIn("consumed", result.diagnostics[0].message)

    def test_type_error(self):
        result = self.parser.check("!Move This @@.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "TypeMismatch")
        self.assertEqual(result.diagnostics[0].expected, "Location")
        self.assertEqual(result.diagnostics[0].actual, "Quantity:Number")

    def test_flat_if(self):
        self.assert_valid(
            "!If Life This EndLife This.",
            "If(condition=Life(subject=This),consequent=End(state=Life(subject=This)))",
            6,
        )

    def test_binder(self):
        self.assert_valid(
            "All [a:«Know«MoveLifeThing»»] Life $a.",
            "All(binder=a:«Know«MoveLifeThing»»,predicate=Life(subject=$a))",
            6,
        )

    def test_sequence_collection(self):
        self.assert_valid(
            "!Sequence {Move This Here,EndLife Self}.",
            "Sequence(events=[Move(theme=This,goal=Here),End(state=Life(subject=Self))])",
            7,
        )

    def test_named_role(self):
        self.assert_valid(
            "!Move This Here There.",
            "Move(theme=This,goal=Here,source=There)",
            4,
        )

    def test_deep_flat_relative_change(self):
        self.assert_valid(
            "!Preserve Volume This Change This Density Multiply @@ BeforeValue Density This.",
            "Preserve(value=Volume(subject=This),event=Change(theme=This,attribute=Density,target=Multiply(factor=2,value=BeforeValue(value=Density(subject=This),event=EnclosingEvent))))",
            12,
        )

    def test_preserve_volume_type_error(self):
        result = self.parser.check("!Change This Density Here.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "TypeMismatch")

    def test_missing_period(self):
        result = self.parser.check("Matter|Self")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SyntaxError")


if __name__ == "__main__":
    unittest.main()
