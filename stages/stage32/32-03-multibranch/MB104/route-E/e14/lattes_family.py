# E14 par. 6: explicit families, EXACT over Q(i).
#   L(x) = (x^2 - 1)/(2 i x)   (x-coordinate of the (1+i)-isogeny of y^2 = x^3 - x, up to a unit)
#   L_n = L o ... o L (n times): degree 2^n, slack 0 for B = {0, inf, 1, -1, i, -i}
#   p_{n,c} = L_n(t^2 + c): degree 2^(n+1), slack 1 (for the sample values of c below)
# For p = P/Q of degree d and beta in B:  F = P - beta*Q (F = Q for beta = inf); multiplicity at t = inf is d - deg F.
# All multiplicities are certified <= 2 by gcd(g, g') = 1 for g = gcd(F, F'); odd points = simple points.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gq import *
from fractions import Fraction as Fr
def L_of(Pn, Qn): return psub(pmul(Pn, Pn), pmul(Qn, Qn)), pscale(pmul(Pn, Qn), 2 * I)
def odd_data(Pn, Qn):
    d = max(deg(Pn), deg(Qn)); assert deg(pgcd(Pn, Qn)) == 0
    tot = 0; per = []
    for beta in (G(0), None, G(1), G(-1), I, -I):
        F = Qn if beta is None else psub(Pn, pscale(Qn, beta))
        g = pgcd(F, pder(F)); assert deg(pgcd(g, pder(g))) <= 0          # all finite multiplicities <= 2
        minf = d - deg(F); assert minf <= 2
        o = deg(F) - 2 * deg(g) + (1 if minf == 1 else 0)
        per.append(o); tot += o
    return d, tot, per
def slack(d, tot): return Fr(tot - 2 * d - 4, 2)
ok = True
print("L_n (slack 0 expected):")
Pn, Qn = P(0, 1), P(1)
for n in range(1, 6):
    Pn, Qn = L_of(Pn, Qn)
    d, tot, per = odd_data(Pn, Qn); s = slack(d, tot)
    print("  n = %d: degree %d, |O| = %d, odd points over (0, inf, 1, -1, i, -i) = %s, slack = %s" % (n, d, tot, per, s))
    ok &= (d == 2 ** n and s == 0)
print("p_{n,c} = L_n(t^2 + c) (slack 1 expected; n = 0 is the example t^2 + c of E10 par. 5):")
for c in (G(2), G(Fr(1, 3), Fr(1, 2)), G(-5, 1)):
    Pn, Qn = P(c, 0, 1), P(1)
    for n in range(0, 5):
        if n: Pn, Qn = L_of(Pn, Qn)
        d, tot, per = odd_data(Pn, Qn); s = slack(d, tot)
        print("  c = %s, n = %d: degree %d, |O| = %d, slack = %s" % (c, n, d, tot, s))
        ok &= (d == 2 ** (n + 1) and s == 1)
print("pair (p, -p): -B_chi = B_chi for chi = a, b, e, so O_1 = O_2 with equal labels and Omega is empty (no computation needed);")
print("              the image of (p, -p) is the graph y = -x, of bidegree (1, 1): the pair is not birational onto a (d, d) curve.")
print("PASS" if ok else "FAIL")
