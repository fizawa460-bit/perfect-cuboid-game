"""Shape of the low-omega birational (4,4) configurations found by f02_spectrum.py (file low4x4.json).

Step 1 (exact). Every record (omega <= cut) is rebuilt in mpmath (dps 50) and its coincidences are counted exactly
  (coincident: cross < 1e-30; separation: every other pair > 1e-12, or the run fails). Birationality of the exact
  configurations is recomputed.
Step 2 (shape), for the birational records at the exact minimum omega:
  - branch data of p1 and q (from maps4.json);
  - Aut(p) = Moebius S with p o S = p, for p1 and q. For degree 4, p = r o u with deg r = deg u = 2 iff Aut(p)
    contains an involution;
  - left factors: for every involution s in Aut(p), the critical values of r (= p at the two fixed points of s).
    "shared left factor" = p1 and q have a degree-2 left factor with the same pair of critical values;
  - symmetry orbit: is q = g o p1 o S for some g in G (24 Moebius maps of B, with conjugation) and Moebius S?
  - labels (a, b, e) of the coincident points.
(a = b = 4 only: the map information is computed from the list of p1 maps, which is also the list of q maps.)
usage: python -I -O analyze_extremal.py 4 4 [omega]   (default: the minimum; output extremal{a}x{b}[_om{omega}].json)
"""
import itertools, json, os, sys
from collections import Counter
from multiprocessing import Pool
import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import f02_spectrum as F2
import recheck_amb as RA
F1 = F2.F1
mp.mp.dps = 50
EPS = mp.mpf(10) ** -30
BPTS = [mp.mpc(0, 1), mp.mpc(0, -1), mp.mpc(1), mp.mpc(-1), mp.mpc(0), mp.inf]
BNAME = ["I", "-I", "1", "-1", "0", "oo"]


def peval(P, Q, z):
    n = len(P) - 1
    if z == mp.inf: num, den = P[n], Q[n]
    else: num, den = mp.polyval(list(reversed(P)), z), mp.polyval(list(reversed(Q)), z)
    return mp.inf if abs(den) < mp.mpf(10) ** -35 * (abs(num) + abs(den)) else num / den


def mob(M, z):
    a, b, c, d = M
    if z == mp.inf: return mp.inf if abs(c) < mp.mpf(10) ** -35 else a / c
    den = c * z + d
    return mp.inf if abs(den) < mp.mpf(10) ** -35 else (a * z + b) / den


def same_pt(z, w, tol=mp.mpf(10) ** -20):
    if z == mp.inf or w == mp.inf:
        if z == mp.inf and w == mp.inf: return True
        x = w if z == mp.inf else z
        return abs(x) > 1 / tol
    return abs(z - w) < tol * (1 + abs(z) + abs(w))


def crit(P, Q):
    n = len(P) - 1
    dP = [k * P[k] for k in range(1, n + 1)]; dQ = [k * Q[k] for k in range(1, n + 1)]
    W = [mp.mpc(0)] * (2 * n)
    for i, a in enumerate(dP):
        for k, b in enumerate(Q): W[i + k] += a * b
    for i, a in enumerate(P):
        for k, b in enumerate(dQ): W[i + k] -= a * b
    nrm = max(abs(t) for t in W)
    deg = max(k for k in range(2 * n) if abs(W[k]) > mp.mpf(10) ** -30 * nrm)
    rts = list(mp.polyroots(list(reversed(W[:deg + 1])), maxsteps=400, extraprec=400)) if deg > 0 else []
    return rts + [mp.inf] * (2 * n - 2 - deg)


