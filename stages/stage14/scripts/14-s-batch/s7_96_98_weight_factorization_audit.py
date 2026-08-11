#!/usr/bin/env python3
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
paths = {
    's95': ROOT/'stages/stage14/14-s7-95/result.md',
    'm4fk': ROOT/'stages/stage14/14-4fk/result.md',
    'm4fm': ROOT/'stages/stage14/14-4fm/result.md',
    'work': ROOT/'stages/stage14/14-Work-btX32/result.md',
    's96': ROOT/'stages/stage14/14-s7-96/result.md',
    's97': ROOT/'stages/stage14/14-s7-97/result.md',
    's98': ROOT/'stages/stage14/14-s7-98/result.md',
    'report': ROOT/'stages/stage14/14-s-batch/s7-96-98-report.md',
}
for k,p in paths.items():
    assert p.exists(), (k,p)
t = {k:p.read_text() for k,p in paths.items()}

for needle in [
    'GLOBAL_S_WEIGHTED_UNITARY_DIVISOR_INCIDENCE_IDENTIFIED=true',
    'MAINLINE_4FM_E_SCALE_SPLIT_APPLIES_TO_SAME_S7_95_PACKET=true',
]:
    assert needle in t['work'], needle
assert 'COMPLEMENTARY_E_SCALE_SPLIT_EXPLICIT=true' in t['m4fm']
assert 'COMPLEMENTARY_E_LOCAL_MASK_EXPLICIT=true' in t['m4fk']
assert 'STAGE14_S7_96=COMPLETE_WEIGHTED_UNITARY_PACKET_SYNCHRONIZATION_AND_E_LOCAL_WEIGHT_FACTORIZATION' in t['s96']
assert 'STAGE14_S7_97=COMPLETE_FIXED_E_LOCAL_MASK_EXHAUSTION_AND_CANONICAL_REVERSE_WEIGHT_ISOLATION' in t['s97']
assert 'STAGE14_S7_98=COMPLETE_POLYNOMIAL_E_PRIMITIVE_PRODUCT_SCALE_SPLIT_TO_OUTER_OCCUPANCY_OR_TWO_SCALE_UNITARY_CORRELATION' in t['s98']
assert 'BATCH_STOP_REASON=receiver_change' in t['report']
assert 'NEXT=Stage14-s7-99' in t['report']


def unitary_divisors(n):
    return [d for d in range(1,n+1) if n%d==0 and gcd(d,n//d)==1]

# s7-96 / 97 exact coordinate reconstruction.
for E in [1,2,5,12]:
    for m in [6,10,12,30,45]:
        n = E*m
        for u in unitary_divisors(m):
            v = m//u
            assert gcd(u,v)==1
            q = u*v
            assert q == m
            assert n//q == E
            L = E*u*u
            # exact ratio identity L/n = u/v by cross multiplication
            assert L*v == n*u

# Fixed-E branch: all inner multiplicity is unitary orientation only.
for m in range(1,120):
    uds = unitary_divisors(m)
    assert len(uds) >= 1
    for u in uds:
        assert gcd(u,m//u)==1

# Polynomial-E / subpolynomial-m algebra: once (m,u) is fixed, varying E
# changes only n=Em while u/v remains fixed.
m,u = 30,5
v = m//u
ratio_num, ratio_den = u, v
for E in [7,11,19,37]:
    n = E*m
    L = E*u*u
    assert L*ratio_den == n*ratio_num

# Polynomial-E / polynomial-m sample maintains exact two-level factorization.
for E,m in [(101,210),(211,330),(307,462)]:
    n=E*m
    for u in unitary_divisors(m)[:4]:
        v=m//u
        assert n == E*u*v
        assert gcd(u,v)==1

for needle in [
    'FIXED_E_LOCAL_MASK_EXHAUSTED=true',
    'FIXED_E_COMPLETION_EXISTENCE_AUTOMATIC=false',
    'P0_POLYNOMIAL_ENTROPY_ONLY_IN_E=true',
    'P1_BOTH_E_AND_M_POLYNOMIAL=true',
    'RECEIVER_MATERIALLY_CHANGED=true',
]:
    assert needle in t['s97'] or needle in t['s98'], needle

print('STAGE14_S_BATCH_AUDIT=PASS')
print('S7_96_98_WEIGHT_FACTORIZATION_AUDIT=PASS')
