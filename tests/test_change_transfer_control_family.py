from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class ChangeTransferControlFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_give_root_is_removed(self):
        self.assertIsNone(self.language.entry("Give"))

    def test_give_meaning_is_coordinated_possession_boundaries(self):
        result = self.assert_valid(
            "Concurrent EndHave Self This BeginHave You This!"
        )
        canonical = result.ast.children[0].canonical()
        self.assertIn("End(state=Have(holder=Self,theme=This))", canonical)
        self.assertIn("Begin(state=Have(holder=You,theme=This))", canonical)

    def test_change_cause_transfer_and_control_survive(self):
        for source in (
            "Change This Heat «HeatUnit» @!",
            "Cause Self BeginLife This!",
            "Transfer This Self You!",
            "Control Self This.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)

    def test_rebuilt_transfer_old_names_resolve(self):
        for source in (
            "«TransferLifeMatter» This.",
            "«TransferBeginHaveThing» This.",
            "«TransferBeginHaveGroup» This.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)


if __name__ == "__main__":
    unittest.main()
