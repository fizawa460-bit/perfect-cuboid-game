"""E06 / Moebius-type co-image (k = 8): ψ2 = T∘ψ1 with T in PGL2(C).
Branch values of C8 -> R = C8/G = P^1_t (t = d0/c in the F70 model a^2=c^2+d0^2, b^2=c^2-d0^2, e^2=2cd0):
  B_a = {i, -i} (1+t^2=0),  B_b = {1, -1} (1-t^2=0),  B_e = {0, oo} (t).
Same marked G-cover along ψ1 and ψ2 forces q_chi(Tψ1)/q_chi(ψ1) to be a square in K(E) for each chi, hence every
point of Delta(T) = U_chi (B_chi symdiff T^-1 B_chi) has only even local degrees of ψ1, and Riemann-Hurwitz gives
|Delta(T)| <= 4 + 4(g-1)/n  (g = g(E) in {0,1}).  Counting shows |Delta| = 12 - 2j - h with j = label-preserving hits
and h = label-changing hits of B under T; |Delta| <= 4 forces j >= 3 (T fixed by three points) or T(B) = B, so the
candidates are the T sending some 3 points of B to 3 points of B.  Exact arithmetic in Q(i)."""
from fractions import Fraction as F
import itertools, json
class G:   # Gaussian rationals
    __slots__ = ("re", "im")
    def __init__(s, re, im=0): s.re, s.im = F(re), F(im)
    def __add__(s, o): return G(s.re + o.re, s.im + o.im)
    def __sub__(s, o): return G(s.re - o.re, s.im - o.im)
    def __mul__(s, o): return G(s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    def __truediv__(s, o):
        n = o.re*o.re + o.im*o.im; return G((s.re*o.re + s.im*o.im)/n, (s.im*o.re - s.re*o.im)/n)
    def __eq__(s, o): return isinstance(o, G) and s.re == o.re and s.im == o.im
    def __hash__(s): return hash((s.re, s.im))
    def iszero(s): return s.re == 0 and s.im == 0
    def __repr__(s):
        if s.im == 0: return str(s.re)
        return f"({s.re}{'+' if s.im >= 0 else '-'}{abs(s.im)}i)"
INF = "oo"
ZERO, ONE = G(0), G(1)
PTS = {G(0, 1): "a", G(0, -1): "a", G(1): "b", G(-1): "b", G(0): "e", INF: "e"}
B = list(PTS)
def apply(M, z):
    a, b, c, d = M
    if z == INF:
        return INF if c.iszero() else a / c
    num, den = a*z + b, c*z + d
    return INF if den.iszero() else num / den
def cross_map(z):   # Moebius sending (z1,z2,z3) -> (0,1,oo)
    z1, z2, z3 = z
    def coef(p):    # returns (a,b,c,d) of S(x) = ((x-z1)(z2-z3))/((x-z3)(z2-z1)) handling oo
        pass
    if not any(p == INF for p in z):
        return (z2 - z3, (z1*(z2 - z3)) * G(-1), z2 - z1, (z3*(z2 - z1)) * G(-1))
    if z1 == INF: return (ZERO, z2 - z3, ONE, z3 * G(-1))          # (z2-z3)/(x-z3)
    if z2 == INF: return (ONE, z1 * G(-1), ONE, z3 * G(-1))        # (x-z1)/(x-z3)
    return (ONE, z1 * G(-1), ZERO, z2 - z1)                         # (x-z1)/(z2-z1)
def inv(M):
    a, b, c, d = M; return (d, b*G(-1), c*G(-1), a)
def mul(M, N):
    a, b, c, d = M; e, f, g, h = N
    return (a*e + b*g, a*f + b*h, c*e + d*g, c*f + d*h)
def normalize(M):
    piv = next(x for x in M if not x.iszero())
    return tuple(x / piv for x in M)
cands = set()
for src in itertools.permutations(B, 3):
    for dst in itertools.permutations(B, 3):
        T = normalize(mul(inv(cross_map(dst)), cross_map(src)))
        a, b, c, d = T
        if (a*d - b*c).iszero(): continue
        cands.add(T)
def preimage(T, p):          # T^-1(p)
    return apply(inv(T), p)
res = []
for T in sorted(cands, key=repr):
    delta = set()
    for chi in "abe":
        Bc = {p for p in B if PTS[p] == chi}
        Tinv = {preimage(T, p) for p in Bc}
        delta |= (Bc ^ Tinv)
    j = sum(1 for p in B if apply(T, p) in PTS and PTS[apply(T, p)] == PTS[p])
    h = sum(1 for p in B if apply(T, p) in PTS and PTS[apply(T, p)] != PTS[p])
    if len(delta) != 12 - 2*j - h: raise SystemExit("FAIL: counting identity")
    res.append((T, len(delta), j, h, sorted(map(repr, delta))))
from collections import Counter
print("candidate T (sending 3 points of B into B):", len(cands))
print("distribution of |Delta|:", sorted(Counter(r[1] for r in res).items()))
keep = [r for r in res if r[1] <= 4]
print("T with |Delta| <= 4 (allowed for g = 1):", len(keep), "  of which |Delta| <= 3 (allowed for g = 0):", sum(r[1] <= 3 for r in keep))
for T, n, j, h, dl in keep:
    print(f"  |Delta|={n} j={j} h={h}  T={T}  Delta={dl}")
import tempfile, os
json.dump([{"T": [repr(x) for x in T], "delta": n, "j": j, "h": h, "Delta": dl} for T, n, j, h, dl in keep], open(os.path.join(tempfile.gettempdir(), "mobius_allowed.json"), "w"), indent=1)
# --- check Delta ⊂ B and T(Delta) ⊂ B for every allowed T (needed for D1 = D2 = 0) ---
ok = True
for T, n, j, h, dl in keep:
    D = set()
    for chi in "abe":
        Bc = {p for p in B if PTS[p] == chi}
        D |= (Bc ^ {preimage(T, p) for p in Bc})
    inB = all(p in PTS for p in D); TinB = all(apply(T, p) in PTS for p in D)
    if not (inB and TinB): ok = False
    print("  Delta in B:", inB, " T(Delta) in B:", TinB, " label-preserving:", n == 0)
print("k=8: all allowed T have Delta, T(Delta) inside B:", ok)
expected = (len(cands) == 1080 and len(keep) == 16 and sum(r[1] == 0 for r in keep) == 4 and all(r[1] in (0, 4) for r in keep))
print("PASS" if (ok and expected) else "FAIL")
if not (ok and expected): raise SystemExit(1)
