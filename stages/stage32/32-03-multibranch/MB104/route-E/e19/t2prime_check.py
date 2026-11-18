#!/usr/bin/env python3
"""E19 s.21.1: numerical check of Lemma T2' (exact 2-jet constant) on random holomorphic maps of the disc.

For G holomorphic, w = log |G'|_hyp, A_z = the isometry with A_z(z) = G(z) and arg A_z'(z) = arg G'(z), and a geodesic
z(s) (0 <= s <= L) from z0 to z1, Lemma T2' says
    d(G(z1), A_{z0}(z1)) <= int_0^L ( |e^{w(z(s))} - 1| cosh(L - s) + |grad w(z(s))| sinh(L - s) ) ds.
The script prints the largest ratio lhs / rhs over random samples (must be <= 1).
usage: python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e19/t2prime_check.py
"""
import cmath, math, random, sys
sys.dont_write_bytecode = True
def Mb(b, u): return (u + b) / (1 + b.conjugate() * u)
def Mbi(b, u): return (u - b) / (1 - b.conjugate() * u)
def dist(a, b): return 2 * math.atanh(abs(Mbi(a, b)))
def geod(z0, z1, s):
    v = Mbi(z0, z1); return Mb(z0, math.tanh(s / 2) * v / abs(v))
rng = random.Random(20261118); worst = 0.0; n = 0
while n < 300:
    a = complex(rng.uniform(-.3, .3), rng.uniform(-.3, .3)); b = complex(rng.uniform(-.2, .2), rng.uniform(-.2, .2))
    c = rng.uniform(0.6, 1.0) / (1 + 0.3 * abs(a)); rot = cmath.exp(1j * rng.uniform(0, 6.3)); sh = complex(rng.uniform(-.2, .2), rng.uniform(-.2, .2))
    G = lambda u: Mb(sh, rot * c * (u + a * u * u + b * u ** 3))
    dG = lambda u, h=1e-7: (G(u + h) - G(u - h)) / (2 * h)
    A = lambda z, u: Mb(G(z), cmath.exp(1j * cmath.phase(dG(z))) * Mbi(z, u))
    w = lambda u: math.log(abs(dG(u)) * (1 - abs(u) ** 2) / (1 - abs(G(u)) ** 2))
    def gw(u, h=1e-5):
        return math.hypot(w(u + h) - w(u - h), w(u + 1j * h) - w(u - 1j * h)) / (2 * h) * (1 - abs(u) ** 2) / 2
    z0 = complex(rng.uniform(-.3, .3), rng.uniform(-.3, .3)); z1 = complex(rng.uniform(-.55, .55), rng.uniform(-.55, .55))
    if abs(z1) > .7 or abs(G(z1)) > .98 or dist(z0, z1) < 0.05: continue
    L = dist(z0, z1); N = 400; I = 0.0
    for i in range(N):
        s = (i + .5) * L / N; z = geod(z0, z1, s)
        I += (abs(math.exp(w(z)) - 1) * math.cosh(L - s) + gw(z) * math.sinh(L - s)) * L / N
    worst = max(worst, dist(G(z1), A(z0, z1)) / I); n += 1
print("samples: %d   max lhs/rhs = %.4f" % (n, worst))
assert worst <= 1.0
print("PASS")
