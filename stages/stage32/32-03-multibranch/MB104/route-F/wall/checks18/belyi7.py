#!/usr/bin/env python3
"""checks18 / belyi7.py -- the 16 Belyi maps of degree 7 with passport (4 2 1)^3, and their fields (ANSWER-18, 2.4).

pbar = c x^4 (x-b)^2 (x-c1) / ((x-d)^2 (x-e)),  pbar - 1 = c (x-1)^4 (x-g)^2 (x-h) / ((x-d)^2 (x-e)).
The points of ramification 4 over 0, 1, oo are put at 0, 1, oo, so each dessin gives exactly one solution.
Newton from random starts (numpy), polish with mpmath (dps 120), then belyi7.gp factors the degree-16 polynomials of the coordinates.
"""
import sys, json
import numpy as np
import mpmath as mp

rng = np.random.default_rng(18)


def resid(v, P=np):
    c, b, c1, d, e, g, h = v
    x = P.poly1d([1, 0]) if P is np else None
    raise NotImplementedError


def polymul(a, b, zero):
    r = [zero] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] = r[i + j] + x * y
    return r


def F(v, one, zero):
    c, b, c1, d, e, g, h = v
    lin = lambda r: [one, -r]
    def prod(fs):
        r = [one]
        for f in fs: r = polymul(r, f, zero)
        return r
    Pn = prod([lin(zero)] * 4 + [lin(b)] * 2 + [lin(c1)])          # degree 7
    Qd = prod([lin(d)] * 2 + [lin(e)])                             # degree 3
    Rn = prod([lin(one)] * 4 + [lin(g)] * 2 + [lin(h)])            # degree 7
    out = []
    for k in range(1, 8):                                          # coefficients x^6 .. x^0
        q = Qd[k - 4] if k >= 4 else zero
        out.append(c * Pn[k] - q - c * Rn[k])
    return out


def newton_np(v):
    for it in range(80):
        f = np.array(F(list(v), 1.0 + 0j, 0j))
        J = np.zeros((7, 7), dtype=complex); h = 1e-7
        for j in range(7):
            w = v.copy(); w[j] += h
            J[:, j] = (np.array(F(list(w), 1.0 + 0j, 0j)) - f) / h
        try: dv = np.linalg.solve(J, -f)
        except np.linalg.LinAlgError: return None
        v = v + dv
        if not np.all(np.isfinite(v)) or np.max(np.abs(v)) > 1e6: return None
        if np.max(np.abs(dv)) < 1e-12: break
    f = np.array(F(list(v), 1.0 + 0j, 0j))
    return v if np.max(np.abs(f)) < 1e-9 else None


def good(v):
    c, b, c1, d, e, g, h = v
    pts = [0, 1, b, c1, d, e, g, h]
    return abs(c) > 1e-8 and min(abs(pts[i] - pts[j]) for i in range(8) for j in range(i)) > 1e-6


def main():
    sols = []
    tries = 0
    while tries < 60000 and len(sols) < 16:
        tries += 1
        v = (rng.normal(size=7) + 1j * rng.normal(size=7)) * 1.5
        s = newton_np(v)
        if s is None or not good(s): continue
        if all(np.max(np.abs(s - t)) > 1e-6 for t in sols): sols.append(s); print("found", len(sols), "after", tries, flush=True)
    print("solutions:", len(sols), "tries:", tries)
    mp.mp.dps = 120
    res = []
    for s in sols:
        x0 = [mp.mpc(z) for z in s]
        r = mp.findroot(lambda *v: F(list(v), mp.mpf(1), mp.mpf(0)), x0, tol=mp.mpf(10) ** -100, maxsteps=50)
        res.append([r[i] for i in range(7)])
    json.dump({"solutions": [[[mp.nstr(z.real, 110), mp.nstr(z.imag, 110)] for z in r] for r in res]}, open("belyi7.json", "w"), indent=1)


if __name__ == "__main__":
    main()
