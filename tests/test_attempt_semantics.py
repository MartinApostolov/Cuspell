from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class AttemptSemanticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def check(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_attempt_is_an_actual_goal_directed_event(self):
        result = self.check("Before Attempt Self MoveSelfHere Now.")
        self.assertEqual(
            result.ast.children[0].canonical(),
            "Before(earlier=Attempt(agent=Self,goal=Move(theme=Self,goal=Here)),later=Now)",
        )

    def test_attempt_is_distinct_from_intention(self):
        attempted = self.check("Before Attempt Self MoveSelfHere Now.")
        intended = self.check("Before Intend Self MoveSelfHere Now.")
        self.assertNotEqual(
            attempted.ast.children[0].canonical(),
            intended.ast.children[0].canonical(),
        )

    def test_attempt_does_not_entail_goal_success(self):
        result = self.check(
            "And {Before Attempt Self MoveSelfHere Now,Not Before MoveSelfHere Now}."
        )
        meaning = result.ast.children[0].canonical()
        self.assertIn("Attempt(", meaning)
        self.assertIn("Not(", meaning)

    def test_attempt_and_goal_can_both_occur(self):
        result = self.check(
            "And {Before Attempt Self MoveSelfHere Now,Before MoveSelfHere Now}."
        )
        meaning = result.ast.children[0].canonical()
        self.assertIn("Attempt(", meaning)
        self.assertIn("Move(", meaning)

    def test_attempt_is_commandable_without_commanding_success(self):
        result = self.check("Attempt Self MoveSelfHere!")
        self.assertEqual(result.mood, "command")
        self.assertEqual(
            result.ast.children[0].canonical(),
            "Attempt(agent=Self,goal=Move(theme=Self,goal=Here))",
        )

    def test_incomplete_goal_still_fails_command_closure(self):
        result = self.parser.check("Attempt Self MoveSelf!")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")


if __name__ == "__main__":
    unittest.main()
