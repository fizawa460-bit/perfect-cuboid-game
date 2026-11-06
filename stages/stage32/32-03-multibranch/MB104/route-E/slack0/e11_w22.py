"""E11 search: Problem W with (a, b) = (2, 2), both slacks 0 (k = 8, gamma = 0, |Omega| = 4).
Slack-0 degree-2 maps: q(t) = M(t^2) with critical values y1, y2 in B (15 choices), unique up to source Moebius.
p1 = q_i (fixed representative), p2 = q_j o T.  |Omega| = 4 needs >= 6 common odd points, so T maps some triple of
O_1 into O_{q_j}; since j >= 4, the triple can be taken label-matched.  Enumerate all (i, j, triple of O_1, ordered triple of O_qj), build T, count |Omega|.
Numerical (complex double): coincidence = chordal distance < 1e-8.  The run asserts a gap: every accepted coincidence
is < 1e-11 and every non-coincidence is > 1e-4 (measured: 7.6e-15 vs 1.8e-3).  Fail-closed expected counts below.
usage: python -I e11_w22.py"""
import itertools, cmath
from collections import Counter
INF = complex("inf")
B = {1j: "a", -1j: "a", 1: "b", -1: "b", 0: "e", INF: "e"}
BP = list(B)
TOL = 1e-8

def isinf(z): return z == INF or cmath.isinf(z) or abs(z) > 1e15
def chord(z, w):
    if isinf(z) and isinf(w): return 0.0
    if isinf(z): return 1 / (1 + abs(w) ** 2) ** 0.5
    if isinf(w): return 1 / (1 + abs(z) ** 2) ** 0.5
    return abs(z - w) / ((1 + abs(z) ** 2) * (1 + abs(w) ** 2)) ** 0.5
def same(z, w): return chord(z, w) < TOL
def lab(y):
    for b, l in B.items():
        if same(y, b): return l
    return None

def apply(M, z):
    (a, b), (c, d) = M
    if isinf(z): return INF if abs(c) < 1e-14 else a / c
    den = c * z + d
    return INF if abs(den) < 1e-14 * (abs(c * z) + abs(d) + 1) else (a * z + b) / den
def mat_to01inf(p):
    p0, p1, p2 = p
    # standard cross-ratio map z -> ((z - p0)(p1 - p2)) / ((z - p2)(p1 - p0)), with infinities handled
    if isinf(p0): return [[0, p1 - p2], [1, -p2]]          # (p1 - p2)/(z - p2)
    if isinf(p1): return [[1, -p0], [1, -p2]]              # (z - p0)/(z - p2)
    if isinf(p2): return [[1, -p0], [0, p1 - p0]]          # (z - p0)/(p1 - p0)
    return [[p1 - p2, -p0 * (p1 - p2)], [p1 - p0, -p2 * (p1 - p0)]]
def inv(M):
    (a, b), (c, d) = M
    return [[d, -b], [-c, a]]
def mul(M, N):
    return [[M[0][0] * N[0][0] + M[0][1] * N[1][0], M[0][0] * N[0][1] + M[0][1] * N[1][1]],
            [M[1][0] * N[0][0] + M[1][1] * N[1][0], M[1][0] * N[0][1] + M[1][1] * N[1][1]]]
def moeb(src, dst): return mul(inv(mat_to01inf(dst)), mat_to01inf(src))

def deg2_map(y1, y2):
    """q = M(t^2), M(0) = y1, M(inf) = y2, M(1) = c (c chosen outside B)."""
    c = 0.37 + 0.81j
    M = moeb([0, 1, INF], [y1, c, y2])
    return lambda t: apply(M, INF if isinf(t) else t * t), M

def odd_points(y1, y2):
    """points of O (local degree 1 over B) with labels: preimages of the 4 non-critical branch values."""
    q, M = deg2_map(y1, y2)
    Mi = inv(M); pts = []
    for y in BP:
        if same(y, y1) or same(y, y2): continue
        s = apply(Mi, y)      # t^2 = s
        r = cmath.sqrt(s)
        pts += [(r, B[y]), (-r, B[y])]
    return pts, q

MAPS = [(y1, y2) for y1, y2 in itertools.combinations(BP, 2)]
DATA = [odd_points(*m) for m in MAPS]
SANE = len(MAPS) == 15 and all(len(pts) == 8 and all(lab(q(t)) == l for t, l in pts) for pts, q in DATA)

