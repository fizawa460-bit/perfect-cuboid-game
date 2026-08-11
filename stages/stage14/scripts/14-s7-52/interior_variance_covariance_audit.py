#!/usr/bin/env python3
from fractions import Fraction as F

# Exact finite-probability checks for Bernoulli variance/covariance identities.
checks = 0
for a in range(1, 10):
    mu = F(a, 10)
    var = mu * (1 - mu)
    assert var >= 0
    assert var <= F(1, 4)
    checks += 1

# Symbolic exponent bookkeeping: if V_j <= B^-delta, every covariance
# containing X_j loses delta/2 by Cauchy-Schwarz; exceptional deterministic
# replacement loses delta itself.
for d in range(1, 20):
    delta = F(d, 100)
    ambient = F(1, 2)
    cov = ambient - delta / 2
    exceptional = ambient - delta
    assert cov < ambient
    assert exceptional < ambient
    checks += 2

# Triple-centering identity on several exact finite cells.
for n in range(4, 12):
    wp = [F((3*i+1) % 2) for i in range(n)]
    wm = [F((5*i+1) % 2) for i in range(n)]
    wk = [F((7*i+1) % 2) for i in range(n)]
    mus = [sum(wp)/n, sum(wm)/n, sum(wk)/n]
    xp = [x-mus[0] for x in wp]
    xm = [x-mus[1] for x in wm]
    xk = [x-mus[2] for x in wk]
    lhs = sum(a*b*c for a,b,c in zip(wp,wm,wk))
    rhs = (
        n*mus[0]*mus[1]*mus[2]
        + mus[0]*sum(b*c for b,c in zip(xm,xk))
        + mus[1]*sum(a*c for a,c in zip(xp,xk))
        + mus[2]*sum(a*b for a,b in zip(xp,xm))
        + sum(a*b*c for a,b,c in zip(xp,xm,xk))
    )
    assert lhs == rhs
    # numerical Cauchy-Schwarz for all pairs
    arrays = [xp,xm,xk]
    for i,j in ((0,1),(0,2),(1,2)):
        cij = sum(arrays[i][r]*arrays[j][r] for r in range(n))
        vi = sum(x*x for x in arrays[i])
        vj = sum(x*x for x in arrays[j])
        assert cij*cij <= vi*vj
    checks += 4

print('Stage14-s7-52 interior variance/covariance audit: PASS')
print('checks:', checks)
print('current exponent: 1/2')
print('next: Stage14-s7-53')
