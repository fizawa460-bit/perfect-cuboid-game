#!/usr/bin/env python3
"""Goal4AJ gen17 generation 3: bind all post-create immutable source locks.

Generation 1 contains two creation-time placeholders/temporary locks: the
post-create denominator-note blob and a provisional retained92 packet SHA.
Generation 2 bound only the note blob. This generation source-locks both prior
files and substitutes the observed immutable note blob plus the locator-run
retained92 packet SHA. No mathematical condition, process order, field, degree
cap, truncation rule, or credit boundary changes.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN17 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_truncated_strict_kernel_gen17.py"
GEN17_G2 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_truncated_strict_kernel_gen17_g2.py"
GEN17_BLOB = "8631c9818c2431d66dddc861472babf0f53a7b2b"
GEN17_G2_BLOB = "7a6dad9321d3029a0d8e8ec245dbd571133baef6"
DEN31_NOTE_BLOB = "95c0eef4a420234964217d3ceb41e57ea5e5b95d"
STRICT_PACKET_SHA256 = "4f9c446900aab6d79e433bf84400e3b82d07ab9c4c38e749c3167d6e449a3717"


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN17) == GEN17_BLOB
assert git_blob(GEN17_G2) == GEN17_G2_BLOB
src = GEN17.read_text(encoding="utf-8")
old_note = 'DEN31_NOTE_BLOB = "__DEN31_NOTE_BLOB__"'
new_note = f'DEN31_NOTE_BLOB = "{DEN31_NOTE_BLOB}"'
old_packet = 'STRICT_PACKET_SHA256 = "d3af7bfe3fd390b4af8d6688d6ab885716cff1738400a218f09413dffde6936c"'
new_packet = f'STRICT_PACKET_SHA256 = "{STRICT_PACKET_SHA256}"'
assert src.count(old_note) == 1
assert src.count(old_packet) == 1
src = src.replace(old_note, new_note, 1).replace(old_packet, new_packet, 1)
code = compile(src, str(GEN17) + "[gen17-generation3-all-source-locks-bound]", "exec")
exec(code, {"__name__": "__main__", "__file__": __file__})
