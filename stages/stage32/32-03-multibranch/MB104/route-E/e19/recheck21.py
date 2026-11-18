#!/usr/bin/env python3
"""E19 s.21.5: independent re-computation of the official bound (does not import chain20.py; grid search over t0
instead of golden section; closed forms written out again).  Prints log10 a_max for seedless 121 (official), 73, 169.
usage: python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e19/recheck21.py
"""
import math, sys
sys.dont_write_bytecode = True
l = math.acosh(1 + math.sqrt(2)); c = 1 / (1 + math.pi / l); AV = math.pi * (math.cosh(l / 2) - 1)
e5 = 2 * math.atanh(math.exp(-5.0))
r = math.tanh(0.5); lam = 2 / (1 - r * r); f = lam ** 2 * (math.exp(2 * e5) - 1)
K = (((2 / r) * (e5 + r * r / 4 * f) + r * f) / 2 + e5) / e5
K1 = K - 1 + math.exp(e5); beta = 1 / (1 - math.exp(-10.0)); gam = 2 / (1 - math.exp(-2 * l)); h = 2 * math.sinh(l / 2) / l
kap = lambda t: 1 + math.log(beta * K1 / l) + math.log(math.exp(8 * l / 3) + h * gam * (t + 4 * l / 3) * math.exp(4 * l / 3))
R0 = 10.78 + l
s0 = (R0 - kap(R0)) / 3
assert s0 >= 1
lhs = K1 * 2 * math.atanh(math.exp(-(R0 - s0 - 1))) * math.sinh(s0 + 1) \
    + h * K1 * 2 * beta * gam * math.e * (R0 - s0 + 4 * l / 3) * math.exp(-(R0 - s0)) * math.sinh(s0 + 1)
assert lhs < 0.2, lhs                     # eps0 test at R0 (chain20.py checks all t >= R0)
lNv = lambda R: math.log((math.cosh(R + l / 2) - 1) / (math.cosh(l / 2) - 1)) if R < 300 else R + l / 2 - math.log(2 * (math.cosh(l / 2) - 1))
def lse(u, v): return max(u, v) + math.log1p(math.exp(-abs(u - v)))
def lM(la):
    best = float("inf"); t = R0
    while t < R0 + 3 * la + 100:
        rb = (t - kap(t)) / 3
        if rb >= 1 + l / 2:
            best = min(best, lse(math.log(4) + lNv(t), math.log(2 * math.pi / AV) + la - c * (rb - 1 - l / 2)))
        t += 0.01
    return best
for SL in (121, 73, 169):
    lo, hi = 1.0, 1000.0
    for _ in range(45):
        m = (lo + hi) / 2
        if lse(math.log(11), math.log(216.3 * SL) + lse(math.log(4) + lNv(R0), lM(m))) >= m: lo = m
        else: hi = m
    print("seedless %3d: log10 a_max = %.2f" % (SL, lo / math.log(10)))
print("kappa(R0) = %.3f  K1 = %.4f" % (kap(R0), K1))
