from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryLayoutTests(unittest.TestCase):
    def test_current_surface_directory_contains_only_v08_snapshot(self):
        syntax = ROOT / "language" / "syntax"
        snapshots = sorted(path.name for path in syntax.glob("surface_v*.json"))
        self.assertEqual(snapshots, ["surface_v0_8.json"])
        for version in range(2, 8):
            self.assertTrue(
                (ROOT / "archive" / "syntax" / f"surface_v0_{version}.json").is_file()
            )

    def test_current_docs_root_contains_no_completed_audit_snapshots(self):
        docs = ROOT / "docs"
        audits = sorted(path.name for path in docs.glob("*_AUDIT.md"))
        self.assertEqual(audits, [])
        self.assertFalse((docs / "history").exists())
        self.assertTrue((ROOT / "archive" / "audits").is_dir())

    def test_historical_decision_log_is_archived(self):
        self.assertTrue((ROOT / "docs" / "DECISIONS.md").is_file())
        self.assertTrue(
            (ROOT / "archive" / "decisions" / "DECISIONS_D001_D179.md").is_file()
        )

    def test_player_reference_layer_exists(self):
        for relative in (
            "player/README.md",
            "player/QUICK_START.md",
            "player/RULES.md",
            "player/RUNES.md",
            "player/ADVANCED_GRAMMAR.md",
            "player/names/OLD_NAMES.md",
            "player/names/NEW_NAMES.md",
        ):
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_player_rune_index_matches_current_lexicon(self):
        lexicon = json.loads(
            (ROOT / "language" / "core" / "lexicon.json").read_text(encoding="utf-8")
        )
        expected = {entry["surface"] for entry in lexicon["entries"]}

        surfaces: set[str] = set()
        for line in (ROOT / "player" / "RUNES.md").read_text(encoding="utf-8").splitlines():
            match = re.match(r"^\|\s*\x60([^\x60]+)\x60\s*\|", line)
            if match:
                surfaces.add(match.group(1))

        self.assertEqual(surfaces, expected)
        self.assertEqual(len(surfaces), 205)

    def test_player_old_name_index_matches_registry(self):
        old_names = json.loads(
            (ROOT / "language" / "names" / "old_names.json").read_text(encoding="utf-8")
        )
        expected = {entry["sign"] for entry in old_names["entries"]}

        signs: set[str] = set()
        for line in (
            ROOT / "player" / "names" / "OLD_NAMES.md"
        ).read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            match = re.search(r"\x60«(.+?)»\x60", line)
            if match:
                signs.add(match.group(1))

        self.assertEqual(signs, expected)
        self.assertEqual(len(signs), 102)

    def test_written_stress_snapshot_is_archive_only(self):
        self.assertFalse((ROOT / "docs" / "spec" / "STRESS_TESTS.md").exists())
        self.assertTrue((ROOT / "archive" / "tests" / "WRITTEN_STRESS_TESTS.md").is_file())
        self.assertFalse((ROOT / "tests" / "surface_syntax_cases.json").exists())
        self.assertTrue(
            (ROOT / "archive" / "tests" / "surface_syntax_cases_v0_3.json").is_file()
        )


    def test_current_reference_has_no_free_semantic_role_markers(self):
        forbidden = re.compile(
            r":(?:authority|context|path|source|instrument|basis|profile|offense|"
            r"community|goal|recipient|amount|frame|threat|observer|period|"
            r"interval|region|alternative|predicate|power)\\b"
        )
        roots = [ROOT / "docs", ROOT / "player", ROOT / "language" / "syntax"]
        failures: list[str] = []
        for root in roots:
            for path in root.rglob("*"):
                if not path.is_file() or path.suffix not in {".md", ".json"}:
                    continue
                if "archive" in path.parts:
                    continue
                for line_number, line in enumerate(
                    path.read_text(encoding="utf-8").splitlines(),
                    start=1,
                ):
                    if forbidden.search(line):
                        failures.append(
                            f"{path.relative_to(ROOT)}:{line_number}: {line.strip()}"
                        )
        self.assertEqual(failures, [], "\n".join(failures))

    def test_current_markdown_relative_links_resolve(self):
        roots = [
            ROOT / "README.md",
            ROOT / "AGENTS.md",
            ROOT / "docs",
            ROOT / "player",
            ROOT / "language" / "syntax" / "README.md",
            ROOT / "world" / "README.md",
        ]
        markdown_files: list[Path] = []
        for item in roots:
            if item.is_file():
                markdown_files.append(item)
            elif item.is_dir():
                markdown_files.extend(item.rglob("*.md"))

        link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
        failures: list[str] = []
        for source in markdown_files:
            if "archive" in source.parts:
                continue
            content = source.read_text(encoding="utf-8")
            for raw in link_re.findall(content):
                target = raw.strip().split("#", 1)[0]
                if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                    continue
                target = target.split("?", 1)[0].replace("%20", " ")
                resolved = (source.parent / target).resolve()
                if not resolved.exists():
                    failures.append(f"{source.relative_to(ROOT)} -> {raw}")

        self.assertEqual(failures, [], "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