GAP = [0.0, 1.0]   # [max chordal distance among accepted coincidences, min among non-coincidences]
def omega(O1, O2):
    """|Omega| = #{v : lab1(v) != lab2(v)} over the union of O1 and O2 (points compared numerically)."""
    pts = [(t, l, None) for t, l in O1]
    for t, l in O2:
        for k, (u, l1, l2) in enumerate(pts):
            dd = chord(t, u)
            if dd < TOL: GAP[0] = max(GAP[0], dd)
            else: GAP[1] = min(GAP[1], dd)
            if same(t, u):
                pts[k] = (u, l1, l); break
        else:
            pts.append((t, None, l))
    return sum(1 for _, l1, l2 in pts if l1 != l2), pts

# positive control (a, b) = (1, 1): p1 = id, p2 = T (Moebius); O_1 = O_2-source = B.  Here j >= 2 only, so no label
# pruning.  Expect the Klein group {t, -t, 1/t, -1/t} (|Omega| = 0) and maps like t -> i t (j = 2, h = 4, |Omega| = 4).
OB = [(b, l) for b, l in B.items()]
ctrl = set()
for tri in itertools.combinations(range(6), 3):
    for dst in itertools.permutations(range(6), 3):
        T = moeb([OB[k][0] for k in tri], [OB[d][0] for d in dst]); Ti = inv(T)
        n, _ = omega(OB, [(apply(Ti, t), l) for t, l in OB])
        if n <= 4:
            ctrl.add((n,) + tuple((round(apply(T, z).real, 6), round(apply(T, z).imag, 6)) for z in (0.3 + 0.1j, 0.7 - 0.2j)))
print("control (1,1): Moebius T with |Omega| <= 4:", len(ctrl), " by |Omega|:", dict(Counter(c[0] for c in ctrl)))
CTRL_OK = len(ctrl) == 16 and sorted(Counter(c[0] for c in ctrl).items()) == [(0, 4), (4, 12)]
hits = []; tested = 0; nonbir = {}
for i, (O1, _) in enumerate(DATA):
    for j, (Oq, _) in enumerate(DATA):
        for tri in itertools.combinations(range(8), 3):
            src = [O1[k][0] for k in tri]
            for dst in itertools.permutations(range(8), 3):
                if any(O1[k][1] != Oq[d][1] for k, d in zip(tri, dst)): continue   # triple of label-matched points (j >= 4)
                T = moeb(src, [Oq[k][0] for k in dst])
                Ti = inv(T)
                O2 = [(apply(Ti, t), l) for t, l in Oq]      # O_2 = T^{-1}(O_q) with labels
                tested += 1
                n, pts = omega(O1, O2)
                if n <= 4:
                    # (p1, p2) must be birational onto W: p2 not invariant under the deck involution t -> -t of p1
                    qj = DATA[j][1]
                    key0 = (i, j, tuple(sorted((round(u.real, 6), round(u.imag, 6)) if not isinf(u) else (9e9, 9e9) for u, _, _ in pts)))
                    if all(same(qj(apply(T, z0)), qj(apply(T, -z0))) for z0 in (0.4127 + 0.2291j, -1.37 + 0.61j)):
                        nonbir[key0] = n; continue
                    key = (i, j, tuple(sorted((round(u.real, 6), round(u.imag, 6)) if not isinf(u) else (9e9, 9e9) for u, _, _ in pts)))
                    hits.append((i, j, n, T, key))
uniq = {}
for i, j, n, T, key in hits: uniq.setdefault(key, (i, j, n, T))
print("Moebius maps tested:", tested)
print("birational hits with |Omega| <= 4 (raw, distinct):", len(hits), len(uniq))
print("by (i, j, |Omega|):", Counter((i, j, n) for i, j, n, _ in uniq.values()))
for key, (i, j, n, T) in list(uniq.items())[:20]:
    print("  p1 crit", MAPS[i], " q crit", MAPS[j], " |Omega| =", n)
print("chordal gap: max coincidence distance %.3e, min non-coincidence distance %.3e" % tuple(GAP))
print("non-birational configurations with |Omega| <= 4 (factor through a common degree-2 map; bidegree (1,1)):", len(nonbir))
ok = SANE and CTRL_OK and GAP[0] < 1e-11 and GAP[1] > 1e-4 and tested == 157824 and len(nonbir) == 57 and len(uniq) == 0
print("PASS" if ok else "FAIL")
if not ok: raise SystemExit(1)
