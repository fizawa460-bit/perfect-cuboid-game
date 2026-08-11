#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
paths = {
    's89': ROOT/'stages/stage14/14-s7-89/result.md',
    'm4fg': ROOT/'stages/stage14/14-4fg/result.md',
    'work': ROOT/'stages/stage14/14-Work-brX30/result.md',
    's90': ROOT/'stages/stage14/14-s7-90/result.md',
    's91': ROOT/'stages/stage14/14-s7-91/result.md',
    's92': ROOT/'stages/stage14/14-s7-92/result.md',
}
for k,p in paths.items():
    assert p.exists(), (k,p)
t = {k:p.read_text() for k,p in paths.items()}

# Source and boundary locks.
assert 'PEELED_ROOT_PAIR_NORMAL_FORM=true' in t['s89']
assert 'ROOT_PAIR_SINGLE_L_COORDINATE_PROVED=true' in t['m4fg']
assert 'GLOBAL_S_RECIPROCAL_DIVISOR_WINDOW_COORDINATE_IDENTIFIED=true' in t['work']
for needle in [
    'COMMON_SQUAREPART_GCD_PEELED=true',
    'PEELED_TRIPLE_TO_E_U_V_BIJECTION=true',
    'FIXED_N_E_U_V_FIBER=Bo1',
]:
    assert needle in t['s90'], needle
for needle in [
    'COMMON_DILATION_ELIMINATED_FROM_ROOT_WINDOWS=true',
    'PHYSICAL_ROOT_WINDOWS_PROJECTED_TO_PRIMITIVE_RATIO=true',
    'L_s_equals_n_times_u_over_v=true',
]:
    assert needle in t['s91'], needle
for needle in [
    'ARCHIMEDEAN_RATIO_WINDOW_NONEMPTY_IFF_N_IN_PRODUCT_WINDOW=true',
    'ARCHIMEDEAN_WINDOW_ALONE_FIXED_POWER_SAVING=false',
    'PRIMITIVE_RATIO_WINDOW_MULTIPLICATIVE_WIDTH=Bo1',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'NEXT=Stage14-s7-93',
]:
    assert needle in t['s92'], needle


def sqf(n: int) -> int:
    out = 1
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p += 1
    if n > 1:
        out *= n
    return out

# s7-90 exact bijection and root formulas on deterministic samples.
samples = [
    (1, 6, 10),
    (5, 12, 18),
    (7, 15, 25),
    (30, 14, 21),
    (33, 20, 28),
]
alpha, beta = 3, 5
for J1,a1,b1 in samples:
    assert sqf(J1) == J1  # chosen squarefree samples
    g = gcd(a1,b1)
    u, v = a1//g, b1//g
    assert gcd(u,v) == 1
    E = J1*g*g
    n = J1*a1*b1
    assert n == E*u*v
    assert sqf(E) == J1
    assert alpha*J1*a1*a1 == alpha*E*u*u
    assert beta*J1*b1*b1 == beta*E*v*v
    # inverse reconstruction
    gg = isqrt(E//sqf(E))
    assert gg*gg == E//sqf(E)
    assert (sqf(E), gg*u, gg*v) == (J1,a1,b1)

# s7-91 elimination: L/n = u/v and reciprocal roots.
for J1,a1,b1 in samples:
    g = gcd(a1,b1)
    u,v = a1//g,b1//g
    E = J1*g*g
    n = E*u*v
    L = E*u*u
    assert Fraction(L,n) == Fraction(u,v)
    assert alpha*L == Fraction(alpha*n*u, v)
    assert beta*n*n//L == Fraction(beta*n*v, u)

# s7-92 interval geometry: intersection iff product window condition.
def intersects(a,b,c,d):
    # closed intervals [a,b] and [c,d], Fraction endpoints
    return max(a,c) <= min(b,d)

# X/Y windows and fixed coefficients. Check a broad set of exact integer n.
Xm, Xp = 100, 200
Ym, Yp = 300, 600
alpha, beta = 2, 3
for n in range(1, 300):
    RX = (Fraction(Xm,alpha*n), Fraction(Xp,alpha*n))
    RY = (Fraction(beta*n,Yp), Fraction(beta*n,Ym))
    lhs = intersects(RX[0],RX[1],RY[0],RY[1])
    rhs = (Xm*Ym <= alpha*beta*n*n <= Xp*Yp)
    assert lhs == rhs, (n,RX,RY,lhs,rhs)
    if lhs:
        lo=max(RX[0],RY[0]); hi=min(RX[1],RY[1])
        # Intersection multiplicative width cannot exceed either parent width.
        assert hi/lo <= Fraction(Xp,Xm)
        assert hi/lo <= Fraction(Yp,Ym)

print('STAGE14_S_BATCH_AUDIT=PASS')
print('S7_90_92_PRIMITIVE_RATIO_WINDOW_AUDIT=PASS')
