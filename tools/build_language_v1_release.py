#!/usr/bin/env python3
"""Build reproducible, self-contained Cuspell Language v1.0 release ZIPs.

No rune meanings, approved outlines, Unicode codepoints, or type rules change.
The accepted WinTest TTF/WOFF2 are copied byte-for-byte. Only explanatory
strings/default examples in the release copy of the offline keyboard change.
Run after the repository tests:
    python -m pip install fonttools brotli
    python tools/build_language_v1_release.py --output dist
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/release/LANGUAGE_V1_0_MANIFEST.json"
WIN = ROOT / "assets/glyphs/references/idylwild/windows_test_font"
COMPACT = ROOT / "assets/glyphs/references/idylwild/compact_font"
FULL_NAME = "Cuspell-Language-v1.0.zip"
KIT_NAME = "Cuspell-Language-v1.0-Windows-Font-Kit.zip"
TTF_NAME = "CuspellCompactWinTest-Regular.ttf"
WOFF_NAME = "CuspellCompactWinTest-Regular.woff2"
ARCHIVE_ROOT = "Cuspell-Language-v1.0"
DATE_TIME = (2026, 11, 22, 0, 0, 0)
TOP_LEVEL = ("assets/", "docs/", "language/", "player/", "src/", "tests/", "tools/", "world/")
ROOT_FILES = ("README.md", "pyproject.toml", "run_cuspell.py")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def check_release_invariants(manifest: dict) -> None:
    assert manifest["language_release"] == "1.0.0"
    assert manifest["git_tag"] == "v1.0.0"
    assert manifest["status"] == "FROZEN_RELEASE_SOURCE"
    counts = manifest["counts"]
    glyphs = read_json(ROOT / "language/core/glyph_assignments.json")
    lexical = read_json(ROOT / "language/core/lexicon.json")["entries"]
    old_names = read_json(ROOT / "language/names/old_names.json")["entries"]
    roles = read_json(ROOT / "language/core/inventory_roles.json")
    syntax = read_json(ROOT / "language/syntax/surface_v0_10.json")
    assert syntax["version"] == "0.10"
    assert len(lexical) == counts["registered_base_runes"] == 217
    assert len(glyphs["assignments"]) == counts["glyph_meanings_assigned"] == 218
    assert len(glyphs["spares"]) == counts["unassigned_spares"] == 16
    assert len(glyphs["assignments"] + glyphs["spares"]) == counts["approved_glyph_designs"] == 234
    assert glyphs["counts"]["approved_separate_punctuation"] == counts["separate_punctuation"] == 13
    assert len(old_names) == counts["old_names"] == 204
    assert sum(len(e.get("frames", [])) for e in lexical) == counts["semantic_frames"] == 276
    assert sum(len(e.get("frames", [])) > 1 for e in lexical) == counts["lexical_entries_with_multiple_frames"] == 53
    assert sum(roles["counts"].values()) == 217
    assert {e["surface"] for e in lexical} | {"@"} == {g["surface"] for g in glyphs["assignments"]}
    assert len({g["temporary_character"] for g in glyphs["assignments"]}) == 218
    assert all(len(g["temporary_character"]) == 1 for g in glyphs["assignments"])
    assert len({g["glyph_id"] for g in glyphs["assignments"] + glyphs["spares"]}) == 234
    assert (ROOT / "archive/syntax/surface_v0_9.json").is_file()
    assert (ROOT / "docs/release/LANGUAGE_V1_PC_UTF8_ACCEPTANCE.md").is_file()

    ttf = WIN / TTF_NAME
    assert ttf.is_file() and (WIN / WOFF_NAME).is_file()
    assert (WIN / "DEJAVU-LICENSE.txt").is_file()
    assert sha256(ttf.read_bytes()) == manifest["typography"]["approved_ttf_sha256"]
    assert read_json(WIN / "font_manifest.json")["ttf_sha256"] == manifest["typography"]["approved_ttf_sha256"]

    # Compare the *actual binary fonts* to guarantee approved PUA contours,
    # mapping and proportional spacing are not modified in the release build.
    from fontTools.ttLib import TTFont
    from fontTools.pens.recordingPen import DecomposingRecordingPen

    original = TTFont(COMPACT / "CuspellCompact-Regular.ttf")
    accepted = TTFont(ttf)
    original_set, accepted_set = original.getGlyphSet(), accepted.getGlyphSet()
    old_map, win_map = original.getBestCmap(), accepted.getBestCmap()
    assert old_map.keys() <= win_map.keys(), "Windows font lacks original cmap"
    assert all(win_map[cp] == name for cp, name in old_map.items())
    assert all(cp in win_map for cp in range(33, 127)), "Latin fallback missing"
    assert accepted["name"].getDebugName(1) == "Cuspell Compact WinTest"
    assert accepted["OS/2"].ulCodePageRange1 & 1
    assert accepted["OS/2"].fsSelection & 0x40
    assert any(t.platformID == 3 and t.platEncID == 1 for t in accepted["cmap"].tables)
    for cp, glyph_name in old_map.items():
        old_g, new_g = original["glyf"][glyph_name], accepted["glyf"][glyph_name]
        assert original["hmtx"].metrics[glyph_name] == accepted["hmtx"].metrics[glyph_name]
        assert old_g.numberOfContours == new_g.numberOfContours
        # Approved glyphs can be TrueType composites with no direct .coordinates.
        # Decompose against each font's *own* component glyph set, then compare
        # outline commands; this catches contour changes without rejecting
        # legitimate, unchanged composites.
        old_pen = DecomposingRecordingPen(original_set)
        new_pen = DecomposingRecordingPen(accepted_set)
        original_set[glyph_name].draw(old_pen)
        accepted_set[glyph_name].draw(new_pen)
        assert old_pen.value == new_pen.value, f"Changed outline: U+{cp:04X}"
    for item in glyphs["assignments"]:
        cp = ord(item["temporary_character"])
        assert cp in win_map, item["surface"]
    original.close()
    accepted.close()


def release_keyboard() -> bytes:
    source = (WIN / "meaning_keyboard.html").read_text(encoding="utf-8")
    assert "Cuspell 234 Review" in source, "Expected historical copy not found"
    assert "CuspellCompactWinTest-Regular.woff2" in source
    keyboard = source.replace("Cuspell 234 Review", "Cuspell Compact WinTest")
    old_examples = "Move This There!\nLifeThis?\nCreate Light «LightUnit» @!"
    current = (
        "All :«This» Life $«This».\n"
        "Create :«This» At $«This» There Change $«This» Light «LightUnit» @!"
    )
    assert keyboard.count(old_examples) == 1, "Unexpected old keyboard default"
    keyboard = keyboard.replace(old_examples, current)
    keyboard = keyboard.replace(
        "<title>Cuspell meaning-aware glyph keyboard</title>",
        "<title>Cuspell Language v1.0 — meaning-aware rune keyboard</title>",
    ).replace(
        "<h1>Cuspell · Meaning-aware rune keyboard</h1>",
        "<h1>Cuspell Language v1.0 · Rune keyboard</h1>",
    )
    assert "Cuspell 234 Review" not in keyboard
    assert current in keyboard
    assert "const CODEC_DATA" in keyboard
    return keyboard.encode("utf-8")


def windows_kit_files(manifest: dict) -> dict[str, bytes]:
    source = read_json(WIN / "font_manifest.json")
    release_font_manifest = {
        **source,
        "status": "WINDOWS_NOTEPAD_UTF8_ACCEPTED_FOR_LANGUAGE_V1_0",
        "source_build_status": source["status"],
        "release_tag": manifest["git_tag"],
        "user_acceptance": "docs/release/LANGUAGE_V1_PC_UTF8_ACCEPTANCE.md",
    }
    instructions = """# Cuspell Language v1.0 — Windows font and keyboard

