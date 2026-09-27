from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data

ROOT=Path(__file__).resolve().parents[1]


class LanguageDataTests(unittest.TestCase):
    def test_machine_readable_language_is_internally_valid(self):
        self.assertEqual(validate_language_data(ROOT),[])


if __name__=="__main__":
    unittest.main()
