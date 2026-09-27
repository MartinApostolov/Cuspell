#!/usr/bin/env python3
"""Deterministic smoke fuzzer for the Cuspell reference parser.

This is not a proof of correctness. It is intended to expose crashes,
non-determinism, runaway recursion, and surprising diagnostic categories while
we expand the machine-readable language.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import random
import sys

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"src"
if str(SRC) not in sys.path:
    sys.path.insert(0,str(SRC))

from cuspell.language import Language
from cuspell.parser import Parser

SEEDS=[
    "Cat Self.",
    "SolidWater This.",
    "!Move This Here.",
    "!Move This :path ThisPath.",
    "!If Life This EndLife This.",
    "All [a:Human] Life $a.",
    "Some [a:Human] Life $a.",
    "!Sequence {Move This Here,EndLife Self}.",
    "!Preserve Volume This Change This Density Multiply @@ BeforeValue Density This.",
    "Same Unique Nearest Collect [a:Human] Life $a Self Self.",
    "More Count Collect [a:Human] Life $a Zero.",
    "!Repeat @@ Move This Here.",
    "!When Move This Here Now.",
]


def random_surface(rng: random.Random, language: Language) -> str:
    roots=list(language.entries)
    atoms=[
        "This","Self","You","Here","There","ThisRegion","ThisPath",
        "ThisEvent","ThatEvent","ThisInterval","Now","@","@@","Zero",
        "SolidWater","NotLife","EndLife","EndExist","EndIn","OppositeBefore",
    ]
    roles=[":source",":goal",":path",":theme"]
    pool=roots+atoms+roles
    count=rng.randint(1,9)
    tokens=[rng.choice(pool) for _ in range(count)]

    # Occasionally turn a contiguous section into an explicit hard group.
    if count>=2 and rng.random()<0.35:
        start=rng.randrange(0,count-1)
        end=rng.randrange(start+2,min(count,start+5)+1)
        tokens[start:end]=["|".join(tokens[start:end])]

    mood=rng.choice(["","!","?"])
    return mood+" ".join(tokens)+"."


def mutate_seed(rng: random.Random, seed: str) -> str:
    mood=""
    body=seed[:-1]
    if body.startswith(("!","?")):
        mood,body=body[0],body[1:]
    # Preserve grouped collection text as a rough token for mutation.
    tokens=body.split()
    if not tokens:
        return seed
    action=rng.randrange(4)
    if action==0 and len(tokens)>=2:
        i=rng.randrange(len(tokens)-1)
        tokens[i:i+2]=[tokens[i]+"|"+tokens[i+1]]
    elif action==1 and len(tokens)>=2:
        del tokens[rng.randrange(len(tokens))]
    elif action==2:
        i=rng.randrange(len(tokens))
        tokens.insert(i,tokens[i])
    else:
        i=rng.randrange(len(tokens))
        tokens[i]=rng.choice(["This","Here","@@","Life","Move","Zero"])
    return mood+" ".join(tokens)+"."


def run(cases:int=1000, seed:int=1337) -> Counter:
    language=Language.load(ROOT)
    parser=Parser(language)
    rng=random.Random(seed)
    counts=Counter()

    surfaces=list(SEEDS)
    while len(surfaces)<cases:
        if rng.random()<0.45:
            surfaces.append(mutate_seed(rng,rng.choice(SEEDS)))
        else:
            surfaces.append(random_surface(rng,language))

    for source in surfaces[:cases]:
        first=parser.check(source).to_dict()
        second=parser.check(source).to_dict()
        if first!=second:
            raise AssertionError(f"non-deterministic parse for {source!r}")
        if first["valid"]:
            counts["VALID"]+=1
        elif first["diagnostics"]:
            counts[first["diagnostics"][0]["code"]]+=1
        else:
            counts["NO_DIAGNOSTIC"]+=1
    return counts


def main(argv=None)->int:
    ap=argparse.ArgumentParser(description="Deterministic Cuspell parser smoke fuzzer")
    ap.add_argument("--cases",type=int,default=1000)
    ap.add_argument("--seed",type=int,default=1337)
    args=ap.parse_args(argv)
    counts=run(args.cases,args.seed)
    print(f"cases: {args.cases}")
    for name,count in sorted(counts.items()):
        print(f"{name}: {count}")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
