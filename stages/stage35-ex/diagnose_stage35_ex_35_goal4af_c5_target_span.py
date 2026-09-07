#!/usr/bin/env python3
"""Goal4AF: exact target-span test after adjoining four C5 residual pair classes.

This is a marked-Picard/divisor-packet linear-algebra diagnostic only.  The
four C5 residual-pair classes are first recomputed by the source C1 #25
receiver solve.  Each primitive INDLIST64 coordinate row is then embedded in
the retained 140-divisor packet by using the corresponding 64 primitive basis
curves as coefficients.  The embedding is checked by mapping it back through
the retained Picard marking.

The resulting four marked representatives are adjoined to Goal4AB's exact
43 complete degree-16 linear-section divisor columns (rank 31), and the fixed
69-support class-B target is tested for exact Q-span membership.

A positive span result would not itself materialize an explicit rational
function F_B; a negative result would block only this marked-representative
augmentation.  No theorem, endpoint, Brauer-Manin, or E1 credit is granted.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import runpy
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
SNAP65 = ROOT / 'stages/stage35-ex/snapshots/MAIN-STATE-V65-e08f399034dc.json'
GOAL4AB = ROOT / 'stages/stage35-ex/verify_stage35_ex_35_goal4ab.py'
RECEIVER = ROOT / 'stages/stage35-ex/diagnose_stage35_ex_35_goal4af_c5_branch_conic_receiver_v4.py'
REC = ROOT / 'stages/stage33/33-07/certify_two_coordinate_swap_picard_rows.py'

LOCKS = {
    SNAP65: '1479da3b0dbb1ce3b60941375261e2660d7847b6',
    GOAL4AB: '347cc43a60f7772d6c8b3f4145839cf9978b4114',
    RECEIVER: 'cd80f7533dd865eb68ad75e0f25454d542ebf4e7',
    REC: '296e2005f822ae89c1aa085161553fe9ef76d077',
}


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()


for p, want in LOCKS.items():
    got = blob(p)
    if got != want:
        raise SystemExit(f'Goal4AF target-span source lock moved: {p}: {got}')

# Reconstruct Goal4AB against its immutable live V65 state, not current V68.
snap65text = SNAP65.read_text()
snap65 = json.loads(snap65text)
if snap65['schema'] != 'STAGE35_EX_PESCH_E1_STATE_V65_GOAL4AB_LOW_DEGREE_RR_FEEDERS_BLOCKED_GENERAL_QI_PRINCIPAL_FUNCTION_PENDING_AUDIT':
    raise SystemExit('Goal4AF V65 snapshot schema regression')
orig_read_text = Path.read_text
state_resolved = STATE.resolve()

def patched_read_text(self: Path, *a, **k):
    if self.resolve() == state_resolved:
        return snap65text
    return orig_read_text(self, *a, **k)

Path.read_text = patched_read_text
try:
    with contextlib.redirect_stdout(io.StringIO()):
        ab = runpy.run_path(str(GOAL4AB))
finally:
    Path.read_text = orig_read_text

M = sp.Matrix(ab['M'])
v = sp.Matrix(ab['v'])
known = [[int(x) for x in r] for r in ab['known']]
picclass = ab['picclass']
if M.shape[0] != 140 or M.shape[1] != 43 or M.rank() != 31:
    raise SystemExit(f'Goal4AB section matrix regression: shape={M.shape}, rank={M.rank()}')
if sum(int(x) != 0 for x in v) != 69:
    raise SystemExit('Goal4AB formal target support regression')
if sp.linsolve((M, v)) != sp.EmptySet:
    raise SystemExit('Goal4AB old target unexpectedly entered rank-31 span')

# Recompute the source-derived C5 pair rows locally and silently.
with contextlib.redirect_stdout(io.StringIO()):
    c5 = runpy.run_path(str(RECEIVER))
summary = c5['summary']
if summary['pair_rows_materialized'] is not True or summary['pair_count'] != 8:
    raise SystemExit('Goal4AF receiver replay did not materialize eight pair rows')
if summary['goal4ac_residual_pair_count'] != 4:
    raise SystemExit('Goal4AF receiver replay did not materialize four residual rows')
if summary['target_span_computed'] is not False:
    raise SystemExit('Goal4AF receiver leaf unexpectedly precomputed target span')
residual = summary['goal4ac_residual_pairs']

# Recover only the primitive INDLIST order from the exact Stage33 certifier.
s33 = REC.parent
sys.path.insert(0, str(s33))
try:
    with contextlib.redirect_stdout(io.StringIO()):
        rec = runpy.run_path(str(REC))
finally:
    if sys.path and sys.path[0] == str(s33):
        sys.path.pop(0)
indlist = [int(x) for x in rec['INDLIST']]
if len(indlist) != 64 or len(set(indlist)) != 64 or any(not (1 <= x <= 140) for x in indlist):
    raise SystemExit('Stage33 primitive INDLIST order regression')

# Embed an INDLIST64 coordinate row into the 140 retained divisor packet.
def embed(row64):
    if len(row64) != 64:
        raise SystemExit('C5 residual marked row width regression')
    out = [0] * 140
    for j, c in enumerate(row64):
        out[indlist[j] - 1] = int(c)
    return out

embedded = []
marked64 = []
for r in residual:
    row = [int(x) for x in r['total_pullback_pair_INDLIST64']]
    strict = [int(x) for x in r['strict_pair_INDLIST64']]
    # Generation10 found no exceptional correction for these C5 pairs.
    if row != strict:
        raise SystemExit('Goal4AF residual strict/total row unexpectedly differs')
    e = embed(row)
    if [int(x) for x in picclass(e)] != row:
        raise SystemExit('C5 marked representative failed retained Picard-image round trip')
    embedded.append(e)
    marked64.append(row)

C = sp.Matrix(140, 4, lambda i, j: embedded[j][i])
A = M.row_join(C)
old_rank = M.rank()
residual_column_rank = C.rank()
aug_rank = A.rank()
solset = sp.linsolve((A, v))
in_span = solset != sp.EmptySet

solution_summary = None
if in_span:
    sol = list(next(iter(solset)))
    syms = sorted(set().union(*(x.free_symbols for x in sol)), key=str)
    one = [sp.simplify(x.subs({s: 0 for s in syms})) for x in sol]
    if A * sp.Matrix(one) != v:
        raise SystemExit('Goal4AF target-span witness substitution regression')
    solution_summary = {
        'free_parameter_count': len(syms),
        'nonzero_linear_section_coefficient_count': sum(x != 0 for x in one[:43]),
        'c5_residual_coefficients': [str(x) for x in one[43:47]],
        'max_coefficient_numerator_abs': max(abs(int(sp.numer(x))) for x in one),
        'max_coefficient_denominator': max(int(sp.denom(x)) for x in one),
    }

out = {
    'schema': 'STAGE35_EX_GOAL4AF_C5_MARKED_REPRESENTATIVE_TARGET_SPAN_DIAGNOSTIC_V1',
    'goal4ab_linear_section_column_count': 43,
    'goal4ab_linear_section_span_rank': old_rank,
    'formal_target_support_count': 69,
    'c5_goal4ac_residual_pair_count': 4,
    'c5_residual_distinct_marked_picard64_row_count': len({tuple(r) for r in marked64}),
    'c5_residual_embedded_column_rank': residual_column_rank,
    'augmented_column_count': A.cols,
    'augmented_span_rank': aug_rank,
    'formal_target_in_Q_span_after_adjoining_c5_marked_representatives': in_span,
    'solution_summary': solution_summary,
    'embedding_semantics': 'INDLIST64 coefficients placed on the corresponding 64 retained primitive basis curves inside the 140-divisor packet; checked by exact Picard-image round trip',
    'actual_C5_support_identified_with_marked_representative': False,
    'explicit_F_B_materialized': False,
    'general_principal_function_problem_closed': False,
    'remote_cas_used': False,
    'theorem_credit': False,
    'endpoint_credit': False,
    'E1_proved': False,
    'stage35_closed': False,
}
print('GOAL4AF_TARGET_SPAN_JSON=' + json.dumps(out, sort_keys=True, separators=(',', ':')))
