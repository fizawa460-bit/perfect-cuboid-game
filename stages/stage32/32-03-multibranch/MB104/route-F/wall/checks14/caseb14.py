"""checks14 / caseb14.py -- request 14, Theorem 14-A, case B (equal elliptic double covers), the two bidegrees the
hand argument leaves: (4, 5) [type (1,3)] and (5, 5) [type (2,2), birational].  Also run on (4, 4) as a control.

An isogeny-type map p (critical values inside a 4-subset S of B) has D(p, S) = the four simple points over S.
Case B: a Moebius T with T(D(p, S_p)) = D(q, S_q).  For every such T the record
   m1 = |O(p) minus O(q o T)|, m2 = |O(q o T) minus O(p)|, h = label mismatches on the common points
is computed; the problem window is: mixed type (m1, m2 >= 1) with m1 + m2 + h <= 4.
p runs over the isogeny-type maps of the stored list (degree 4: all; degree 5: the 12 representatives), q over all
isogeny-type maps (degree 5: representatives composed with the 24 rotations).  (p, q o T) and (h o p, h o q o T)
have the same record, so this covers all pairs.
Usage: python -I caseb14.py [a,b ...] > caseb14.out     (default: 4,4 4,5 5,5)
"""
import sys, os, json, itertools, collections
HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "..", "f02")); C13 = os.path.join(HERE, "..", "checks13")
sys.path.insert(0, F02); sys.path.insert(0, C13)
import mpmath as mp
import build_maps as bm
import expand5 as E5
import galois13 as G13
mp.mp.dps = 60
KEYS = ["I", "-I", "1", "-1", "0", "oo"]
VAL = {"I": mp.mpc(0, 1), "-I": mp.mpc(0, -1), "1": mp.mpc(1), "-1": mp.mpc(-1), "0": mp.mpc(0)}
CLS = {"I": "a", "-I": "a", "1": "b", "-1": "b", "0": "e", "oo": "e"}
TOL = mp.mpf(10) ** -12
ROTS = E5.rotations()


def fibres(n, P, Q):
    """{value key: (simple points, double points)}; a generic source Moebius is applied first (returned P, Q)"""
    sg = mp.mpf("0.3719")
    P = G13.subst(n, P, mp.mpc(1), mp.mpc(0), mp.mpc(sg), mp.mpc(1)); Q = G13.subst(n, Q, mp.mpc(1), mp.mpc(0), mp.mpc(sg), mp.mpc(1))
    out = {}
    for k in KEYS:
        C = Q if k == "oo" else [p - VAL[k] * q for p, q in zip(P, Q)]
        assert abs(C[-1]) > mp.mpf(10) ** -20 * max(abs(c) for c in C), "point at infinity over B"
        rts = mp.polyroots(list(reversed(C)), maxsteps=500, extraprec=400)
        used = [False] * len(rts); simple = []; double = []
        for i in range(len(rts)):
            if used[i]: continue
            cl = [j for j in range(i, len(rts)) if not used[j] and abs(rts[j] - rts[i]) < mp.mpf(10) ** -8]
            for j in cl: used[j] = True
            assert len(cl) in (1, 2), "not slack 0"
            (simple if len(cl) == 1 else double).append(mp.fsum(rts[j] for j in cl) / len(cl))
        out[k] = (simple, double)
    assert sum(len(out[k][0]) for k in KEYS) == 2 * n + 4
    return out


def mob3(a, b):
    def to01(z0, z1, z2): return (z2 - z1, -z0 * (z2 - z1), z2 - z0, -z1 * (z2 - z0))
    A = to01(*a); B = to01(*b); a1, b1, c1, d1 = B; x, y, z, w = (d1, -b1, -c1, a1); e, f, g, h = A
    return (x * e + y * g, x * f + y * h, z * e + w * g, z * f + w * h)


def ap(M, z):
    a, b, c, d = M; den = c * z + d
    return None if abs(den) < mp.mpf(10) ** -40 * (abs(c * z) + abs(d)) else (a * z + b) / den


def near(u, v): return abs(u - v) < TOL * (1 + abs(u))


