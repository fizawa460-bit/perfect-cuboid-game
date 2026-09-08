#!/usr/bin/env python3
"""Goal4AJ gen11: implementation repair of gen10, generation 2.

Gen10 established the semantic old-initialization collapse but failed before any
strict intersection because Singular treated `Current` as an existing package
identifier and the declaration `ideal Current=ideal(1)` was invalid in that
context.  Gen11 generation 1 then failed in the Python source-transform wrapper
before Singular because it renamed the wrapper's own source guard too early.

This generation source-locks gen10 and performs only the intended mechanical
repair:
* preserve the original gen10 pre-truncation prefix and replace its exact
  Current initialization block with a runtime rename Current -> StrictAcc plus
  unit-ideal initialization `ideal StrictAcc=1;`;
* rename Current -> StrictAcc only in the downstream gen10 source text, where
  regexes and final measurements refer to the generated Singular accumulator;
* rename mindeg -> denMinDeg downstream to avoid the second identifier clash;
* rename diagnostic GEN10 markers/schema to GEN11.

No mathematical condition, field, degree cap, divisor packet, truncation rule,
or credit boundary changes. Diagnostic only; no Q/F_B/E1/theorem credit.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN10 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_degree19_truncated_strict_kernel_gen10.py"
GEN10_BLOB = "740cd88223a7ee4b045f35ff370df021e94fbddd"
GEN10_FAILED_RUN = 34150955991
GEN10_FAILED_JOB = 101832986450
GEN11_G1_FAILED_RUN = 34151259036
GEN11_G1_FAILED_JOB = 101833894176


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN10) == GEN10_BLOB
src = GEN10.read_text(encoding="utf-8")
old_block = '''if "ideal Current=surf;" not in s:\n    raise SystemExit("parent Current initialization moved")\ns = s.replace("ideal Current=surf;", "ideal Current=ideal(1);", 1)'''
new_block = '''if "ideal Current=surf;" not in s:\n    raise SystemExit("parent Current initialization moved")\ns = re.sub(r"\\bCurrent\\b", "StrictAcc", s)\ns = s.replace("ideal StrictAcc=surf;", "ideal StrictAcc=1;", 1)'''
assert old_block in src
src = src.replace(old_block, new_block, 1)

# Only downstream Python source must refer to the renamed generated-Singular
# accumulator.  Do not alter the source-guard block above a second time.
marker = "trunc_proc = r'''"
prefix, sep, tail = src.partition(marker)
assert sep == marker
# Prefix already contains the repaired runtime rename. All remaining references
# are downstream generated-Singular regex/tail references.
tail = tail.replace("Current", "StrictAcc").replace("mindeg", "denMinDeg")
src = prefix + sep + tail
src = src.replace("GEN10", "GEN11").replace("gen10", "gen11")

# Add exact failed-generation provenance to the emitted diagnostic only.
src = src.replace(
    '"source_locks": {',
    '"source_locks": {\n'
    '        "gen10_failed_run": 34150955991,\n'
    '        "gen10_failed_job": 101832986450,\n'
    '        "gen10_blob_sha1": "740cd88223a7ee4b045f35ff370df021e94fbddd",\n'
    '        "gen11_generation1_failed_run": 34151259036,\n'
    '        "gen11_generation1_failed_job": 101833894176,',
    1,
)

code = compile(src, str(GEN10) + "[gen11-generation2-repaired]", "exec")
exec(code, {"__name__": "__main__", "__file__": __file__})
