from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class SourcePhrase:
    text: str
    start: int
    end: int


def normalize_pipe_spacing(text: str) -> str:
    return re.sub(r"\s*\|\s*", "|", text)


def strip_sentence_source(text: str) -> tuple[str, str, int]:
    """Return mood, unnormalized sentence body, and its start offset in text.

    Canonical Cuspell v0.5 marks mood with the sentence-final terminator:
    '.' assertion, '?' question, '!' command.

    Legacy prefix mood with a final period remains parser-compatible for the
    existing corpus/tests, but is not canonical surface syntax.
    """
    left_trimmed = len(text) - len(text.lstrip())
    source = text.strip()
    if not source or source[-1] not in ".?!":
        raise ValueError("A complete Cuspell sentence must end with '.', '?', or '!'.")

    terminator = source[-1]
    mood = {
        ".": "assertion",
        "?": "question",
        "!": "command",
    }[terminator]

    raw_body = source[:-1]
    body_left = len(raw_body) - len(raw_body.lstrip())
    body = raw_body.strip()
    body_start = left_trimmed + body_left

    # Temporary backwards compatibility for the pre-v0.5 transliteration.
    # Only a final period may use the legacy leading mood marker.
    if terminator == "." and body.startswith("!"):
        mood = "command"
        body = body[1:]
        body_start += 1
        mood_space = len(body) - len(body.lstrip())
        body = body.lstrip()
        body_start += mood_space
    elif terminator == "." and body.startswith("?"):
        mood = "question"
        body = body[1:]
        body_start += 1
        mood_space = len(body) - len(body.lstrip())
        body = body.lstrip()
        body_start += mood_space
    elif body.startswith(("!", "?")):
        raise ValueError("In canonical Cuspell, '?' and '!' are sentence-final mood marks.")

    if not body:
        raise ValueError("Sentence body is empty.")
    return mood, body, body_start


def strip_sentence(text: str) -> tuple[str, str]:
    mood, body, _ = strip_sentence_source(text)
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


def split_phrases_with_spans(body: str) -> list[SourcePhrase]:
    """Split top-level whitespace while preserving pipe-connected source spans.

    Returned text is pipe-normalized for the parser. start/end are half-open
    character offsets into the supplied body before normalization.
    """
    out: list[SourcePhrase] = []
    start = 0
    paren = brace = bracket = 0
    quote = False
    i = 0

    def append_piece(raw_start: int, raw_end: int) -> None:
        piece = body[raw_start:raw_end]
        leading = len(piece) - len(piece.lstrip())
        trailing = len(piece) - len(piece.rstrip())
        piece_start = raw_start + leading
        piece_end = raw_end - trailing
        if piece_start >= piece_end:
            return
        normalized = normalize_pipe_spacing(body[piece_start:piece_end])
        if normalized:
            out.append(SourcePhrase(normalized, piece_start, piece_end))

    while i < len(body):
        ch = body[i]
        if ch == "«":
            quote = True
            i += 1
            continue
        if ch == "»":
            quote = False
            i += 1
            continue
        if not quote:
            if ch == "(":
                paren += 1
            elif ch == ")":
                paren -= 1
            elif ch == "{":
                brace += 1
            elif ch == "}":
                brace -= 1
            elif ch == "[":
                bracket += 1
            elif ch == "]":
                bracket -= 1
            elif ch.isspace() and paren == brace == bracket == 0:
                run_start = i
                while i < len(body) and body[i].isspace():
                    i += 1
                prev_nonspace = body[run_start - 1] if run_start > 0 else ""
                next_nonspace = body[i] if i < len(body) else ""
                if prev_nonspace == "|" or next_nonspace == "|":
                    continue
                append_piece(start, run_start)
                start = i
                continue
        i += 1

    append_piece(start, len(body))
    return out


def split_phrases(body: str) -> list[str]:
    return [piece.text for piece in split_phrases_with_spans(body)]


def split_fields(phrase: str) -> list[str]:
    return split_top_level(phrase, "|")
