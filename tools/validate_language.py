#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"src"
if str(SRC) not in sys.path:
    sys.path.insert(0,str(SRC))

from cuspell.data_validation import validate_language_data


def main()->int:
    errors=validate_language_data(ROOT)
    if errors:
        print(f"LANGUAGE DATA INVALID ({len(errors)} issue(s))")
        for error in errors:
            print(f"- {error}")
        return 1
    print("LANGUAGE DATA VALID")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
