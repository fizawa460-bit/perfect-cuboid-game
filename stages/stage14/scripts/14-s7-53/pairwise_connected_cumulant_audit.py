#!/usr/bin/env python3
from fractions import Fraction as F

# Exhaustively verify the exact three-Bernoulli cumulant identity on all
# probability masses on {0,1}^3 with denominator 8.
pts = [(a,b,c) for a in (0,1) for b in (0,1) for c in (0,1)]
checks = 0

# weak compositions of 8 into 8 bins

def comps(n,k,prefix=()):
    if k == 1:
        yield prefix + (n,)
        return
    for x in range(n+1):
        yield from comps(n-x,k-1,prefix+(x,))

for mass in comps(8,8):
    if sum(mass) != 8:
        continue
    p = [F(x,8) for x in mass]
    mu = []
    for j in range(3):
        mu.append(sum(p[i]*pts[i][j] for i in range(8)))

    gam = {}
    for i,j in ((0,1),(0,2),(1,2)):
        gam[(i,j)] = sum(
            p[r]*(pts[r][i]-mu[i])*(pts[r][j]-mu[j])
            for r in range(8)
        )

    kap = sum(
        p[r]*(pts[r][0]-mu[0])*(pts[r][1]-mu[1])*(pts[r][2]-mu[2])
        for r in range(8)
    )
    lhs = sum(p[r]*pts[r][0]*pts[r][1]*pts[r][2] for r in range(8))
    rhs = (
        mu[0]*mu[1]*mu[2]
        + mu[2]*gam[(0,1)]
        + mu[1]*gam[(0,2)]
        + mu[0]*gam[(1,2)]
        + kap
    )
    assert lhs == rhs
    checks += 1

# exponent ledger: if all pairwise covariance terms are B^-delta relative to
# a B^1/2 charged-once majorant, their aggregate is B^(1/2-delta+o(1)).
for dnum in range(1,9):
    delta = F(dnum,64)
    pair_exp = F(1,2)-delta
    assert pair_exp < F(1,2)

print('Stage14-s7-53 pairwise/connected cumulant audit: PASS')
print('Bernoulli distributions checked:', checks)
print('exact identity: principal + 3 pairwise covariances + connected third cumulant')
print('pairwise power-small branch leaves connected cumulant as only signed three-way obstruction')
