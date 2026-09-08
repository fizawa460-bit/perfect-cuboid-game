#!/usr/bin/env python3
"""Goal4AJ gen17 generation 2: bind the post-create denominator note blob.

Generation 1 was created before GitHub returned the note blob and therefore
contains only the sentinel __DEN31_NOTE_BLOB__. This wrapper source-locks that
exact generation-1 source, substitutes the observed immutable note blob, and
executes it unchanged otherwise. No mathematical condition, process order,
field, degree cap, truncation rule, or credit boundary changes.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN17 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_truncated_strict_kernel_gen17.py"
GEN17_BLOB = "8631c9818c2431d66dddc861472babf0f53a7b2b"
DEN31_NOTE_BLOB = "95c0eef4a420234964217d3ceb41e57ea5e5b95d"


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN17) == GEN17_BLOB
src = GEN17.read_text(encoding="utf-8")
sentinel = 'DEN31_NOTE_BLOB = "__DEN31_NOTE_BLOB__"'
replacement = f'DEN31_NOTE_BLOB = "{DEN31_NOTE_BLOB}"'
assert src.count(sentinel) == 1
src = src.replace(sentinel, replacement, 1)
code = compile(src, str(GEN17) + "[gen17-generation2-note-blob-bound]", "exec")
exec(code, {"__name__": "__main__", "__file__": __file__})