def mob3(src, dst):
    """Moebius map sending src[i] -> dst[i] (points of the sphere, mp.inf allowed), as (a,b,c,d)"""
    def to01inf(z1, z2, z3):      # map z1,z2,z3 -> 0, 1, oo
        if z1 == mp.inf: return (0, z2 - z3, 1, -z3)
        if z2 == mp.inf: return (1, -z1, 1, -z3)
        if z3 == mp.inf: return (1, -z1, 0, z2 - z1)
        return (z2 - z3, -z1 * (z2 - z3), z2 - z1, -z3 * (z2 - z1))
    A = to01inf(*src); B = to01inf(*dst)
    a, b, c, d = B; Binv = (d, -b, -c, a)
    a1, b1, c1, d1 = Binv; a2, b2, c2, d2 = A
    return (a1 * a2 + b1 * c2, a1 * b2 + b1 * d2, c1 * a2 + d1 * c2, c1 * b2 + d1 * d2)


TESTS = [mp.mpc(0.31, 0.77), mp.mpc(-1.13, 0.29), mp.mpc(0.6, -1.4), mp.mpc(2.2, 0.15)]


def aut(P, Q):
    """all Moebius S with p o S = p (S permutes the critical points, preserving values)"""
    cps = crit(P, Q); vals = [peval(P, Q, c) for c in cps]
    out = []
    i0, i1, i2 = 0, 1, 2
    for tri in itertools.permutations(range(len(cps)), 3):
        if not all(same_pt(vals[x], vals[y], mp.mpf(10) ** -15) for x, y in zip((i0, i1, i2), tri)): continue
        S = mob3([cps[i0], cps[i1], cps[i2]], [cps[t] for t in tri])
        if all(same_pt(peval(P, Q, mob(S, z)), peval(P, Q, z), mp.mpf(10) ** -15) for z in TESTS):
            if not any(all(abs(S[k] * T[m] - S[m] * T[k]) < mp.mpf(10) ** -15 * (1 + max(abs(x) for x in S + T)) ** 2
                           for k in range(4) for m in range(4)) for T in out):
                out.append(S)
    return out, cps, vals


def is_involution(S):
    a, b, c, d = S
    return abs(a + d) < mp.mpf(10) ** -15 * (abs(a) + abs(b) + abs(c) + abs(d))     # trace 0 (identity has trace 2a)


def fixed_points(S):
    a, b, c, d = S
    if abs(c) < mp.mpf(10) ** -30: return [mp.inf, b / (d - a)] if abs(d - a) > 1e-30 else [mp.inf]
    disc = mp.sqrt((a - d) ** 2 + 4 * b * c)
    return [((a - d) + disc) / (2 * c), ((a - d) - disc) / (2 * c)]


def left_factors(P, Q, A):
    """critical-value pairs of the degree-2 left factors r (p = r o u, u = quotient by an involution in Aut)"""
    res = []
    for S in A:
        if not is_involution(S): continue
        fp = fixed_points(S)
        res.append(tuple(sorted([complex(peval(P, Q, z)) if peval(P, Q, z) != mp.inf else complex(1e300) for z in fp],
                                key=lambda w: (round(w.real, 8), round(w.imag, 8)))))
    return res


_A = {}


def init(a, b):
    RA._rinit(a, b)
    _A.update(RA._R)
    data = json.load(open(os.path.join(HERE, "maps4.json")))
    _A["datum"] = [d["datum"] for d in data]


def exact(rec):
    ia, ib, s, t, om, j, h, bd = rec
    O1, Oq = _A["A_mp"][ia], _A["B_mp"][ib]
    X1 = [p for p, _ in O1]; Xq = [p for p, _ in Oq]
    T = RA.frame(*[Xq[k] for k in t[:3]]) * mp.inverse(RA.frame(*[X1[k] for k in s[:3]]))
    Ti = mp.inverse(T)
    V = []
    for y, ly in Oq:
        v = Ti * mp.matrix([y[0], y[1]]); nv = mp.sqrt(abs(v[0]) ** 2 + abs(v[1]) ** 2); V.append((v[0] / nv, v[1] / nv, ly))
    co = []; minfar = mp.mpf(1)
    for i1, (x, lx) in enumerate(O1):
        for i2, (v0, v1, ly) in enumerate(V):
            c = abs(x[0] * v1 - x[1] * v0)
            if c < EPS: co.append((i1, i2, lx, ly))
            elif c < minfar: minfar = c
    jj = sum(1 for c in co if c[2] == c[3]); hh = len(co) - jj
    om2 = len(O1) + len(Oq) - 2 * jj - hh
    Tn = np.array([[complex(T[0, 0]), complex(T[0, 1])], [complex(T[1, 0]), complex(T[1, 1])]])
    bd2 = F2.bir_degree(_A["a"], *_A["A_maps"][ia], *_A["B_maps"][ib], Tn / np.linalg.norm(Tn)) if om2 <= _A["cut"] else None
    return dict(ia=ia, ib=ib, exact=[om2, jj, hh], bir=bd2, float=[om, j, h, bd], minfar=float(minfar), co=co)


