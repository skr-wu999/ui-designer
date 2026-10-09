"""Generate seed strings for the Discover stage of the ui-designer skill.

A model can only predict the most likely next token, so it cannot act randomly; this script
supplies the entropy from outside. Each seed becomes one design direction, so log the seed
next to the direction it produced to reproduce a direction later.

    python seed_string.py                     one 40-character seed
    python seed_string.py --count 4           four candidates to choose from
    python seed_string.py --length 64         longer string, more subpatterns to find
    python seed_string.py --count 3 --json    machine-readable, for logging
    python seed_string.py --seed 12345        reproduce a previous run exactly
"""

from __future__ import annotations

import argparse
import json
import random
import secrets
import string

ALPHABET = string.ascii_letters + string.digits


def make_seed(length: int, rng: random.Random | None) -> str:
    if rng is not None:
        return "".join(rng.choice(ALPHABET) for _ in range(length))
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate seed strings for design direction injection.")
    parser.add_argument("--length", type=int, default=40, help="characters per seed (default 40)")
    parser.add_argument("--count", type=int, default=1, help="how many seeds to print (default 1)")
    parser.add_argument("--seed", type=int, default=None, help="reproduce a previous run from this integer")
    parser.add_argument("--json", action="store_true", help="print JSON instead of one seed per line")
    args = parser.parse_args()

    if args.length < 8:
        parser.error("--length must be at least 8")
    if args.count < 1:
        parser.error("--count must be at least 1")

    rng = random.Random(args.seed) if args.seed is not None else None
    seeds = [make_seed(args.length, rng) for _ in range(args.count)]

    if args.json:
        print(json.dumps({"length": args.length, "seed": args.seed, "seeds": seeds}, indent=2))
    else:
        print("\n".join(seeds))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
