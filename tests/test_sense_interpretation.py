from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser


ROOT = Path(__file__).resolve().parents[1]


class SenseInterpretationRedesignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_sense_has_only_the_explicit_channel_frame(self):
        sense = self.language.entry("Sense")
        self.assertIsNotNone(sense)
        self.assertEqual([frame["id"] for frame in sense.frames], ["sense.channel"])

        explicit = self.parser.check("Sense Self Vision «yes».")
        self.assertTrue(explicit.valid, explicit.diagnostics)

        hidden_interpretation = self.parser.check("Sense Self «yes».")
        self.assertFalse(hidden_interpretation.valid)

    def test_interpret_is_a_distinct_single_frame_process(self):
        interpret = self.language.entry("Interpret")
        self.assertIsNotNone(interpret)
        self.assertEqual([frame["id"] for frame in interpret.frames], ["interpret.sign"])

        result = self.parser.check("Interpret Self «yes».")
        self.assertTrue(result.valid, result.diagnostics)

    def test_former_read_meaning_combines_sense_and_interpret(self):
        self.assertIsNone(self.language.entry("Read"))
        result = self.parser.check(
            "Concurrent Sense Self Vision «yes» Interpret Self «yes»."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_interpretation_stays_distinct_from_meaning_and_understanding(self):
        interpret = self.parser.check("Interpret Self «yes».")
        meaning = self.parser.check("Meaning «yes» ThisInformation.")
        understand = self.parser.check("Understand Self ThisInformation.")

        self.assertTrue(interpret.valid, interpret.diagnostics)
        self.assertTrue(meaning.valid, meaning.diagnostics)
        self.assertTrue(understand.valid, understand.diagnostics)
        self.assertNotEqual(
            interpret.ast.children[0].canonical(),
            meaning.ast.children[0].canonical(),
        )
        self.assertNotEqual(
            interpret.ast.children[0].canonical(),
            understand.ast.children[0].canonical(),
        )


if __name__ == "__main__":
    unittest.main()
