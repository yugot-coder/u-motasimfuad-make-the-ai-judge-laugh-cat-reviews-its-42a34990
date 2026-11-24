#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one single-line one-star review, written by a house cat about
its human, to /output/entry.txt (or $OUTPUT_DIR/entry.txt when the
OUTPUT_DIR environment variable is set). Standard library only.

The review (164 characters, one line):

    1 star. Serves dinner at 7 when I ordered 5, closes the only door
    I need open, and evicts me from the warm laptop I pay rent on in
    dead mice. Would not adopt again.
"""

import os

REVIEW = (
    "1 star. Serves dinner at 7 when I ordered 5, closes the only door "
    "I need open, and evicts me from the warm laptop I pay rent on in "
    "dead mice. Would not adopt again."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters (1 to 200), and
    # the entry is exactly one line of text.
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)
    # Read-back verification: re-open the file just written and compare
    # its contents against the intended review explicitly, so a
    # truncated or corrupted write fails loudly instead of shipping
    # silently. An explicit check (not assert) stays active even when
    # Python runs with -O.
    with open(entry_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != REVIEW:
        raise SystemExit(
            f"error: read-back verification failed for {entry_path}: "
            f"expected {REVIEW!r}, found {written!r}"
        )


if __name__ == "__main__":
    main()
