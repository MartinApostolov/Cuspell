from __future__ import annotations

import argparse
import json
import sys

from .explain import tree
from .language import Language
from .parser import Parser


def _format_check(parser: Parser, source: str, explain: bool = False, as_json: bool = False) -> int:
    result = parser.check(source)
    if as_json:
        print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
        return 0 if result.valid else 1
    if result.valid:
        print("VALID")
        if result.ast:
            semantic = result.ast.children[0] if result.ast.children else result.ast
            print(f"Meaning: {semantic.canonical()}")
            print(f"Result type: {semantic.type}")
            print(f"Mana: {result.mana}")
            if explain:
                print("\nAST:")
                print(tree(semantic))
        return 0
    codes = {diag.code for diag in result.diagnostics}
    if "SemanticallyIncomplete" in codes:
        print("INCOMPLETE")
    elif "ContradictoryConstraint" in codes:
        print("CONTRADICTORY")
    else:
        print("INVALID")
    for diag in result.diagnostics:
        print(f"{diag.code}: {diag.message}")
        if diag.expected or diag.actual:
            print(f"  expected: {diag.expected or '-'}")
            print(f"  received: {diag.actual or '-'}")
    print(f"Mana (written semantic runes): {result.mana}")
    return 1


def _interactive(parser: Parser) -> int:
    print("Cuspell reference parser v0.3")
    print("Type a complete sentence ending in '.', or :help / :quit.")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not line:
            continue
        if line in {":quit", ":q", "quit", "exit"}:
            return 0
        if line == ":help":
            print("Enter Cuspell text directly, e.g. !Move This Here.")
            print("Interactive commands: :roots, :entry ROOT, :mana TEXT, :quit")
            continue
        if line == ":roots":
            print(" ".join(sorted(parser.language.entries)))
            continue
        if line.startswith(":entry "):
            surface=line.split(maxsplit=1)[1].strip()
            entries=parser.language.resolve_entries(surface)
            if not entries:
                print(f"No registered or derivable entry: {surface}")
            else:
                for entry in entries:
                    print(json.dumps(entry.data,indent=2,ensure_ascii=False))
            continue
        if line.startswith(":mana "):
            print(parser.mana_cost(line.split(maxsplit=1)[1]))
            continue
        if line.startswith(("python ", "py ", "cuspell ")):
            print("You are already inside Cuspell interactive mode; type the Cuspell sentence directly.")
            print("Example: !Move This Here.")
            continue
        _format_check(parser, line, explain=True)


def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="cuspell", description="Cuspell reference parser/type-checker")
    ap.add_argument("--root", help="Path to Cuspell repository root")
    sub = ap.add_subparsers(dest="command")
    for name in ("check", "parse", "explain", "mana"):
        sp = sub.add_parser(name)
        sp.add_argument("text")
        if name in {"check", "parse", "explain"}:
            sp.add_argument("--json", action="store_true")
    sub.add_parser("roots", help="List currently encoded exact roots")
    entry = sub.add_parser("entry", help="Show machine-readable data for a root or derived compound")
    entry.add_argument("surface")
    equiv = sub.add_parser("equiv", help="Compare two complete Cuspell sentences by normalized meaning")
    equiv.add_argument("left")
    equiv.add_argument("right")
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    language = Language.load(args.root)
    parser = Parser(language)
    if args.command is None:
        return _interactive(parser)
    if args.command == "mana":
        print(parser.mana_cost(args.text))
        return 0
    if args.command == "roots":
        for surface in sorted(language.entries):
            entry=language.entries[surface]
            print(f"{surface}\t{entry.category or '-'}")
        return 0
    if args.command == "entry":
        entries=language.resolve_entries(args.surface)
        if not entries:
            print(f"No registered or derivable entry: {args.surface}",file=sys.stderr)
            return 1
        for i,entry in enumerate(entries):
            if i:
                print()
            print(json.dumps(entry.data,indent=2,ensure_ascii=False))
        return 0
    if args.command == "equiv":
        left = parser.check(args.left)
        right = parser.check(args.right)
        if not left.valid or not right.valid:
            print("NOT COMPARABLE")
            for label, result in (("left", left), ("right", right)):
                if not result.valid:
                    print(f"{label}:")
                    for diag in result.diagnostics:
                        print(f"  {diag.code}: {diag.message}")
            return 2
        left_meaning = left.ast.children[0].canonical()
        right_meaning = right.ast.children[0].canonical()
        same = left.mood == right.mood and left_meaning == right_meaning
        print("EQUIVALENT" if same else "DIFFERENT")
        print(f"left:  {left_meaning}  [mana {left.mana}]")
        print(f"right: {right_meaning}  [mana {right.mana}]")
        return 0 if same else 1
    if args.command == "check":
        return _format_check(parser, args.text, explain=False, as_json=args.json)
    if args.command == "explain":
        return _format_check(parser, args.text, explain=True, as_json=args.json)
    if args.command == "parse":
        result = parser.check(args.text)
        if args.json:
            print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
        elif result.valid and result.ast:
            print(result.ast.children[0].canonical())
        else:
            for diag in result.diagnostics:
                print(f"{diag.code}: {diag.message}", file=sys.stderr)
        return 0 if result.valid else 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
