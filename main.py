#!/usr/bin/env python3
"""Write the one-line resignation letter to /output/entry.txt.

The text is fixed, single-line, and validated against the competition gate:
strict UTF-8, 1..140 characters, not whitespace only, no trailing newline.
The file is published atomically via a temporary file plus os.replace, so the
grader can never observe a partial or truncated entry.
"""

import hashlib
import os
import tempfile

ENTRY = (
    "I resign as the kindergarten teacher. After nine years of telling "
    "children to use their words, I'm the one in time-out."
)
MIN_CHARS = 1
MAX_CHARS = 140


def validated_payload() -> bytes:
    """Return the exact entry bytes or raise if the gate would reject them."""
    if not MIN_CHARS <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be {MIN_CHARS}..{MAX_CHARS} characters")
    if ENTRY != ENTRY.strip() or not ENTRY.strip() or "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be one non-blank line with no padding")
    payload = ENTRY.encode("utf-8", errors="strict")
    if payload.decode("utf-8", errors="strict") != ENTRY:
        raise ValueError("entry is not round-trip UTF-8")
    if payload.endswith(b"\n") or payload.endswith(b"\r"):
        raise ValueError("entry must have no trailing newline")
    return payload


def write_atomically(out_dir: str, payload: bytes) -> str:
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    fd, temp_path = tempfile.mkstemp(prefix=".entry-", suffix=".tmp", dir=out_dir)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, target)
    except BaseException:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        raise
    return target


def main() -> None:
    payload = validated_payload()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = write_atomically(out_dir, payload)
    print(
        f"entry.txt: {len(ENTRY)} chars, {len(payload)} bytes, "
        f"sha256 {hashlib.sha256(payload).hexdigest()} -> {target}"
    )


if __name__ == "__main__":
    main()
