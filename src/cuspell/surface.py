from __future__ import annotations

import re


def normalize_pipe_spacing(text: str) -> str:
    return re.sub(r"\s*\|\s*", "|", text)


def strip_sentence(text: str) -> tuple[str, str]:
    source = text.strip()
    if not source.endswith("."):
        raise ValueError("A complete Cuspell sentence must end with '.'.")
    body = source[:-1].strip()
    mood = "assertion"
    if body.startswith("!"):
        mood = "command"
        body = body[1:].lstrip()
    elif body.startswith("?"):
        mood = "question"
        body = body[1:].lstrip()
    if not body:
        raise ValueError("Sentence body is empty.")
    return mood, normalize_pipe_spacing(body)


def split_top_level(text: str, delimiter: str) -> list[str]:
    out: list[str] = []
    start = 0
    paren = brace = bracket = 0
    quote = False
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "«":
            quote = True
        elif ch == "»":
            quote = False
        elif not quote:
            if ch == "(": paren += 1
            elif ch == ")": paren -= 1
            elif ch == "{": brace += 1
            elif ch == "}": brace -= 1
            elif ch == "[": bracket += 1
            elif ch == "]": bracket -= 1
            elif ch == delimiter and paren == brace == bracket == 0:
                out.append(text[start:i].strip())
                start = i + 1
        i += 1
    out.append(text[start:].strip())
    return [x for x in out if x != ""]


def split_phrases(body: str) -> list[str]:
    out: list[str] = []
    start = 0
    paren = brace = bracket = 0
    quote = False
    i = 0
    while i < len(body):
        ch = body[i]
        if ch == "«":
            quote = True
        elif ch == "»":
            quote = False
        elif not quote:
            if ch == "(": paren += 1
            elif ch == ")": paren -= 1
            elif ch == "{": brace += 1
            elif ch == "}": brace -= 1
            elif ch == "[": bracket += 1
            elif ch == "]": bracket -= 1
            elif ch.isspace() and paren == brace == bracket == 0:
                piece = body[start:i].strip()
                if piece:
                    out.append(piece)
                while i + 1 < len(body) and body[i + 1].isspace():
                    i += 1
                start = i + 1
        i += 1
    piece = body[start:].strip()
    if piece:
        out.append(piece)
    return out


def split_fields(phrase: str) -> list[str]:
    return split_top_level(phrase, "|")
