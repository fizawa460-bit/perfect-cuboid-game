# E15 par. 11: the component condition of E10 par. 5 (Stab(Z) contains the diagonal G), tested on non-birational pairs.
# Lemma C1: the condition holds iff there is no pair of characters chi != psi with O_1^chi = O_2^psi, where
#   O_i^chi = points of O_i whose label lies in the support of chi (labels e: {0, inf}, b: {1, -1}, a: {i, -i}).
# For a pair (p, -p) one has O_1 = O_2 with equal labels, so the condition holds iff every label class of O_p is
# non-empty.  EXACT arithmetic in Q(i)[t] (e14/gq.py), no floating point.
#   L   = (x^2 - 1)/(2 i x)                      (E14 par. 6)
#   f   = x (x^2 + al)^2 / (al x^2 + 1)^2,  al = -1 + 2i   (E15 Lemma M)
# Expected: label class b EMPTY for L_n and L_n(t^2 + c)  -> condition FAILS  (q_b(p) is a square);
#           all classes non-empty for f, f o f, f(t^2 + c), f(f(t^2 + c)) -> condition HOLDS, slacks 0, 0, 1, 1.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "e14"))
from gq import G, I, P, padd, psub, pmul, pscale, pder, pgcd, deg
from fractions import Fraction as Fr
def compose(A, B, Pn, Qn):
    """(A/B) o (Pn/Qn) as a reduced pair of polynomials."""
    d = max(deg(A), deg(B))
    def hom(F):
        r = []
        for k, c in enumerate(F):
            term = pscale(pmul(ppow(Pn, k), ppow(Qn, d - k)), c)
            r = padd(r, term)
        return r
    N, D = hom(A), hom(B); g = pgcd(N, D)
    assert deg(g) == 0
    return N, D
def ppow(p, k):
    r = P(1)
    for _ in range(k): r = pmul(r, p)
    return r
def odd_data(Pn, Qn):
    d = max(deg(Pn), deg(Qn)); per = []
    for beta in (G(0), None, G(1), G(-1), I, -I):
        F = Qn if beta is None else psub(Pn, pscale(Qn, beta))
        g = pgcd(F, pder(F)); assert deg(pgcd(g, pder(g))) <= 0          # all finite multiplicities <= 2
        minf = d - deg(F); assert minf <= 2
        per.append(deg(F) - 2 * deg(g) + (1 if minf == 1 else 0))
    return d, per
al = G(-1, 2)
fA = pmul(P(0, 1), pmul(P(al, 0, 1), P(al, 0, 1))); fB = pmul(P(1, 0, al), P(1, 0, al))
LA = P(-1, 0, 1); LB = P(0, 2 * I)
ok = True
def report(name, Pn, Qn, want_slack, want_holds):
    global ok
    d, per = odd_data(Pn, Qn); tot = sum(per); s = Fr(tot - 2 * d - 4, 2)
    cls = {"e": per[0] + per[1], "b": per[2] + per[3], "a": per[4] + per[5]}
    holds = all(v > 0 for v in cls.values())
    print("  %-22s degree %3d, slack %s, label classes e/b/a = %d/%d/%d -> condition for (p, -p): %s"
          % (name, d, s, cls["e"], cls["b"], cls["a"], "HOLDS" if holds else "FAILS"))
    ok &= (s == want_slack and holds == want_holds)
print("Lattes family of E14 par. 6 (expected: class b empty, condition fails):")
Pn, Qn = P(0, 1), P(1)
for n in range(1, 5):
    Pn, Qn = compose(LA, LB, Pn, Qn); report("L_%d" % n, Pn, Qn, 0, False)
c = G(2)
Pn, Qn = P(c, 0, 1), P(1)
for n in range(1, 4):
    Pn, Qn = compose(LA, LB, Pn, Qn); report("L_%d(t^2 + 2)" % n, Pn, Qn, 1, False)
print("Degree-5 map f of Lemma M (expected: all classes non-empty, condition holds):")
P1, Q1 = fA, fB; report("f", P1, Q1, 0, True)
P2, Q2 = compose(fA, fB, P1, Q1); report("f o f", P2, Q2, 0, True)
for c in (G(2), G(Fr(1, 3), Fr(1, 2))):
    K = P(c, 0, 1)
    Pk, Qk = compose(fA, fB, K, P(1)); report("f(t^2 + %s)" % c, Pk, Qk, 1, True)
Pk, Qk = compose(fA, fB, *compose(fA, fB, P(G(2), 0, 1), P(1))); report("f(f(t^2 + 2))", Pk, Qk, 1, True)
print("PASS" if ok else "FAIL")
