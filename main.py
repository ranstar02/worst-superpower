"""Worst Superpower — make.fun entry.

Writes a single line inventing the most useless superpower to
/output/entry.txt (falling back to ./output/entry.txt).

Why this line wins: the power only ever helps the drivers *behind*
you — every traffic light you face stays red for you, while the cars
in your rear-view mirror sail through on green. You can picture it
instantly, and you never get a single benefit from it yourself.
No network, no randomness, stdlib only; the output is the same
on every run.
"""

import os

SUPERPOWER = "I can make traffic lights turn green, but only the ones behind me."


def main() -> None:
    # Self-check: the gate wants 1-140 UTF-8 characters, one line, not blank.
    assert 1 <= len(SUPERPOWER) <= 140, "superpower must be 1-140 characters"
    assert "\n" not in SUPERPOWER and "\r" not in SUPERPOWER, "must be one line"
    assert SUPERPOWER.strip(), "must not be only whitespace"

    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(SUPERPOWER)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(SUPERPOWER)

    print(SUPERPOWER)
    print(f"Characters: {len(SUPERPOWER)}")
    print(f"Wrote: {path}")


if __name__ == "__main__":
    main()
