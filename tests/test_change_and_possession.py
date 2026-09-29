from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT=Path(__file__).resolve().parents[1]


class ChangeAndPossessionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser=Parser(Language.load(ROOT))

    def valid(self,source,meaning=None):
        result=self.parser.check(source)
        self.assertTrue(result.valid,result.diagnostics)
        if meaning is not None:
            self.assertEqual(result.ast.children[0].canonical(),meaning)
        return result

    def test_change_family_member_shorthand(self):
        self.valid(
            "!Change This Solid.",
            "Change(theme=This,attribute=Phase,target=Solid)",
        )

    def test_change_family_member_differs_from_property_assertion(self):
        prop=self.valid("Solid This.").ast.children[0].canonical()
        change=self.valid("!Change This Solid.").ast.children[0].canonical()
        self.assertNotEqual(prop,change)

    def test_change_by_density(self):
        self.valid(
            "!ChangeBy This Density Density Self.",
            "ChangeBy(theme=This,attribute=Density,delta=Density(subject=Self))",
        )

    def test_begin_have_compound(self):
        self.valid("!BeginHave Self This.","Begin(state=Have(holder=Self,theme=This))")

    def test_end_have_compound(self):
        self.valid("!EndHave Self This.","End(state=Have(holder=Self,theme=This))")

    def test_get_is_begin_have_molecule(self):
        self.valid("!Get Self This.","Begin(state=Have(holder=Self,theme=This))")

    def test_loss_is_written_with_end_have(self):
        self.valid("!EndHave Self This.","End(state=Have(holder=Self,theme=This))")


if __name__=="__main__":
    unittest.main()
