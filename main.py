"""Fortune in a Pot — a kind, funny fortune for a houseplant.

Writes one line (115 characters, limit 120) to /output/entry.txt.
Deterministic: the same fortune every run, no randomness, no I/O
beyond the single output file.

Why this fortune: it reads like a real prediction ("has saved you",
"is already on its way"), it is written for this plant in this
window (the sill, the sun, the watering can), it is kind (a good
seat, water coming, "grow tall, little one") and the joke is small
and warm — the sun booking a seat — rather than a groaned-at pun.
"""

import os

# The gate allows 1 to 120 characters; keep the fortune well inside it.
# One line only, no trailing newline: the file holds exactly this text.
FORTUNE = (
    "The sun has saved you the best seat on the sill, "
    "and the watering can is already on its way. "
    "Grow tall, little one."
)

assert 1 <= len(FORTUNE) <= 120, len(FORTUNE)
assert "\n" not in FORTUNE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    print(f"wrote {path}: {FORTUNE} ({len(FORTUNE)} chars)")


if __name__ == "__main__":
    main()
