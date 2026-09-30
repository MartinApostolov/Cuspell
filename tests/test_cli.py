from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
import os

from cuspell.cli import main

ROOT=Path(__file__).resolve().parents[1]


class CliTests(unittest.TestCase):
    def call(self,args):
        old=os.environ.get("CUSPELL_ROOT")
        os.environ["CUSPELL_ROOT"]=str(ROOT)
        out=io.StringIO(); err=io.StringIO()
        try:
            with redirect_stdout(out), redirect_stderr(err):
                code=main(args)
        finally:
            if old is None:
                os.environ.pop("CUSPELL_ROOT",None)
            else:
                os.environ["CUSPELL_ROOT"]=old
        return code,out.getvalue(),err.getvalue()

    def test_roots_lists_move(self):
        code,out,_=self.call(["roots"])
        self.assertEqual(code,0)
        self.assertIn("Move\tProcess",out)

    def test_entry_can_show_derived_compound(self):
        code,out,_=self.call(["entry","SolidMatter"])
        self.assertEqual(code,0)
        self.assertIn('"derived_kind"',out)

    def test_equiv_reports_normalized_equivalence(self):
        code,out,_=self.call(["equiv","NotNotLife This.","Life This."])
        self.assertEqual(code,0)
        self.assertIn("EQUIVALENT",out)

    def test_entry_unknown_fails_cleanly(self):
        code,_,err=self.call(["entry","DefinitelyNotARoot"])
        self.assertEqual(code,1)
        self.assertIn("No registered or derivable entry",err)

    def test_check_shows_source_span_for_invalid_input(self):
        code,out,_=self.call(["check","!Move This @@."])
        self.assertEqual(code,1)
        self.assertIn("source span: 11:13",out)
        self.assertIn("!Move This @@.",out)
        self.assertIn("^^",out)


if __name__=="__main__":
    unittest.main()
