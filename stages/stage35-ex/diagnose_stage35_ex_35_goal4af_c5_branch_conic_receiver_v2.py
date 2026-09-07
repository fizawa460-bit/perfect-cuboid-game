#!/usr/bin/env python3
"""Goal4AF generation8 wrapper repair.

Generation7 stopped before mathematics because it tried to inject receiver
metadata into the *outer* generation6 wrapper with an over-specific string
locator.  Remove only that metadata-injection block.  The source C1 #25
receiver constraint, rank-64 solve, row materialization, equivariant replay,
and separate GOAL4AF_BRANCH_CONIC_RECEIVER_JSON marker are unchanged.
"""
from pathlib import Path
import hashlib

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4af_c5_branch_conic_receiver.py'
BASE_BLOB='e4291503ccff329546e939c2522359573f12dc2a'
raw=BASE.read_bytes()
got=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
if got!=BASE_BLOB:
    raise SystemExit(f'Goal4AF generation7 wrapper blob moved: {got}')
text=raw.decode()
start="old_summary = '''    \"known_curve_receiver_count_detecting_null\": len(null_receiver_rows),\\n'''\n"
end="text = text.replace(old_summary,new_summary)\n\n"
i=text.find(start)
if i<0:
    raise SystemExit('Goal4AF generation7 summary-wrapper repair start locator regression')
j=text.find(end,i)
if j<0:
    raise SystemExit('Goal4AF generation7 summary-wrapper repair end locator regression')
j+=len(end)
text=text[:i]+text[j:]
exec(compile(text,str(BASE),'exec'),globals())