class Map:
    def __init__(self, n, P, Q, name):
        self.n = n; self.name = name
        fb = fibres(n, P, Q)
        self.typ = "".join(str(len(fb[k][1])) for k in KEYS)
        self.O = [(z, CLS[k]) for k in KEYS for z in fb[k][0]]
        crit = [k for k in KEYS if fb[k][1]]
        self.D = []                         # one D per admissible S
        for S in itertools.combinations(KEYS, 4):
            if all(k in S for k in crit):
                D = [z for k in S for z in fb[k][0]]
                assert len(D) == 4
                self.D.append((S, D))
        self.iso = len(crit) <= 4


def rot(P, Q, H):
    a, b, c, d = H
    return [a * p + b * q for p, q in zip(P, Q)], [c * p + d * q for p, q in zip(P, Q)]


def load(deg, allrot):
    if deg == 4: data = json.load(open(os.path.join(F02, "maps4.json")))
    else: data = [json.loads(l) for l in open(os.path.join(F02, "maps5reps.state.jsonl"))]
    out = []
    for idx, r in enumerate(data):
        if sum(ch != "0" for ch in r["datum"]) > 4: continue
        P = [bm.parse_c(x) for x in r["P"]]; Q = [bm.parse_c(x) for x in r["Q"]]
        if allrot and deg == 5:
            for k, (perm, H) in enumerate(ROTS):
                P2, Q2 = rot(P, Q, H); out.append(Map(deg, P2, Q2, "%d.r%d" % (idx, k)))
        else: out.append(Map(deg, P, Q, str(idx)))
    return out


def run(a, b):
    Ps = load(a, False); Qs = load(b, True)
    stat = collections.Counter(); window = []; nT = 0
    for p in Ps:
        for q in Qs:
            seen = []
            for (Sp, Dp) in p.D:
                for (Sq, Dq) in q.D:
                    for perm in itertools.permutations(range(4)):
                        T = mob3(Dp[:3], [Dq[perm[k]] for k in range(3)])
                        t = ap(T, Dp[3])
                        if t is None or not near(t, Dq[perm[3]]): continue
                        key = [ap(T, mp.mpc("0.123", "0.456")), ap(T, mp.mpc("-0.7", "0.31"))]
                        if any(near(key[0], s[0]) and near(key[1], s[1]) for s in seen): continue
                        seen.append(key); nT += 1
                        img = [ap(T, z) for z, _ in p.O]
                        common = 0; h = 0
                        for (u, lab) in zip(img, [l for _, l in p.O]):
                            for (v, lab2) in q.O:
                                if u is not None and near(u, v):
                                    common += 1; h += (lab != lab2); break
                        m1 = len(p.O) - common; m2 = len(q.O) - common
                        stat[(m1, m2, h)] += 1
                        if m1 >= 1 and m2 >= 1 and m1 + m2 + h <= 4: window.append((p.name, q.name, m1, m2, h))
    mixed = [k for k in stat if k[0] >= 1 and k[1] >= 1]
    print("bidegree (%d, %d): isogeny-type maps p: %d, q: %d; Moebius maps T with T(D_p) = D_q: %d" % (a, b, len(Ps), len(Qs), nT))
    print("  type (0,0) records:", sum(v for k, v in stat.items() if k[0] == 0 and k[1] == 0),
          "; mixed records:", sum(stat[k] for k in mixed),
          "; smallest |Omega| among mixed:", min((k[0] + k[1] + k[2] for k in mixed), default=None))
    print("  smallest mixed records (m1, m2, h): count:", sorted(((k, stat[k]) for k in mixed), key=lambda t: sum(t[0]))[:6])
    print("  records in the problem window:", len(window), window[:5], flush=True)
    return len(window)


def main():
    bad = 0
    todo = [tuple(int(x) for x in a.split(",")) for a in sys.argv[1:]] or [(4, 4), (4, 5), (5, 5)]
    for a, b in todo: bad += run(a, b)
    print("PASS" if bad == 0 else "WINDOW RECORDS FOUND")


main()