def mapinfo(i):
    P, Q = _A["A_maps"][i]
    A, cps, vals = aut(P, Q)
    return i, dict(aut=len(A), lf=left_factors(P, Q, A))


def main(a, b):
    low = json.load(open(os.path.join(HERE, f"low{a}x{b}.json")))
    with Pool(11, initializer=init, initargs=(a, b)) as pool:
        ex = pool.map(exact, low, chunksize=200)
        minfar = min(e["minfar"] for e in ex)
        bir = [e for e in ex if e["bir"] == 1]
        om_min = min(e["exact"][0] for e in bir)
        target = int(sys.argv[3]) if len(sys.argv) > 3 else om_min      # optional: classify another omega level
        top = [e for e in bir if e["exact"][0] == target]
        need = sorted({e["ia"] for e in top} | {e["ib"] for e in top})
        info = dict(pool.map(mapinfo, need))
    datum = json.load(open(os.path.join(HERE, "maps4.json")))
    datum = [d["datum"] for d in datum]
    changed = sum(1 for e in ex if e["exact"][:3] != e["float"][:3] or (e["bir"] == 1) != (e["float"][3] == 1))
    hist_b = Counter(e["exact"][0] for e in bir)
    hist_n = Counter(e["exact"][0] for e in ex if e["bir"] is not None and e["bir"] != 1)

    def shared(e):
        A1 = {tuple((round(w.real, 8), round(w.imag, 8)) for w in x) for x in info[e["ia"]]["lf"]}
        A2 = {tuple((round(w.real, 8), round(w.imag, 8)) for w in x) for x in info[e["ib"]]["lf"]}
        return bool(A1 & A2)
    res = dict(
        records=len(ex), changed_by_exact=changed, min_noncoincident_cross=minfar,
        birational_by_exact_omega=dict(sorted(hist_b.items())), nonbirational_by_exact_omega=dict(sorted(hist_n.items())),
        omega_min=om_min, extremal=len(top),
        extremal_jh=sorted(Counter(tuple(e["exact"][1:]) for e in top).items()),
        distinct_pairs=len({(e["ia"], e["ib"]) for e in top}),
        T_per_pair=sorted(Counter(Counter((e["ia"], e["ib"]) for e in top).values()).items()),
        datum_pairs=sorted(Counter(tuple(sorted((datum[e["ia"]], datum[e["ib"]]))) for e in top).items(), key=lambda x: -x[1]),
        aut_pairs=sorted(Counter(tuple(sorted((info[e["ia"]]["aut"], info[e["ib"]]["aut"]))) for e in top).items()),
        p1_decomposable=sum(1 for e in top if info[e["ia"]]["lf"]), q_decomposable=sum(1 for e in top if info[e["ib"]]["lf"]),
        shared_left_factor=sum(1 for e in top if shared(e)),
        same_map=sum(1 for e in top if e["ia"] == e["ib"]),
        coincidence_labels=sorted(Counter(tuple(sorted(Counter(c[2] for c in e["co"]).items())) for e in top).items()),
    )
    suffix = "" if len(sys.argv) <= 3 else f"_om{sys.argv[3]}"
    json.dump(top, open(os.path.join(HERE, f"extremal{a}x{b}{suffix}.json"), "w"), default=str)
    print(json.dumps(res, default=str))
    ok = minfar > 1e-12
    print("PASS" if ok else "FAIL: separation")


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