The installed Windows font family is **Cuspell Compact WinTest**.
The WinTest name is retained because this is the exact binary approved
in the user's Windows Notepad and UTF-8 save/reopen/decode checks.
No new installation test is required and no glyph outlines were altered.

1. Install CuspellCompactWinTest-Regular.ttf.
2. Keep meaning_keyboard.html beside the TTF/WOFF2, then open the HTML
   directly in a browser (offline is supported).
3. Type Cuspell transliteration in the left pane and select
   Convert → glyphs. To decode, paste in the right pane and select
   Decode → names.
4. In Notepad choose font family Cuspell Compact WinTest to display the
   copied Private Use Area symbols. In other fonts they can look like boxes.

The keyboard converts spelling, not grammatical meaning; the parser
in the complete Language v1.0 ZIP validates syntax and semantic types.
VS Code compatibility and gameplay execution are not release requirements.

The added Latin fallback outlines are from DejaVu Sans Mono and
the accompanying DEJAVU-LICENSE.txt must be retained.
Original stylized Idylwild Runic/Alchemical artwork is CC0;
see assets/glyphs/references/idylwild/keyboard_kit/SOURCES.txt
in the complete language distribution.
"""
    return {
        TTF_NAME: (WIN / TTF_NAME).read_bytes(),
        WOFF_NAME: (WIN / WOFF_NAME).read_bytes(),
        "meaning_keyboard.html": release_keyboard(),
        "README.md": instructions.encode("utf-8"),
        "font_manifest.json": (json.dumps(release_font_manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
        "DEJAVU-LICENSE.txt": (WIN / "DEJAVU-LICENSE.txt").read_bytes(),
    }


def zip_add(zf: ZipFile, name: str, data: bytes) -> None:
    zi = ZipInfo(name, DATE_TIME)
    zi.compress_type = ZIP_DEFLATED
    zi.external_attr = 0o100644 << 16
    zf.writestr(zi, data, compresslevel=9)


def tracked_paths() -> list[Path]:
    # Source-of-truth is the checked-out release commit. Never package a
    # working-tree scratch file, old archive, secrets, CI state or dist output.
    raw = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    all_paths = [Path(p.decode("utf-8")) for p in raw.split(b"\0") if p]
    selected = [
        p for p in all_paths
        if str(p) in ROOT_FILES or str(p).startswith(TOP_LEVEL)
    ]
    assert selected and any(str(p).startswith("assets/glyphs/") for p in selected)
    return sorted(selected, key=lambda p: p.as_posix())


def build(outdir: Path) -> None:
    manifest = read_json(MANIFEST)
    check_release_invariants(manifest)
    outdir.mkdir(parents=True, exist_ok=True)
    windows_files = windows_kit_files(manifest)
    win_zip = outdir / KIT_NAME
    with ZipFile(win_zip, "w") as zf:
        for name, data in sorted(windows_files.items()):
            zip_add(zf, name, data)
    with ZipFile(win_zip) as zf:
        assert zf.testzip() is None
        assert set(zf.namelist()) == set(windows_files)

    root_sha = os.environ.get("GITHUB_SHA") or subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True,
    ).strip()
    release_manifest = {
        **manifest,
        "git_commit": root_sha,
        "release_windows_kit_sha256": sha256(win_zip.read_bytes()),
        "windows_keyboard_sha256": sha256(windows_files["meaning_keyboard.html"]),
    }
    readme = (
        "# Cuspell Language v1.0\n\n"
        "Start at player/README.md for the language and docs/CUSPELL_DICTIONARY.md "
        "for the illustrated dictionary.\n\n"
        "Install the accepted Windows font from release/Windows_Font/"
        + TTF_NAME + " and open release/Windows_Font/meaning_keyboard.html "
        "from that same folder. The Windows font family is Cuspell Compact WinTest.\n\n"
        "The canonical meaning mapping is language/core/glyph_assignments.json; "
        "the canonical written syntax is language/syntax/surface_v0_10.json. "
        "The included Python parser can be invoked with run_cuspell.py.\n\n"
        "Release notes are in docs/release/LANGUAGE_V1_0_RELEASE_NOTES.md. "
        "Previous grammar snapshots and historical review fonts are preserved "
        "on the tagged GitHub repository, but are not needed for current writing.\n"
    )
    full = outdir / FULL_NAME
    with ZipFile(full, "w") as zf:
        for p in tracked_paths():
            zip_add(zf, f"{ARCHIVE_ROOT}/{p.as_posix()}", (ROOT / p).read_bytes())
        for name, data in sorted(windows_files.items()):
            zip_add(zf, f"{ARCHIVE_ROOT}/release/Windows_Font/{name}", data)
        zip_add(zf, f"{ARCHIVE_ROOT}/release/README.md", readme.encode("utf-8"))
        zip_add(zf, f"{ARCHIVE_ROOT}/release/version-manifest.json",
                (json.dumps(release_manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    with ZipFile(full) as zf:
        assert zf.testzip() is None
        paths = set(zf.namelist())
        for required in (
            "language/syntax/surface_v0_10.json",
            "language/core/lexicon.json",
            "language/core/glyph_assignments.json",
            "language/names/old_names.json",
            "docs/CUSPELL_DICTIONARY.md",
            "player/README.md",
            "src/cuspell/parser.py",
            "release/version-manifest.json",
            "release/Windows_Font/meaning_keyboard.html",
            "release/Windows_Font/DEJAVU-LICENSE.txt",
            f"release/Windows_Font/{TTF_NAME}",
        ):
            assert f"{ARCHIVE_ROOT}/{required}" in paths, required

    # Copy the accepted TTF byte-for-byte beside the verified ZIPs.
    # Both SHA256SUMS and the release uploader use these exact files.
    out_font = outdir / TTF_NAME
    out_font.write_bytes((WIN / TTF_NAME).read_bytes())
    checks = {
        FULL_NAME: sha256(full.read_bytes()),
        KIT_NAME: sha256(win_zip.read_bytes()),
        TTF_NAME: sha256(out_font.read_bytes()),
    }
    checksum_file = outdir / "SHA256SUMS.txt"
    checksum_file.write_text(
        "".join(f"{digest}  {name}\n" for name, digest in sorted(checks.items())),
        encoding="ascii",
    )
    print("Cuspell Language v1.0: release invariants and font contours verified")
    for name, digest in checks.items():
        print(f"  {name}: {digest}")
    print(f"  Release commit: {root_sha}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    build(args.output)
