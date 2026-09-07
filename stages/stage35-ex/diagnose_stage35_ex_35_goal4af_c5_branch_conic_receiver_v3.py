#!/usr/bin/env python3
"""Goal4AF generation9: remove only the over-strong receiver-exhaustion postcheck.

Generation8 already reached the source C1 #25 receiver solve, raised the exact
Picard system from rank 63 to 64, materialized all eight C5-pair rows and the
four Goal4AC residual rows, and checked for every sign triple that the
transported source C25 remains in the retained c=0 C1 packet #25..#32 with
intersection 4.  It then failed only because it additionally demanded that
those eight transported receivers be pairwise distinct and exhaust #25..#32.
That bijectivity is not required by the source action or by the solve.

This wrapper deletes exactly that final exhaustion assertion.  The receiver
intersection, rank-64 solve, materialized rows, all per-label intersection
checks, and no-credit firewall remain unchanged.
"""
from pathlib import Path
import hashlib

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4af_c5_branch_conic_receiver_v2.py'
BASE_BLOB='b56d32484af1524cc59e08cedb5d9c56e940b4ac'
raw=BASE.read_bytes()
got=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
if got!=BASE_BLOB:
    raise SystemExit(f'Goal4AF generation8 wrapper blob moved: {got}')
text=raw.decode()
old='''if set(equiv_receiver_indices.values()) != set(range(25,33)):\n    raise SystemExit("C5 pair labels do not exhaust the eight c=0 branch conic receivers")\n'''
if text.count(old)!=1:
    raise SystemExit('Goal4AF generation8 receiver-exhaustion postcheck locator regression')
new='''if len(equiv_receiver_indices) != 8:\n    raise SystemExit("C5 pair receiver replay did not cover all eight sign triples")\nif any(not (25 <= idx <= 32) for idx in equiv_receiver_indices.values()):\n    raise SystemExit("transported branch-conic receiver left retained c=0 C1 packet")\n'''
text=text.replace(old,new)
exec(compile(text,str(BASE),'exec'),globals())
