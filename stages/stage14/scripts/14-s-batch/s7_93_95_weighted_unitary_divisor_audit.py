#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
paths = {
    's92': ROOT/'stages/stage14/14-s7-92/result.md',
    'm4fi': ROOT/'stages/stage14/14-4fi/result.md',
    'm4fj': ROOT/'stages/stage14/14-4fj/result.md',
    'work': ROOT/'stages/stage14/14-Work-bsX31/result.md',
    's93': ROOT/'stages/stage14/14-s7-93/result.md',
    's94': ROOT/'stages/stage14/14-s7-94/result.md',
    's95': ROOT/'stages/stage14/14-s7-95/result.md',
}
for k,p in paths.items():
    assert p.exists(), (k,p)
t = {k:p.read_text() for k,p in paths.items()}

# Merged source locks.
assert 'PRIMITIVE_RATIO_WINDOW_MULTIPLICATIVE_WIDTH=Bo1' in t['s92']
assert 'HEAVY_SUPPORT_CANNOT_CONCENTRATE_AT_RECIPROCAL_WINDOW_ENDPOINTS=true' in t['m4fi']
assert 'INTERIOR_EXISTENTIAL_SUPPORT_INCIDENCE_EXPONENT_EQUIVALENT=true' in t['m4fj']
assert 'GLOBAL_S_PRIMITIVE_DIVISOR_RATIO_COORDINATE_IDENTIFIED=true' in t['work']
assert 'GLOBAL_S_RADIAL_ENDPOINT_STRIPS_DISCHARGED=true' in t['work']

# New boundary locks.
for needle in [
    'PHYSICAL_INCIDENCE_PULLED_BACK_TO_RATIO_COORDINATE=true',
    'E_SQUAREFREE_KERNEL_DECOMPOSITION_IS_TAUTOLOGICAL=true',
    'COMPLEMENTARY_E_FIXED_KERNEL_COPRIMALITY_EXPOSED=true',
]:
    assert needle in t['s93'], needle
for needle in [
    'COPRIME_FACTOR_PAIR_EQUALS_FULL_PRIME_POWER_ORIENTATION=true',
    'RATIO_WINDOW_IS_SIGNED_PRIME_POWER_LOG_INTERVAL=true',
    'INNER_RATIO_ENDPOINT_DISTINCT_FROM_RADIAL_ENDPOINT=true',
]:
    assert needle in t['s94'], needle
for needle in [
    'PRIMITIVE_COPRIME_PAIR_EQUIVALENT_TO_UNITARY_DIVISOR=true',
    'RATIO_WINDOW_TO_UNITARY_DIVISOR_INTERVAL_EXACT=true',
    'WEIGHTED_UNITARY_DIVISOR_INCIDENCE_DEFINED=true',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'NEXT=Stage14-s7-96',
]:
    assert needle in t['s95'], needle


def sqf(n: int) -> int:
    out = 1
    p = 2
    while p*p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p += 1
    if n > 1:
        out *= n
    return out


def prime_power_blocks(n: int):
    blocks=[]
    p=2
    while p*p<=n:
        if n%p==0:
            pp=1
            while n%p==0:
                n//=p
                pp*=p
            blocks.append(pp)
        p+=1
    if n>1:
        blocks.append(n)
    return blocks


def divisors(n: int):
    return [d for d in range(1,n+1) if n%d==0]

# Every E has the unique sqf(E)*square form used in s7-93.
for E in range(1,500):
    J=sqf(E)
    z=E//J
    r=int(z**0.5)
    assert r*r==z, (E,J,z)

# Primitive pair <-> q plus unitary divisor; coordinate identities remain exact.
samples=[
    (2*3*5, 2, 15, 7),
    (2**3*3**2*5, 8*5, 9, 11),
    (7**2*11*13, 49*13, 11, 3),
    (2**4*17**2, 16, 289, 5),
]
alpha,beta=3,5
for q,u,v,E in samples:
    assert u*v==q
    assert gcd(u,v)==1
    n=E*q
    assert n%(u*v)==0
    L=E*u*u
    assert Fraction(L,n)==Fraction(u,v)
    assert alpha*L==Fraction(alpha*n*u,v)
    assert beta*E*v*v==Fraction(beta*n*v,u)
    assert gcd(u,q//u)==1  # unitary divisor condition

# All coprime factorizations of q are exactly unitary divisors; count is 2^omega(q).
for q in [1,6,12,60,72,210,360,2310]:
    uds=[u for u in divisors(q) if gcd(u,q//u)==1]
    pairs=[(u,q//u) for u in divisors(q) if gcd(u,q//u)==1]
    assert len(uds)==len(pairs)
    assert len(uds)==2**len(prime_power_blocks(q))
    for u,v in pairs:
        assert u*v==q and gcd(u,v)==1

# Ratio short window <=> square-root unitary-divisor interval, checked without floating point.
windows=[(Fraction(1,4),Fraction(4,1)),(Fraction(2,3),Fraction(3,2)),(Fraction(3,5),Fraction(5,3))]
for q in [6,12,30,60,210]:
    for u in divisors(q):
        if gcd(u,q//u)!=1:
            continue
        ratio=Fraction(u*u,q)
        for lo,hi in windows:
            lhs=(lo<=ratio<=hi)
            rhs=(lo*q<=u*u<=hi*q)
            assert lhs==rhs

print('STAGE14_S_BATCH_AUDIT=PASS')
print('S7_93_95_WEIGHTED_UNITARY_DIVISOR_AUDIT=PASS')
