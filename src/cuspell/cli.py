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
    print("INVALID")
    for diag in result.diagnostics:
        print(f"{diag.code}: {diag.message}")
        if diag.expected or diag.actual:
            print(f"  expected: {diag.expected or '-'}")
            print(f"  received: {diag.actual or '-'}")
    print(f"Mana (written semantic runes): {result.mana}")
    return 1


def _interactive(parser: Parser) -> int:
    print("Cuspell reference parser v0.1")
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
            print("Enter Cuspell text, e.g. !Move|This|Here.")
            print("Commands: :quit")
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
