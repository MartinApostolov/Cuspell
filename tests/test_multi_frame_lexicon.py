from __future__ import annotations

import json
import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser


ROOT = Path(__file__).resolve().parents[1]


class MultiFrameLexiconAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_grateful_to_basis_is_one_optional_positional_role(self):
        data = json.loads(
            (ROOT / "language" / "core" / "lexicon.json").read_text(encoding="utf-8")
        )
        entry = next(item for item in data["entries"] if item["surface"] == "GratefulTo")

        self.assertEqual([frame["id"] for frame in entry["frames"]], ["grateful_to.state"])
        basis = next(slot for slot in entry["frames"][0]["slots"] if slot["name"] == "basis")
        self.assertFalse(basis["required"])
        self.assertNotIn("named_only", basis)

        for source in (
            "GratefulTo Self You.",
            "GratefulTo Self You ThisEvent.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)


if __name__ == "__main__":
    unittest.main()
