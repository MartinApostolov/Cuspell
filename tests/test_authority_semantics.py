from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class AuthoritySemanticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_authority_is_persistent_social_relation(self):
        entry = self.language.entry("Authority")
        self.assertIsNotNone(entry)
        node = self.parser.parse_phrase(
            "Authority Self This",
            expected_type="StateProposition",
        )
        self.assertEqual(node.type, "StateProposition")
        result = self.parser.check("Authority Self This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_authority_can_begin_and_end_as_a_state(self):
        begin = self.parser.check("Begin Authority Self This!")
        end = self.parser.check("End Authority Self This!")
        self.assertTrue(begin.valid, begin.diagnostics)
        self.assertTrue(end.valid, end.diagnostics)

    def test_authority_is_not_physical_control(self):
        authority = self.parser.check("Authority Self This.").ast.children[0].canonical()
        control = self.parser.check("Control Self This.").ast.children[0].canonical()
        self.assertNotEqual(authority, control)

    def test_authority_is_not_merely_permission(self):
        authority_result = self.parser.check("Authority Self This.")
        permitted_result = self.parser.check("Permitted Self Move Self Here This.")
        self.assertTrue(authority_result.valid, authority_result.diagnostics)
        self.assertTrue(permitted_result.valid, permitted_result.diagnostics)

        authority = authority_result.ast.children[0]
        permitted = permitted_result.ast.children[0]
        self.assertEqual(authority.type, "StateProposition")
        self.assertEqual(permitted.type, "Proposition")
        self.assertNotEqual(authority.canonical(), permitted.canonical())


if __name__ == "__main__":
    unittest.main()
