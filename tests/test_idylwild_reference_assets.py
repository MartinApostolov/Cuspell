"""Regression tests for Idylwild source archives used in visual Cuspell comparisons.

Standard-library only so Cuspell's Python 3.11/3.12 parser CI keeps working.
The initial workflow push may run before GitHub Actions has imported ZIPs;
in that case ZIP-specific tests skip. The importer CI re-runs them after
downloading and before committing source archives and review images.
"""
import hashlib
import re
import struct
import unittest
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"assets/glyphs/references/idylwild/original"
SOURCES=[
    ("idylwilds_runic_codex.zip","1f5473b40e96fdaa980bc93993890a2f9e49d13ba0fdb6d5895bbacf5cb4cda5",224),
    ("idylwilds_alchemical_codex.zip","50ffd77d022dd0a62603f105dfc1b94ccff767e126622a3105ce03dc612dc055",75),
]

def count_numbered(names,kind):
    pat=(r"runes/rune(\d+)\.png" if kind=="runic" else r"tile(\d{3})\.png")
    return {int(m.group(1)):n for n in names if (m:=re.fullmatch(pat,n))}

class CodexReferenceArchiveTests(unittest.TestCase):
    def test_comparison_script_is_saved(self):
        self.assertTrue((BASE.parent/"compare_codices.py").is_file())

    def test_archive_original_bytes_and_layout(self):
        for name,sha,n in SOURCES:
            with self.subTest(name=name):
                p=BASE/name
                if not p.is_file():
                    self.skipTest("Idylwild ZIPs are still being imported by source-asset CI")
                self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),sha)
                with zipfile.ZipFile(p) as z:
                    self.assertIsNone(z.testzip(),"ZIP CRC integrity failure")
                    runic="runic" in name
                    selected=count_numbered(z.namelist(),"runic" if runic else "alchemical")
                    self.assertEqual(set(selected),set(range(1,n+1)) if runic else set(range(n*3)))
                    self.assertEqual(sum(s.endswith(".png") and s.startswith("runes/")
                                         for s in z.namelist()) if runic else len(selected),
                                     672 if runic else 225)
                    first=selected[1 if runic else 0]
                    header=z.read(first)[:24]
                    self.assertEqual(header[:8],b"\x89PNG\r\n\x1a\n")
                    self.assertEqual(struct.unpack(">II",header[16:24]),(16,16))

if __name__=="__main__":
    unittest.main()
