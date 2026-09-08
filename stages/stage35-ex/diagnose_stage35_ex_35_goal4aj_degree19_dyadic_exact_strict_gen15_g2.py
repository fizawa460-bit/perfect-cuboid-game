#!/usr/bin/env python3
"""Goal4AJ gen15 generation 2: remove irrelevant parent Current bookkeeping.

Generation 1 reached all 22 characteristic-zero strict membership checks and
printed PASS for every one, but then failed its completion guard because the
source-locked parent still contained Hilbert/print bookkeeping for its old
cumulative ideal named Current. In this Singular environment Current resolves
as a package after the old declaration fails, so those unused lines emit type
errors. This wrapper source-locks generation 1 and removes only that bookkeeping,
renaming the now-unused parent initializer. Mathematical conditions, dyadic lift,
field, symbolic powers, and 22 direct membership checks are unchanged.

Diagnostic only; no A1-exact, degree31, F_B, local, E1, Stage35, theorem, or
endpoint credit is granted here.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN15 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_degree19_dyadic_exact_strict_gen15.py"
GEN15_BLOB = "230eb5e67b15d7d30822c3c10906cbeca6062126"
GEN15_G1_FAILED_RUN = 34177910521
GEN15_G1_FAILED_JOB = 101910921519


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN15) == GEN15_BLOB
src = GEN15.read_text(encoding="utf-8")

marker = 's = s.split(cut, 1)[0]\n'
if src.count(marker) != 1:
    raise SystemExit("gen15 final-tail split marker moved")
repair = marker + r'''
# Generation-1 implementation repair: the direct membership replay no longer
# maintains the parent's cumulative Current ideal. Remove exactly its 22 Hilbert
# rows and 22 matching print rows, then rename the one unused initializer.
_parent_lines = s.splitlines()
_hilb_count = sum("hilb(Current,1)" in line for line in _parent_lines)
_print_count = sum(
    "GOAL4AJ_DEN_STRICT_STEP=" in line and "size(Current)" in line
    for line in _parent_lines
)
if _hilb_count != 22 or _print_count != 22:
    raise SystemExit(
        f"parent Current bookkeeping moved: hilb={_hilb_count}, print={_print_count}"
    )
s = "\n".join(
    line for line in _parent_lines
    if "hilb(Current,1)" not in line
    and not ("GOAL4AJ_DEN_STRICT_STEP=" in line and "size(Current)" in line)
) + "\n"
if s.count("ideal Current=surf;") != 1:
    raise SystemExit("parent Current initializer count moved")
s = s.replace("ideal Current=surf;", "ideal DyadicUnusedCurrent=surf;", 1)
if re.search(r"\bCurrent\b", s):
    raise SystemExit("unexpected residual Current reference after gen15-g2 repair")
'''
src = src.replace(marker, repair, 1)

src = src.replace(
    '"source_locks": {',
    '"source_locks": {\n'
    '        "gen15_generation1_script_blob_sha1": "230eb5e67b15d7d30822c3c10906cbeca6062126",\n'
    '        "gen15_generation1_failed_run": 34177910521,\n'
    '        "gen15_generation1_failed_job": 101910921519,',
    1,
)

code = compile(src, str(GEN15) + "[generation2-current-bookkeeping-repair]", "exec")
exec(code, {"__name__": "__main__", "__file__": __file__})
