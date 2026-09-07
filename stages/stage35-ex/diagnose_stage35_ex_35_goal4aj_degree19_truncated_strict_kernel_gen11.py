#!/usr/bin/env python3
"""Goal4AJ gen11: exact implementation repair of gen10.

Gen10 established the semantic old-initialization collapse but failed before any
strict intersection because Singular treated `Current` as an existing package
identifier and the declaration `ideal Current=ideal(1)` was invalid in that
context.  This wrapper source-locks gen10, performs only the mechanical repair
needed to test the already-authorized mathematics, and executes the repaired
program:

* rename the Singular accumulator token `Current` -> `StrictAcc` everywhere;
* initialize it as the unit ideal with `ideal StrictAcc=1;`;
* rename `mindeg` -> `denMinDeg` to avoid a second Singular identifier clash;
* rename diagnostic GEN10 markers/schema to GEN11.

No mathematical condition, field, degree cap, divisor packet, truncation rule,
or credit boundary is changed.  Diagnostic only; no Q/F_B/E1/theorem credit.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN10 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_degree19_truncated_strict_kernel_gen10.py"
GEN10_BLOB = "740cd88223a7ee4b045f35ff370df021e94fbddd"
FAILED_RUN = 34150955991
FAILED_JOB = 101832986450


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN10) == GEN10_BLOB
src = GEN10.read_text(encoding="utf-8")

# Fail closed if the exact implementation defect has moved.
assert 's.replace("ideal Current=surf;", "ideal Current=ideal(1);", 1)' in src
assert 'int mindeg=999;' in src

# Pure implementation repair; preserve all mathematical/source-lock content.
src = re.sub(r"\bCurrent\b", "StrictAcc", src)
src = src.replace("ideal StrictAcc=ideal(1);", "ideal StrictAcc=1;")
src = re.sub(r"\bmindeg\b", "denMinDeg", src)
src = src.replace("GEN10", "GEN11").replace("gen10", "gen11")

# Preserve provenance of the failed implementation generation in the emitted
# diagnostic without changing the parent mathematics.
src = src.replace(
    '"source_locks": {',
    '"source_locks": {\n        "gen10_failed_run": 34150955991,\n        "gen10_failed_job": 101832986450,\n        "gen10_blob_sha1": "740cd88223a7ee4b045f35ff370df021e94fbddd",',
    1,
)

code = compile(src, str(GEN10) + "[gen11-repaired]", "exec")
exec(code, {"__name__": "__main__", "__file__": __file__})
