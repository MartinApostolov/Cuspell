from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT=Path(__file__).resolve().parents[1]


class MeasuredPropertyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser=Parser(Language.load(ROOT))

    def assert_valid(self,source,meaning):
        result=self.parser.check(source)
        self.assertTrue(result.valid,result.diagnostics)
        self.assertEqual(result.ast.children[0].canonical(),meaning)

    def test_zero_light(self):
        self.assert_valid("ZeroLight This.","Equal(left=Light(subject=This),right=0)")

    def test_zero_heat(self):
        self.assert_valid("ZeroHeat This.","Equal(left=Heat(subject=This),right=0)")

    def test_zero_density(self):
        self.assert_valid("ZeroDensity This.","Equal(left=Density(subject=This),right=0)")

    def test_measured_property_costs_both_written_roots(self):
        result=self.parser.check("ZeroLight This.")
        self.assertTrue(result.valid,result.diagnostics)
        self.assertEqual(result.mana,3)

    def test_quantity_attribute_compound_is_not_generic_relation_compounding(self):
        result=self.parser.check("ZeroBefore ThisEvent ThatEvent.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code,"IllegalCompound")


if __name__=="__main__":
    unittest.main()
