#!/usr/bin/env python3
"""checks20 / decomp15.py -- is an F_p solution pbar = c x A1^2 B1^4 / (A2^2 B2^4) of vfp20 a composite F o G?
Inner G of degree d (target-normalised G(0)=0, G(oo)=oo, G(1)=1, possible because pbar(0), pbar(1), pbar(oo) are distinct),
G = x (x^(d-1) + ...) / (den of degree <= d-1).  Test: pbar is constant on every G-fibre over F_p, i.e. for each y0 in F_p
the cubic G1(x) G2(y0) - G1(y0) G2(x) divides N(x) D(y0) - N(y0) D(x).  Survivors are checked exactly with sympy
(bivariate divisibility).  Usage: python -I decomp15.py n p 'passport-json' d"""
import sys, json, itertools
import numpy as np
from sympy import symbols, Poly, GF, div
x, y = symbols("x y")

def pmul(a, b, p):
    r = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        if u:
            for j, v in enumerate(b): r[i + j] = (r[i + j] + u * v) % p
    return r

def trim(a):
    while len(a) > 1 and a[-1] == 0: a = a[:-1]
    return a

def pmod(a, b, p):
    a = trim(list(a)); b = trim(list(b))
    if len(b) == 1 and b[0] == 0: return None
    ib = pow(b[-1], p - 2, p)
    while len(a) >= len(b) and any(a):
        k = len(a) - len(b); f = a[-1] * ib % p
        for i, v in enumerate(b): a[k + i] = (a[k + i] - f * v) % p
        a = trim(a)
        if len(a) < len(b): break
    return a

def main():
    n, p = int(sys.argv[1]), int(sys.argv[2]); pp = json.loads(sys.argv[3]); d = int(sys.argv[4])
    recs = [json.loads(l) for l in open("vfp20.jsonl") if l.strip()]
    rec = [r for r in recs if r["n"] == n and r["p"] == p and r["passport"] == pp][-1]
    for si, (c, A1, B1, A2, B2) in enumerate(rec["solutions"]):
        N = pmul([0, c], pmul(pmul(A1, A1, p), pmul(pmul(B1, B1, p), pmul(B1, B1, p), p), p), p)
        D = pmul(pmul(A2, A2, p), pmul(pmul(B2, B2, p), pmul(B2, B2, p), p), p)
        Nv = [sum(a * pow(t, i, p) for i, a in enumerate(N)) % p for t in range(p)]
        Dv = [sum(a * pow(t, i, p) for i, a in enumerate(D)) % p for t in range(p)]
        found = []
        # G1 = x * (x^(d-1) + u_{d-2} x^(d-2) + ... + u_0), G2 = e_{d-1} x^(d-1) + ... + e_0 (G2 not identically 0)
        for us in itertools.product(range(p), repeat=d - 1):
            G1 = [0] + list(us) + [1]
            for es in itertools.product(range(p), repeat=d):
                G2 = list(es)
                if not any(G2): continue
                if sum(G1) % p != sum(G2) % p: continue          # G(1) = 1
                if G2[0] == 0: continue                           # G(0) = 0 needs G2(0) != 0 (G1(0) = 0)
                ok = True
                for t in range(p):
                    g1 = sum(a * pow(t, i, p) for i, a in enumerate(G1)) % p
                    g2 = sum(a * pow(t, i, p) for i, a in enumerate(G2)) % p
                    cub = [(a * g2 - b * g1) % p for a, b in itertools.zip_longest(G1, G2, fillvalue=0)]
                    big = [(a * Dv[t] - b * Nv[t]) % p for a, b in itertools.zip_longest(N, D, fillvalue=0)]
                    if not any(trim(cub)) or len(trim(cub)) == 1: continue
                    r = pmod(big, cub, p)
                    if r is None or any(r): ok = False; break
                if ok: found.append((G1, G2))
        exact = []
        dom = GF(p)
        for G1, G2 in found:
            Pg = Poly(sum(a * x**i for i, a in enumerate(G1)) * sum(b * y**i for i, b in enumerate(G2))
                      - sum(a * y**i for i, a in enumerate(G1)) * sum(b * x**i for i, b in enumerate(G2)), x, y, modulus=p)
            Pn = Poly(sum(a * x**i for i, a in enumerate(N)) * sum(b * y**i for i, b in enumerate(D))
                      - sum(a * y**i for i, a in enumerate(N)) * sum(b * x**i for i, b in enumerate(D)), x, y, modulus=p)
            q, r = div(Pn, Pg)
            if r.is_zero: exact.append((G1, G2))
        print(json.dumps({"solution": si, "inner_degree": d, "sieve": len(found), "exact": len(exact), "G": exact[:4]}), flush=True)

if __name__ == "__main__":
    main()
