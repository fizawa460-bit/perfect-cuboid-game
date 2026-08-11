#!/usr/bin/env python3

# Basic logical boundary checks for Stage14-s7-58.

def balanced_mask_has_divisor(n, lo, hi):
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            e = n // d
            if (lo <= d <= hi and lo <= e <= hi):
                return 1
    return 0

# Nonmultiplicativity witness for balanced factorization.
# 6 and 35 separately have no divisor pair in [5,7], but 210=30*7 and 35*6 etc;
# use windows chosen to give a clean mixed-prime witness.
def B(n):
    for d in range(1, n + 1):
        if n % d == 0 and 10 <= d <= 15 and 14 <= n // d <= 21:
            return 1
    return 0

# Search a small coprime witness automatically.
import math
witness = None
for a in range(2, 80):
    for b in range(2, 80):
        if math.gcd(a,b) != 1:
            continue
        if B(a)==0 and B(b)==0 and B(a*b)==1:
            witness=(a,b,a*b)
            break
    if witness:
        break
assert witness is not None

# Range masks are visibly nonmultiplicative.
def R(n): return int(10 <= n <= 20)
assert R(12)==1 and R(13)==1 and R(12*13)==0

# Exact Walsh orientation bookkeeping: l1 cost is 1.
for r in range(0, 12):
    terms = 2**r
    coeff = 2**(-r)
    assert abs(terms*coeff - 1) < 1e-12

print("Stage14-s7-58 zero-mode mask factorization audit: PASS")
print("balanced-mask nonmultiplicativity witness:", witness)
print("orientation Walsh l1 cost: 1")
print("full physical Hecke factorization: not proved")
