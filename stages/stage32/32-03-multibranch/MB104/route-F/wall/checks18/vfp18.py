#!/usr/bin/env python3
"""checks18 / vfp18.py -- F_p count of the Belyi maps pbar of the V-symmetric slack-0 maps (ANSWER-18, 2.4).

Same normal form as belyiV.py:  c x A1^2 B1^4 - A2^2 B2^4 = c (x - 1) A3^2 B3^4  over F_p, (a_k, b_k) = (deg A_k, deg B_k).
Every dessin whose class is fixed by Frobenius gives exactly one solution in F_p (the three unramified points are
rational, and a map of this shape has no automorphism), so  #solutions = #{classes fixed by Frobenius at p}  =: N_p,
and  #{maps with moduli field in Q(i)} <= N_p  for p = 1 mod 4, p > n (see ANSWER-18, section 3).
Method: loop over c and the fibres over 0 and oo; sieve by "(c x s1^2 - s2^2)/(c (x - 1)) is a square or 0 at every x != 1
and vanishes at x = 1"; then check the survivors exactly (factorisation over F_p with sympy).
Usage: python -I vfp18.py p a1,b1 a2,b2 a3,b3      (put the fibre with the largest a + b last)
"""
import sys, json, itertools, time
import numpy as np
from sympy import Poly, symbols, GF, factor_list

X = symbols("x")


def monic_polys(d, p):
    """all monic polynomials of degree d over F_p as coefficient tuples (high to low)"""
    return [(1,) + t for t in itertools.product(range(p), repeat=d)]


def evals(polys, p):
    xs = np.arange(p, dtype=np.int64)
    out = np.zeros((len(polys), p), dtype=np.int64)
    for k, f in enumerate(polys):
        v = np.zeros(p, dtype=np.int64)
        for a in f: v = (v * xs + a) % p
        out[k] = v
    return out


def shape_ok(f, a, b, p):
    """f (sympy Poly over GF(p)) = A^2 B^4, A, B squarefree, coprime, degrees a, b"""
    da = db = 0
    for g, e in f.factor_list()[1]:
        if e == 2: da += g.degree()
        elif e == 4: db += g.degree()
        else: return False
    return da == a and db == b


def main():
    p = int(sys.argv[1]); pp = [tuple(map(int, s.split(","))) for s in sys.argv[2:5]]
    n = 1 + sum(a + b for a, b in pp); assert p % 4 == 1 and p > n
    (a1, b1), (a2, b2), (a3, b3) = pp
    t0 = time.time()
    sq = np.zeros(p, dtype=bool); sq[(np.arange(p) ** 2) % p] = True          # squares and 0
    def fibre(a, b):
        A = monic_polys(a, p); Bq = monic_polys(b, p)
        EA = evals(A, p); EB = evals(Bq, p)
        lst = [(i, j) for i in range(len(A)) for j in range(len(Bq))]
        S = np.array([(EA[i] ** 2 % p) * (EB[j] ** 4 % p) % p for i, j in lst], dtype=np.int16)
        return A, Bq, lst, S
    A1, B1, L1, S1 = fibre(a1, b1); A2, B2, L2, S2 = fibre(a2, b2)
    xs = np.arange(p, dtype=np.int64)
    T1 = (S1.astype(np.int64) * xs % p).astype(np.int16)                         # x s1^2
    inv = np.array([0] + [pow(int(x), p - 2, p) for x in range(1, p)], dtype=np.int64)
    surv = []
    chunk = max(1, 40_000_000 // (len(L2) * p))
    for c in range(1, p):
        w = (inv[c] * inv[(xs - 1) % p]) % p                                    # 1/(c (x - 1)), 0 at x = 1
        for s in range(0, len(L1), chunk):
            M = (c * T1[s:s + chunk, None, :].astype(np.int32) - S2[None, :, :].astype(np.int32)) % p
            ok = M[:, :, 1] == 0
            if not ok.any(): continue
            Mw = (M * w[None, None, :].astype(np.int32)) % p
            good = sq[Mw]; good[:, :, 1] = True
            ok &= good.all(axis=2)
            for k1, k2 in zip(*np.nonzero(ok)): surv.append((c, s + int(k1), int(k2)))
    count = 0; sols = []
    for c, k1, k2 in surv:
        dom = GF(p)
        PA1 = Poly(list(A1[L1[k1][0]]), X, domain=dom); PB1 = Poly(list(B1[L1[k1][1]]), X, domain=dom)
        PA2 = Poly(list(A2[L2[k2][0]]), X, domain=dom); PB2 = Poly(list(B2[L2[k2][1]]), X, domain=dom)
        N0 = Poly([1, 0], X, domain=dom) * PA1 ** 2 * PB1 ** 4; D = PA2 ** 2 * PB2 ** 4
        if not (shape_ok(PA1 ** 2 * PB1 ** 4, a1, b1, p) and shape_ok(D, a2, b2, p)): continue
        if PA1.eval(0) == 0 or PB1.eval(0) == 0: continue
        if N0.gcd(D).degree() > 0: continue
        R = c * N0 - D
        q, r = divmod(R, Poly([c, -c], X, domain=dom))
        if not r.is_zero or q.degree() != n - 1: continue
        if not shape_ok(q, a3, b3, p): continue
        if q.eval(1) == 0: continue
        count += 1; sols.append((c, A1[L1[k1][0]], B1[L1[k1][1]], A2[L2[k2][0]], B2[L2[k2][1]]))
    rec = {"n": n, "p": p, "passport": pp, "survivors_of_sieve": len(surv), "N_p": count, "seconds": round(time.time() - t0, 1)}
    print(json.dumps(rec), flush=True)
    with open("vfp18.jsonl", "a") as f: f.write(json.dumps(rec) + "\n")


if __name__ == "__main__":
    main()
