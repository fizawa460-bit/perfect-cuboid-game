# E16 Lemma S (singularity budget), checked on explicit pairs.  EXACT arithmetic in Q(i)[t] (e14/gq.py).
# For a birational pair Phi = (p1, p2) : P^1 -> P^1 x P^1 of degrees (a, b) the image has arithmetic genus
# (a-1)(b-1) and geometric genus 0, so   sum_P delta_P = (a-1)(b-1),   delta_P >= m_P (m_P - 1)/2,
# m_P = sum over v with Phi(v) = P of min(e_v(p1), e_v(p2))  (multiplicity of the image at P).
# The script computes m_P at the 36 points of B x B (12 of them label-matched) and checks
#   (S)  sum_P C(m_P, 2) <= (a-1)(b-1)          for birational pairs,
#   (K)  M := sum over matched P of m_P <= min(2(a+b), 6a, 6b)   (E15 Lemma K and the fibre bound).
# Birationality is certified exactly: the fibre of Phi through one rational point is a single point.
# Control: the non-birational pair (f, -f) must be detected, and violates (S).
# All maps used have multiplicities <= 2 over B (asserted).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "e14"))
from gq import G, I, P, padd, psub, pmul, pscale, pder, pgcd, pdivmod, peval, deg
from fractions import Fraction as Fr
BPTS = [(G(0), "e"), (None, "e"), (G(1), "b"), (G(-1), "b"), (I, "a"), (-I, "a")]     # None = infinity
def ppow(p, k):
    r = P(1)
    for _ in range(k): r = pmul(r, p)
    return r
def compose(A, B, Pn, Qn):
    d = max(deg(A), deg(B))
    def hom(F):
        r = []
        for k, c in enumerate(F): r = padd(r, pscale(pmul(ppow(Pn, k), ppow(Qn, d - k)), c))
        return r
    N, D = hom(A), hom(B); assert deg(pgcd(N, D)) == 0
    return N, D
def level(Pn, Qn, beta):
    """F = polynomial of the fibre over beta; D1 = its distinct roots, D2 = its double roots; e_inf = order at infinity."""
    d = max(deg(Pn), deg(Qn))
    F = Qn if beta is None else psub(Pn, pscale(Qn, beta))
    D2 = pgcd(F, pder(F)) if deg(F) > 0 else P(1)
    assert deg(pgcd(D2, pder(D2))) <= 0 if deg(D2) > 0 else True
    D1 = pdivmod(F, D2)[0]
    einf = d - deg(F); assert einf <= 2
    return F, D1, D2, einf
def gdeg(p, q):
    if deg(p) <= 0 or deg(q) <= 0: return 0
    return deg(pgcd(p, q))
def value(Pn, Qn, u):
    q = peval(Qn, u)
    return None if q.iszero() else peval(Pn, u) / q
def birational(P1, Q1, P2, Q2):
    for u in (G(2), G(3), G(Fr(1, 2), 1)):
        v1, v2 = value(P1, Q1, u), value(P2, Q2, u)
        if v1 is None or v2 is None: continue
        F1 = psub(P1, pscale(Q1, v1)); F2 = psub(P2, pscale(Q2, v2))
        inf1 = max(deg(P1), deg(Q1)) - deg(F1) > 0; inf2 = max(deg(P2), deg(Q2)) - deg(F2) > 0
        if deg(pgcd(F1, F2)) == 1 and not (inf1 and inf2): return True
    return False
def run(name, P1, Q1, P2, Q2, expect_birational):
    a = max(deg(P1), deg(Q1)); b = max(deg(P2), deg(Q2))
    bir = birational(P1, Q1, P2, Q2)
    L1 = [level(P1, Q1, be) for be, _ in BPTS]; L2 = [level(P2, Q2, be) for be, _ in BPTS]
    S_all = S_m = M = 0; mm = []
    for i, (_, l1) in enumerate(BPTS):
        for k, (_, l2) in enumerate(BPTS):
            m = gdeg(L1[i][1], L2[k][1]) + gdeg(L1[i][2], L2[k][2]) + min(L1[i][3], L2[k][3])
            S_all += m * (m - 1) // 2
            if l1 == l2: M += m; S_m += m * (m - 1) // 2; mm.append(m)
    budget = (a - 1) * (b - 1)
    print("%-26s (a, b) = (%2d, %2d)  birational: %-5s  M = %3d  m_P at matched points = %s" % (name, a, b, bir, M, mm))
    print("%-26s   sum C(m_P, 2): matched %d, all of B x B %d;  (a-1)(b-1) = %d;  bound from M alone: %s"
          % ("", S_m, S_all, budget, Fr(M * (M - 12), 24)))
    if expect_birational:
        return bir and S_all <= budget and M <= min(2 * (a + b), 6 * a, 6 * b) and Fr(M * (M - 12), 24) <= S_m
    return (not bir) and S_all > budget
al = G(-1, 2); alb = G(-1, -2)
def lattes5(al):
    return pmul(P(0, 1), pmul(P(al, 0, 1), P(al, 0, 1))), pmul(P(1, 0, al), P(1, 0, al))
fA, fB = lattes5(al); gA, gB = lattes5(alb)
LA = P(-1, 0, 1); LB = P(0, 2 * I)
def Ln(n, inner=(P(0, 1), P(1))):
    Pn, Qn = inner
    for _ in range(n): Pn, Qn = compose(LA, LB, Pn, Qn)
    return Pn, Qn
ix = (P(0, I), P(1))
ok = True
print("birational pairs (Lemma S must hold):")
ok &= run("(x, i x)", P(0, 1), P(1), P(0, I), P(1), True)
ok &= run("(f, conj f)", fA, fB, gA, gB, True)
ok &= run("(L_2, f)", *Ln(2), fA, fB, True)
ok &= run("(L_2(x), L_2(ix))", *Ln(2), *Ln(2, ix), True)
ok &= run("(L_3(x), L_3(ix))", *Ln(3), *Ln(3, ix), True)
ok &= run("(L_4(x), L_4(ix))", *Ln(4), *Ln(4, ix), True)
f2 = compose(fA, fB, fA, fB); g2 = compose(gA, gB, gA, gB)
ok &= run("(f o f, conj(f o f))", *f2, *g2, True)
print("control, not birational (image y = -x; must be detected and violates (S)):")
ok &= run("(f, -f)", fA, fB, pscale(fA, -1), fB, False)
ok &= run("(f o f, -f o f)", *f2, pscale(f2[0], -1), f2[1], False)
print("PASS" if ok else "FAIL")
