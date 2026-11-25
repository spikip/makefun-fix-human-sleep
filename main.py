"""Entry for the make.fun bounty "Fix Human Sleep: Funniest Patch Note".

The program writes a single patch note to /output/entry.txt. The note
announces version 2.1 of human sleep: the bug where eight hours of
sleep still left the user tired is fixed, sleep now actually works,
and the only side effect is that mornings remain terrible. It reads
like a real changelog entry, with a version number, a fixed bug, and
a deadpan side effect, which is exactly the changelog voice the
bounty asks for. The joke is that the fix works and nothing gets
better, because mornings were never the bug. The gate allows 1 to
160 characters of UTF-8 text, so the line is checked against that
cap before it is written — the fix ships, the mornings do not.
"""

import os

ENTRY = (
    "v2.1: Fixed a bug where eight hours of sleep still left the user "
    "tired. Sleep now works. Side effect: mornings remain terrible."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
