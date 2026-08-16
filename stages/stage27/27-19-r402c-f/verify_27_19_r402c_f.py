#!/usr/bin/env python3
from pathlib import Path
from math import gcd
from itertools import product
import json

ROOT = Path(__file__).resolve().parents[3]

# Exact reduced-core algebra: if A/D=p/q in lowest terms and g=gcd(A,D),
# then A=pg,D=qg and g*max(p,q)=max(A,D).
for m in range(2, 9):
    for n in range(1, m):
        if gcd(m, n) != 1:
            continue
        for r in range(2, 9):
            for s in range(1, r):
                if gcd(r, s) != 1:
                    continue
                A = s*s*(m*m+n*n)
                D = n*n*(r*r-s*s)
                g = gcd(A, D)
                p, q = A//g, D//g
                assert gcd(p, q) == 1
                assert A == p*g and D == q*g
                assert g*max(p, q) == max(A, D)

# Exact combinatorial identities and inequalities for arbitrary occupied fibers.
for k in range(1, 6):
    for weights in product(range(1, 6), repeat=k):
        N = sum(weights)
        S = len(weights)
        C = sum(w*(w-1) for w in weights)
        E = sum(w*w for w in weights)
        assert E == N + C
        assert E >= N
        assert 2*(N-S) <= C
        assert N*N <= S*(N+C)
        # Equivalent square form of N <= S+sqrt(S*C).
        assert (N-S)*(N-S) <= S*C
        for L in range(2, 6):
            heavy = [w for w in weights if w >= L]
            assert len(heavy)*L*(L-1) <= C
            assert sum(heavy)*(L-1) <= C

# Result-surface firewalls.
checks = {
    'stages/stage27/27-19-r402c/result.md': [
        'TAU_CORE_HEIGHT_BOUND=g<2B^2/H(tau)',
        'CORE_TRADEOFF_FIXED_POWER_SAVING_PROVED=false',
    ],
    'stages/stage27/27-19-r402d/result.md': [
        'TAU_FULL_ENERGY_IDENTITY_PROVED=true',
        'TAU_ENERGY_DIAGONAL_LOWER_BOUND=E_tau>=N2',
        'RAW_SECOND_MOMENT_SHORTCUT_CLOSED_AT_HALFWALL=true',
    ],
    'stages/stage27/27-19-r402e/result.md': [
        'TAU_HYBRID_BOUND=N<=S+sqrt(S*C)',
        'TAU_HYBRID_STRICT_SUBHALF_GATE=sigma<1/2_and_sigma+kappa<1',
        'OFFDIAGONAL_ALONE_BREAKS_HALFWALL=false',
    ],
    'stages/stage27/27-19-r402f/result.md': [
        'TAU_BAND_HYBRID_BOUND=N_T<=S_T+sqrt(S_T*C_T)',
        'TAU_BAND_STRICT_SUBHALF_THEOREM_PROVED=false',
        'BATCH_STOP_REASON=EXACT_ARITHMETIC_REPRESENTATION_THEOREM_REQUIRED',
    ],
}
for rel, needles in checks.items():
    text = (ROOT / rel).read_text(encoding='utf-8')
    for needle in needles:
        assert needle in text, (rel, needle)

reg = json.loads((ROOT / 'stages/stage27/27-19-r402c-f/batch-registry.json').read_text())
assert reg['routes'] == ['Stage27-19-r402c','Stage27-19-r402d','Stage27-19-r402e','Stage27-19-r402f']
assert reg['strict_sub_sqrt_upper_proved'] is False
assert reg['audit_status'] == 'PENDING_BATCH_FRESH_AUDIT'
assert reg['next_route_after_audit'] == '27-19-r402g'

ctl = json.loads((ROOT / 'stages/stage27/27-controller.json').read_text())
r402b = ctl['derived_routes']['Stage27-19-r402b']
assert r402b['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'
assert r402b['audit_status'] == 'PASS'
assert r402b['pr'] == 1039
assert r402b['merge_commit'] == 'f70d5313cd3eb148d2fdcb99f5d573bd14e91f5e'
for suffix in 'cdef':
    route = ctl['derived_routes'][f'Stage27-19-r402{suffix}']
    assert route['status'] == 'BATCH_SUBMITTED_PENDING_FRESH_AUDIT'
    assert route['audit_status'] == 'PENDING'
    assert route['merge_allowed'] is False
    assert route['strict_sub_sqrt_upper_proved'] is False
state = ctl['state']
assert state['CURRENT_CHECKPOINT'] == 40
assert state['AUDIT_STATUS'] == 'PENDING'
assert state['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-19-r402-audit'

status = (ROOT / 'docs/00_CURRENT_RESEARCH_STATUS.md').read_text(encoding='utf-8')
for needle in [
    'CURRENT_STAGE=Stage27-19-r402c-f-BATCH-SUBMITTED-PENDING-FRESH-AUDIT',
    'STAGE27_19_R402B_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1039',
    'STAGE27_19_R402C_F_STATUS=MULTI_ROUTE_BATCH_SUBMITTED_PENDING_FRESH_AUDIT',
    'STAGE27_TAU_CORE_HEIGHT_TRADEOFF_PROVED=true',
    'STAGE27_TAU_FULL_ENERGY_DIAGONAL_BARRIER_PROVED=true',
    'STAGE27_TAU_OFFDIAGONAL_HYBRID_GATE_PROVED=true',
    'STAGE27_TAU_DYADIC_BAND_CONTRACT_MATERIALIZED=true',
    'STAGE27_STRICT_SUB_SQRT_UPPER_PROVED=false',
]:
    assert needle in status, needle

print('Stage27-19-r402c-f verifier: PASS')
