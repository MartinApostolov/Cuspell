from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class ExecutionClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def test_move_without_goal_or_path_is_incomplete(self):
        result = self.parser.check("!Move|This.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")
        self.assertIn("goal", result.diagnostics[0].message)
        self.assertIn("path", result.diagnostics[0].message)

    def test_move_with_goal_is_complete(self):
        result = self.parser.check("!Move|This|Here.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_move_with_explicit_path_is_complete(self):
        result = self.parser.check("!Move|This|:path|ThisPath.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(result.ast.children[0].canonical(), "Move(theme=This,path=ThisPath)")

    def test_incomplete_event_inside_if_is_caught(self):
        result = self.parser.check("!If|Life|This|Move|This.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")

    def test_incomplete_event_inside_sequence_is_caught(self):
        result = self.parser.check("!Sequence|{Move|This,EndLife|Self}.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")


if __name__ == "__main__":
    unittest.main()
