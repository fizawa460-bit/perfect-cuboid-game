#!/usr/bin/env python3
"""Goal4AF generation10: direct repair from generation7 source receiver wrapper.

Generation8 reached the mathematics: the source C1 #25 intersection raises the
exact sign+Galois Picard system from rank 63 to rank 64 and materializes eight
C5-pair rows plus the four Goal4AC residual rows.  Generation9 then stopped
before mathematics because it tried to patch a string that existed in the
underlying generation7 wrapper, not in the nested generation8 wrapper.

This leaf starts again from the exact generation7 wrapper and makes only two
wrapper-level changes:
  1. remove the nonessential attempt to inject receiver metadata into the
     inner generation6 summary; the separate receiver JSON remains;
  2. replace the over-strong requirement that transported C25 receivers are a
     bijection onto C1 #25..#32 by the source-required checks only: all eight
     sign triples are covered and every transported receiver stays in that
     retained c=0 C1 packet.

The C25 source intersection, rank-64 solve, per-label intersection replay,
materialized rows, and no-credit firewall are unchanged.
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'stages/stage35-ex/diagnose_stage35_ex_35_goal4af_c5_branch_conic_receiver.py'
BASE_BLOB = 'e4291503ccff329546e939c2522359573f12dc2a'
raw = BASE.read_bytes()
got = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
if got != BASE_BLOB:
    raise SystemExit(f'Goal4AF generation7 receiver wrapper blob moved: {got}')
text = raw.decode()

# Remove only the failed metadata injection into the inner generation6 summary.
start = "old_summary = '''    \"known_curve_receiver_count_detecting_null\": len(null_receiver_rows),\\n'''\n"
end = "text = text.replace(old_summary,new_summary)\n\n"
i = text.find(start)
if i < 0:
    raise SystemExit('Goal4AF generation7 summary-wrapper repair start locator regression')
j = text.find(end, i)
if j < 0:
    raise SystemExit('Goal4AF generation7 summary-wrapper repair end locator regression')
text = text[:i] + text[j + len(end):]

# Remove only the post-materialization receiver-bijection assumption.
old = '''if set(equiv_receiver_indices.values()) != set(range(25,33)):\n    raise SystemExit("C5 pair labels do not exhaust the eight c=0 branch conic receivers")\n'''
new = '''if len(equiv_receiver_indices) != 8:\n    raise SystemExit("C5 pair receiver replay did not cover all eight sign triples")\nif any(not (25 <= idx <= 32) for idx in equiv_receiver_indices.values()):\n    raise SystemExit("transported branch-conic receiver left retained c=0 C1 packet")\n'''
if text.count(old) != 1:
    raise SystemExit('Goal4AF generation7 receiver-exhaustion postcheck locator regression')
text = text.replace(old, new)

exec(compile(text, str(BASE), 'exec'), globals())
