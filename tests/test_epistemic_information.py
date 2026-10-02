from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT=Path(__file__).resolve().parents[1]


class EpistemicInformationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser=Parser(Language.load(ROOT))

    def valid(self,source,meaning=None):
        result=self.parser.check(source)
        self.assertTrue(result.valid,result.diagnostics)
        if meaning is not None:
            self.assertEqual(result.ast.children[0].canonical(),meaning)
        return result

    def test_belief_is_state_not_truth(self):
        self.valid("Believe Self Life This.","Believe(mind=Self,proposition=Life(subject=This))")

    def test_knowledge_frame(self):
        self.valid("Know Self Life This.","Know(mind=Self,proposition=Life(subject=This))")

    def test_evidence_for(self):
        self.valid("EvidenceFor ThisInformation Life This.")

    def test_confidence_comparison(self):
        self.valid("More Confidence Self Life This Confidence Self Exist This.")

    def test_epistemic_thresholds(self):
        self.valid("High Confidence Self Life This.")
        self.valid("More Confidence Self Life This Zero.")
        self.valid("Equal Confidence Self Life This «ConfidenceUnit» @.")

    def test_assertion_event_does_not_become_outer_truth(self):
        meaning=self.valid("Happen Assert You Life Self ThisInterval.").ast.children[0].canonical()
        self.assertIn("Assert",meaning)
        self.assertIn("Life",meaning)

    def test_assert_is_the_canonical_claiming_event(self):
        meaning=self.valid("Happen Assert You Life Self ThisInterval.").ast.children[0].canonical()
        self.assertIn("Assert",meaning)

    def test_promise_contains_future_event_spec(self):
        self.valid(
            "!And {Say Self (Obligated Self (Move Self Here) You) You,Begin (Obligated Self (Move Self Here) You)}."
        )

    def test_open_why_question(self):
        self.valid("?[x:Explanation] Explains $x Life This.")

    def test_open_how_question(self):
        self.valid("?[m:Method] Purpose $m Move This Here.")


if __name__=="__main__":
    unittest.main()
