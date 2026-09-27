from __future__ import annotations

import unittest
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
TOOLS=ROOT/"tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0,str(TOOLS))

import fuzz_parser


class FuzzSmokeTests(unittest.TestCase):
    def test_500_deterministic_fuzz_cases_do_not_crash(self):
        counts=fuzz_parser.run(cases=500,seed=20260927)
        self.assertEqual(sum(counts.values()),500)
        self.assertGreater(counts["VALID"],0)

    def test_repeated_seed_is_reproducible(self):
        self.assertEqual(
            fuzz_parser.run(cases=100,seed=7),
            fuzz_parser.run(cases=100,seed=7),
        )


if __name__=="__main__":
    unittest.main()
