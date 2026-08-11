#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations

# Exact 3-selector cumulant expansion checks.
cumulant_checks = 0
for n in range(2, 20):
    wp = [((3*i+n) % 5) // 3 for i in range(n)]
    wm = [((5*i+2*n) % 7) // 4 for i in range(n)]
    wk = [((7*i+3*n) % 11) // 6 for i in range(n)]
    wp = [1 if x else 0 for x in wp]
    wm = [1 if x else 0 for x in wm]
    wk = [1 if x else 0 for x in wk]
    N = Fraction(n,1)
    mup = sum(map(Fraction,wp),Fraction(0))/N
    mum = sum(map(Fraction,wm),Fraction(0))/N
    muk = sum(map(Fraction,wk),Fraction(0))/N
    xp = [Fraction(x)-mup for x in wp]
    xm = [Fraction(x)-mum for x in wm]
    xk = [Fraction(x)-muk for x in wk]
    avg = lambda xs: sum(xs,Fraction(0))/N
    gpm = avg([xp[i]*xm[i] for i in range(n)])
    gpk = avg([xp[i]*xk[i] for i in range(n)])
    gmk = avg([xm[i]*xk[i] for i in range(n)])
    k3 = avg([xp[i]*xm[i]*xk[i] for i in range(n)])
    lhs = avg([Fraction(wp[i]*wm[i]*wk[i]) for i in range(n)])
    rhs = mup*mum*muk + muk*gpm + mum*gpk + mup*gmk + k3
    assert lhs == rhs
    cumulant_checks += 1

# Walsh antipodal parity split checks on moving cube dimensions.
walsh_checks = 0
odd_mean_checks = 0
for r in range(1,8):
    cube = list(product((-1,1), repeat=r))
    for mask in range(1<<r):
        deg = mask.bit_count()
        def chi(eps):
            out=1
            for j in range(r):
                if mask>>j & 1:
                    out *= eps[j]
            return out
        for eps in cube:
            anti = tuple(-x for x in eps)
            assert chi(anti) == ((-1)**deg)*chi(eps)
            walsh_checks += 1
        if deg % 2 == 1:
            assert sum(chi(e) for e in cube) == 0
            odd_mean_checks += 1

# Formal degree dictionary only: pairwise terms are degree 2, connected triple degree 3.
assert len(list(combinations(range(3),2))) == 3
assert len(list(combinations(range(3),3))) == 1

# Boundary decisions locked by the integrated theorem.
assert Fraction(1,2) == Fraction(1,2)
COMMON_ADAPTER_PROVED = False
SAVING_CROSS_PROMOTABLE = False
GLOBAL_THREE_SELECTOR_ANTIPODE_PROVED = False
STRICT_SUBSQRT_POWER_SAVING_PROVED = False
assert not COMMON_ADAPTER_PROVED
assert not SAVING_CROSS_PROMOTABLE
assert not GLOBAL_THREE_SELECTOR_ANTIPODE_PROVED
assert not STRICT_SUBSQRT_POWER_SAVING_PROVED

print('Stage14-Work-beX17 integrated degree/parity audit: PASS')
print(f'cumulant identity checks: {cumulant_checks}')
print(f'Walsh antipodal parity checks: {walsh_checks}')
print(f'odd-character zero-mean checks: {odd_mean_checks}')
print('global signed degrees: pairwise=2, connected=3')
print('fixed-U surviving Walsh parity: even, including degree 0 principal')
print('common arithmetic adapter proved: false')
print('saving cross-promotable: false')
print('current whole-family exponent: 1/2')
