"""checks13 / sym13.py -- symmetries of the maps that galois13 flags as 'moduli field inside Q(i)' (both invariants of
degree 1).  For each such map p, list all (h, m): h an octahedral rotation of B, m a source Moebius, h o p = p o m.
h = id, m != id is an automorphism (degree 4: equivalent to p = f o g with deg g = 2, g Galois).
Usage: python -I sym13.py G4.jsonl G5.jsonl
"""
import sys, os, json, itertools, random
HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "..", "f02")); sys.path.insert(0, F02); sys.path.insert(0, HERE)
import mpmath as mp
import build_maps as bm
import expand5 as E5
import galois13 as G13
mp.mp.dps = 50
G13.mp.mp.dps = 50
ROTS = E5.rotations()
PT = E5.PT


def peval(C, z): return mp.polyval(list(reversed(C)), z)


def pval(P, Q, z):
    q = peval(Q, z)
    return mp.inf if abs(q) < mp.mpf(10) ** -30 else peval(P, z) / q


def lab(v):
    if v == mp.inf or abs(v) > mp.mpf(10) ** 20: return "oo"
    return min((k for k in PT if k != "oo"), key=lambda k: abs(v - PT[k]))


def mob3(a, b):
    """Moebius sending a0, a1, a2 -> b0, b1, b2 (all finite)"""
    def to01(z0, z1, z2):   # z -> (z - z0)(z2 - z1)/((z - z1)(z2 - z0))
        return (z2 - z1, -z0 * (z2 - z1), z2 - z0, -z1 * (z2 - z0))
    A = to01(*a); B = to01(*b)
    a1, b1, c1, d1 = B; Bi = (d1, -b1, -c1, a1)
    x, y, z, w = Bi; e, f, g, h = A
    return (x * e + y * g, x * f + y * h, z * e + w * g, z * f + w * h)


def ap(M, z):
    a, b, c, d = M; den = c * z + d
    return mp.inf if abs(den) < mp.mpf(10) ** -30 else (a * z + b) / den


def hval(M, v):
    return E5.apply_mob(M, v)


def syms(n, P, Q):
    sg = mp.mpf("0.3719")
    P = G13.subst(n, P, mp.mpc(1), mp.mpc(0), mp.mpc(sg), mp.mpc(1)); Q = G13.subst(n, Q, mp.mpc(1), mp.mpc(0), mp.mpc(sg), mp.mpc(1))
    W = [mp.mpc(0)] * (2 * n)
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j - 1 >= 0: W[i + j - 1] += (i - j) * P[i] * Q[j]
    while abs(W[-1]) < mp.mpf(10) ** -25: W.pop()
    assert len(W) - 1 == 2 * n - 2, "critical point at infinity"
    cps = mp.polyroots(list(reversed(W)), maxsteps=300, extraprec=200)
    labs = [lab(pval(P, Q, c)) for c in cps]
    rnd = random.Random(1); test = [mp.mpc(rnd.uniform(-1, 1), rnd.uniform(-1, 1)) for _ in range(3)]
    out = []
    for perm, H in ROTS:
        for t in itertools.permutations(range(len(cps)), 3):
            if any(labs[t[k]] != perm[labs[k]] for k in range(3)): continue
            M = mob3(cps[:3], [cps[k] for k in t])
            ok = True
            for z in test:
                u = pval(P, Q, ap(M, z)); v = hval(H, pval(P, Q, z))
                if u == mp.inf or v == mp.inf or abs(u - v) > mp.mpf(10) ** -25 * (1 + abs(v)): ok = False; break
            if ok: out.append(("id" if all(perm[k] == k for k in perm) else "".join(perm[k][:2] for k in E5.BKEYS), t))
    return out


def main():
    g4, g5 = sys.argv[1], sys.argv[2]
    d4 = json.load(open(os.path.join(F02, "maps4.json")))
    d5 = [json.loads(l) for l in open(os.path.join(F02, "maps5reps.state.jsonl"))]
    for n, gf, data in ((4, g4, d4), (5, g5, d5)):
        rows = [json.loads(l) for l in open(gf)]
        cand = [r for r in rows if r["I1_deg"] == 1 and r["I2_deg"] == 1]
        extra = [r for r in rows if n == 5 and r["datum"] == "002222" and r not in cand]
        stat = {"aut": 0, "sym_only": 0, "none": 0}
        for r in cand + extra:
            rec = data[r["idx"]]
            P = [bm.parse_c(x) for x in rec["P"]]; Q = [bm.parse_c(x) for x in rec["Q"]]
            s = syms(n, P, Q)
            naut = sum(1 for h, t in s if h == "id") - 1
            nsym = len(s)
            kind = "aut" if naut > 0 else ("sym_only" if nsym > 1 else "none")
            if r in cand: stat[kind] += 1
            print(n, r["idx"], r["datum"], "cand" if r in cand else "other", "|Aut| =", naut + 1, "|Sym| =", nsym,
                  kind, flush=True)
        print("degree", n, "candidates", len(cand), stat, flush=True)


if __name__ == "__main__":
    main()
