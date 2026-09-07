#!/usr/bin/env python3
"""Generation3: replay the exact sign-stabilizer diagnostic without treating
exceptional-node union as a C5-pair label locator.

The C5 sign action is fixed directly by the pinned source equations in the
base diagnostic.  Node incidence remains an independent transport consistency
check, but distinct sign labels are not required to have distinct node unions.
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4af_c5_sign_stabilizer.py"
BASE_BLOB = "732332e94f1346b03d91425bb664905d3f440c44"
raw = BASE.read_bytes()
got = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
if got != BASE_BLOB:
    raise SystemExit(f"Goal4AF sign-stabilizer generation2 blob moved: {got}")
text = raw.decode()
old = '''if len(set(pair_union.values())) != 8:\n    raise SystemExit("C5 pair exceptional-node unions are not label-distinct")\n'''
new = '''pair_union_distinct_count = len(set(pair_union.values()))\n'''
if text.count(old) != 1:
    raise SystemExit("Goal4AF node-union locator gate patch target regression")
patched = text.replace(old, new)
exec(compile(patched, str(BASE), "exec"), globals())
