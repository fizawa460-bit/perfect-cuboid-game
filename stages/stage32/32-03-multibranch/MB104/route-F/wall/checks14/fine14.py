"""checks14 / fine14.py -- request 14: a finer invariant for the degree-4 slack-0 maps of type {0,0,1,1,2,2}
(critical values in four points of B; two maps per type).  CHECK-13's invariants I1, I2 take the same value on
both maps of such a type, so they cannot tell whether the two maps are Galois-conjugate.
Invariant used here (c_o, c_o' = the critical points over the two 'ones' values, t in T1, t' in T2 = the critical points
over the first / second 'twos' value):   J = sum of v + 3 v^2 + 7 v^3 over the four v = cr(c_o, c_o', t, t').
Prediction (ANSWER-14, Lemma 2): the two maps have J in Q(i) iff the cross-ratio (o, o'; t, t') of the VALUES is a
square in Q(i), i.e. iff it equals -1 (ones antipodal, twos antipodal).  Otherwise the two J are conjugate over a
quadratic extension of Q(i).
Usage: python -I fine14.py > fine14.out
"""
import sys, os, json, itertools, collections
HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "..", "f02")); C13 = os.path.join(HERE, "..", "checks13")
sys.path.insert(0, F02); sys.path.insert(0, C13)
import mpmath as mp
import build_maps as bm
import galois13 as G13
mp.mp.dps = 60
KEYS = ["I", "-I", "1", "-1", "0", "oo"]
VAL = {"I": mp.mpc(0, 1), "-I": mp.mpc(0, -1), "1": mp.mpc(1), "-1": mp.mpc(-1), "0": mp.mpc(0), "oo": mp.inf}


def crit(n, P, Q):
    sg = mp.mpf("0.3719")
    P = G13.subst(n, P, mp.mpc(1), mp.mpc(0), mp.mpc(sg), mp.mpc(1)); Q = G13.subst(n, Q, mp.mpc(1), mp.mpc(0), mp.mpc(sg), mp.mpc(1))
    W = [mp.mpc(0)] * (2 * n)
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j - 1 >= 0: W[i + j - 1] += (i - j) * P[i] * Q[j]
    while abs(W[-1]) < mp.mpf(10) ** -25: W.pop()
    assert len(W) - 1 == 2 * n - 2
    cps = mp.polyroots(list(reversed(W)), maxsteps=300, extraprec=300)
    labs = []
    for c in cps:
        q = mp.polyval(list(reversed(Q)), c); pv = mp.polyval(list(reversed(P)), c)
        if abs(q) < mp.mpf(10) ** -15 * (1 + abs(pv)): labs.append("oo"); continue
        v = pv / q
        k = min((k for k in KEYS if k != "oo"), key=lambda k: abs(v - VAL[k]))
        assert abs(v - VAL[k]) < mp.mpf(10) ** -15
        labs.append(k)
    return cps, labs


def cr(a, b, c, d): return (a - c) * (b - d) / ((a - d) * (b - c))


def crv(a, b, c, d):
    def f(x, y): return mp.mpc(1) if (x == mp.inf or y == mp.inf) else x - y
    return f(a, c) * f(b, d) / (f(a, d) * f(b, c))


def ident(z):
    """z in Q(i)?  else in Q(i, sqrt2)?  (PSLQ on real and imaginary parts separately)"""
    def one(x, basis):
        if abs(x) < mp.mpf(10) ** -25: return True
        r = mp.pslq([x] + basis, maxcoeff=10 ** 6, maxsteps=20000, tol=mp.mpf(10) ** -30)
        return r is not None and r[0] != 0
    if one(z.real, [mp.mpf(1)]) and one(z.imag, [mp.mpf(1)]): return "Q(i)"
    if one(z.real, [mp.mpf(1), mp.sqrt(2)]) and one(z.imag, [mp.mpf(1), mp.sqrt(2)]): return "Q(i,sqrt2)"
    return "other"


def main():
    maps = json.load(open(os.path.join(F02, "maps4.json")))
    by = collections.defaultdict(list)
    for idx, r in enumerate(maps):
        if sorted(r["datum"]) == list("001122"): by[r["datum"]].append(idx)
    stat = collections.Counter(); inQi = 0
    for typ in sorted(by):
        ones = [KEYS[k] for k in range(6) if typ[k] == "1"]; twos = [KEYS[k] for k in range(6) if typ[k] == "2"]
        lam = crv(VAL[ones[0]], VAL[ones[1]], VAL[twos[0]], VAL[twos[1]])
        res = []
        for idx in by[typ]:
            r = maps[idx]
            cps, labs = crit(4, [bm.parse_c(x) for x in r["P"]], [bm.parse_c(x) for x in r["Q"]])
            co = [c for c, l in zip(cps, labs) if l == ones[0]][0]; co2 = [c for c, l in zip(cps, labs) if l == ones[1]][0]
            t = [c for c, l in zip(cps, labs) if l == twos[0]]
            t2 = [c for c, l in zip(cps, labs) if l == twos[1]]
            vals = [cr(co, co2, x, y) for x in t for y in t2]
            J = mp.fsum(vals) + 3 * mp.fsum(v * v for v in vals) + 7 * mp.fsum(v ** 3 for v in vals)
            res.append((idx, J, ident(J)))
        kinds = tuple(k for _, _, k in res)
        harmonic = abs(lam + 1) < mp.mpf(10) ** -30
        stat[(harmonic, kinds)] += 1
        if kinds == ("Q(i)", "Q(i)"): inQi += 2
        print(typ, "value cross-ratio", mp.nstr(lam, 6), "| maps", [i for i, _, _ in res], "| J =",
              [mp.nstr(J, 12) for _, J, _ in res], kinds)
        assert len(res) == 2 and abs(res[0][1] - res[1][1]) > mp.mpf(10) ** -20, "J does not separate the two maps"
        assert harmonic == (kinds == ("Q(i)", "Q(i)")), "prediction fails"
    print("types:", len(by), " (harmonic?, fields of the two J) -> count:", dict(stat))
    print("maps of these types with J in Q(i):", inQi, " of", 2 * len(by))
    print("PASS")


main()
