from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class SurfaceV03Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def meaning(self, source: str) -> str:
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result.ast.children[0].canonical()

    def test_normal_space_kind_predication(self):
        self.assertEqual(
            self.meaning("SolidMatter This."),
            "InstanceOf(This,RestrictKind(base=Matter,property=Solid))",
        )

    def test_normal_space_move(self):
        self.assertEqual(self.meaning("!Move This Here."), "Move(theme=This,goal=Here)")

    def test_normal_space_nested_if(self):
        self.assertEqual(
            self.meaning("!If Life This EndLife This."),
            "If(condition=Life(subject=This),consequent=End(state=Life(subject=This)))",
        )

    def test_normal_space_deep_expression(self):
        self.assertEqual(
            self.meaning("!Preserve Volume This Change This Density Multiply @@ BeforeValue Density This."),
            "Preserve(value=Volume(subject=This),event=Change(theme=This,attribute=Density,target=Multiply(factor=2,value=BeforeValue(value=Density(subject=This),event=EnclosingEvent))))",
        )

    def test_pipe_binding_is_equivalent_when_it_covers_whole_expression(self):
        self.assertEqual(
            self.meaning("!Move|This|Here."),
            self.meaning("!Move This Here."),
        )

    def test_pipe_binding_can_group_nested_argument(self):
        self.assertEqual(
            self.meaning("!If Life|This EndLife|This."),
            self.meaning("!If Life This EndLife This."),
        )

    def test_pipe_binding_closes_group(self):
        result = self.parser.check("!Move|This Here.")
        self.assertFalse(result.valid)

    def test_space_does_not_mean_sequence(self):
        result = self.parser.check("!Move|This|Here EndLife Self.")
        self.assertFalse(result.valid)

    def test_collection_items_use_normal_space_syntax(self):
        self.assertEqual(
            self.meaning("!Sequence {Move This Here,EndLife Self}."),
            "Sequence(events=[Move(theme=This,goal=Here),End(state=Life(subject=Self))])",
        )


if __name__ == "__main__":
    unittest.main()
