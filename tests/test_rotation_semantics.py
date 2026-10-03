from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class RotationSemanticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_rotate_is_registered_as_process(self):
        entry = self.language.entry("Rotate")
        self.assertIsNotNone(entry)
        self.assertEqual(entry.category, "Process")
        self.assertEqual(len(entry.frames), 1)

    def test_rotate_requires_explicit_pivot_axis_and_turns(self):
        result = self.parser.check("Rotate This Here Toward Self @!")
        self.assertTrue(result.valid, result.diagnostics)

        missing = self.parser.parse_phrase(
            "Rotate This Here Toward Self",
            expected_type="EventSpec",
        )
        self.assertIsInstance(missing, Diagnostic)

    def test_rotate_is_not_translational_move(self):
        rotate = self.parser.check(
            "Rotate This Here Toward Self @!"
        ).ast.children[0].canonical()
        move = self.parser.check("Move This Here!").ast.children[0].canonical()
        self.assertNotEqual(rotate, move)

    def test_rotate_is_not_change_form(self):
        rotate = self.parser.check(
            "Rotate This Here Toward Self @!"
        ).ast.children[0].canonical()
        self.assertIn("Rotate(", rotate)
        self.assertNotIn("Change(", rotate)


if __name__ == "__main__":
    unittest.main()
