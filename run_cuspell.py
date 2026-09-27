#!/usr/bin/env python3
"""Zero-install entry point for the Cuspell reference parser."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from cuspell.cli import main

raise SystemExit(main())
