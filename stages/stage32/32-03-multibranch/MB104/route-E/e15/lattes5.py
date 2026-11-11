# E15 Lemma M: the degree-5 Lattes map f(x) = x (x^2 + al)^2 / (al x^2 + 1)^2, al = -1 + 2i
# (x-coordinate of multiplication by an element of norm 5 on y^2 = x^3 - x, up to a unit).
# Exact check in Q(i)[x] that
#   (1) f - 1 = (x - 1) D^2 / C^2 and f + 1 = (x + 1) E^2 / C^2 with D = x^2 + u x + 1, E = x^2 - u x + 1;
#   (2) the 8 critical points (roots of x^2 + al, al x^2 + 1, D, E) are distinct and none lies in B;
#   (3) f(B) is contained in B and f is unramified at the six points of B.
# Hence: f has slack 0, f(B) in B, f unramified at B; for every slack-0 map p the map f o p has slack 0 and
# its odd set contains the odd set of p.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "e14"))
from gq import G, I, P, padd, psub, pmul, pscale, pder, pgcd, peval, deg
al = G(-1, 2)
u = (G(1) - al * al) / 2
x = P(0, 1)
A = P(al, 0, 1)            # x^2 + al
C = P(1, 0, al)            # al x^2 + 1
D = P(1, u, 1); E = P(1, -u, 1)
num = pmul(x, pmul(A, A)); den = pmul(C, C)
ok = True
ok &= psub(num, den) == pmul(P(-1, 1), pmul(D, D))
ok &= padd(num, den) == pmul(P(1, 1), pmul(E, E))
print("(1) factorizations of f - 1 and f + 1:", ok)
crit = pmul(pmul(A, C), pmul(D, E))                       # degree 8 = 2*5 - 2
sq = deg(pgcd(crit, pder(crit))) == 0
Bfin = [G(0), G(1), G(-1), I, -I]
offB = all(not peval(crit, b).iszero() for b in Bfin)     # infinity: deg num = 5 > deg den = 4, simple pole
print("(2) 8 distinct critical points: %s; none in B: %s" % (sq, offB)); ok &= sq and offB and deg(crit) == 8
img = {}
for b in Bfin:
    img[b] = peval(num, b) / peval(den, b)
inB = all(any(v == b for b in Bfin) for v in img.values())
print("(3) f(0), f(1), f(-1), f(i), f(-i) =", [img[b] for b in Bfin], " f(inf) = inf; inside B:", inB)
ok &= inB
print("PASS" if ok else "FAIL")
