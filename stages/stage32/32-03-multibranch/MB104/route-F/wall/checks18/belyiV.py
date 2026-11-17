#!/usr/bin/env python3
"""checks18 / belyiV.py -- Belyi maps pbar of the V-symmetric slack-0 maps, any passport (ANSWER-18, 2.4).

Passport: over the k-th branch point (0, oo, 1) the ramification is 1 2^a_k 4^b_k.  The three unramified points are put
at 0, oo, 1, so each dessin gives exactly one solution:
    pbar = c x A1(x)^2 B1(x)^4 / (A2(x)^2 B2(x)^4),   pbar - 1 = c (x - 1) A3(x)^2 B3(x)^4 / (A2(x)^2 B2(x)^4),
A_k, B_k monic of degrees a_k, b_k.  Unknowns: c and the lower coefficients (n in all); equations: the n coefficients.
Newton from random starts (numpy), polish with mpmath, write the solutions for gp (belyiV.gp factors the polynomials).
Usage: python -I belyiV.py a1,b1 a2,b2 a3,b3 expected_count [max_tries]
"""
import sys, json
import numpy as np
import mpmath as mp


def pmul(a, b, zero):
    r = [zero] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] = r[i + j] + x * y
    return r


def ppow(a, k, one, zero):
    r = [one]
    for _ in range(k): r = pmul(r, a, zero)
    return r


def split(v, pp, one):
    c = v[0]; k = 1; polys = []
    for a, b in pp:
        A = [one] + list(v[k:k + a]); k += a
        Bq = [one] + list(v[k:k + b]); k += b
        polys.append((A, Bq))
    return c, polys


def F(v, pp, one, zero):
    n = len(v)
    c, polys = split(v, pp, one)
    def fib(A, Bq, lin):
        r = pmul(ppow(A, 2, one, zero), ppow(Bq, 4, one, zero), zero)
        return pmul(r, lin, zero) if lin else r
    N0 = fib(*polys[0], [one, zero])          # degree n
    D = fib(*polys[1], None)                  # degree n - 1
    N1 = fib(*polys[2], [one, -one])          # degree n
    return [c * N0[k] - D[k - 1] - c * N1[k] for k in range(1, n + 1)]


def newton_np(v, pp):
    n = len(v)
    for it in range(100):
        f = np.array(F(list(v), pp, 1.0 + 0j, 0j))
        J = np.zeros((n, n), dtype=complex); h = 1e-7
        for j in range(n):
            w = v.copy(); w[j] += h
            J[:, j] = (np.array(F(list(w), pp, 1.0 + 0j, 0j)) - f) / h
        try: dv = np.linalg.solve(J, -f)
        except np.linalg.LinAlgError: return None
        nd = np.max(np.abs(dv))
        if nd > 2.0: dv *= 2.0 / nd
        v = v + dv
        if not np.all(np.isfinite(v)) or np.max(np.abs(v)) > 1e7: return None
        if nd < 1e-12 * max(1.0, np.max(np.abs(v))): break
    else:
        return None                       # no quadratic convergence: a degenerate (singular) solution, discard
    f = np.array(F(list(v), pp, 1.0 + 0j, 0j))
    return v if np.max(np.abs(f)) < 1e-8 * max(1.0, np.max(np.abs(v)) ** 4) else None


def good(v, pp):
    """all points of the three fibres distinct, c != 0"""
    c, polys = split(list(v), pp, 1.0 + 0j)
    if abs(c) < 1e-9: return False
    pts = [0j, 1 + 0j]
    for A, Bq in polys:
        for q in (A, Bq):
            if len(q) > 1: pts += list(np.roots(q))
    pts = np.array(pts)
    d = np.abs(pts[:, None] - pts[None, :]) + np.eye(len(pts))
    return d.min() > 1e-3


def mp_newton(x, pp):
    """Newton in mpmath with a numerical Jacobian (step 10^-60 at dps 130); stops when the residual is below 10^-110"""
    n = len(x); h = mp.mpf(10) ** -60; one, zero = mp.mpf(1), mp.mpf(0)
    for it in range(40):
        f = mp.matrix(F(x, pp, one, zero))
        if mp.norm(f, mp.inf) < mp.mpf(10) ** -110 and it > 0: return x
        J = mp.matrix(n, n)
        for j in range(n):
            w = list(x); w[j] = w[j] + h
            g = F(w, pp, one, zero)
            for i in range(n): J[i, j] = (g[i] - f[i]) / h
        dv = mp.lu_solve(J, -f)
        x = [x[i] + dv[i] for i in range(n)]
    raise RuntimeError("mp_newton did not converge")


def main():
    pp = [tuple(map(int, s.split(","))) for s in sys.argv[1:4]]
    want = int(sys.argv[4]); maxtries = int(sys.argv[5]) if len(sys.argv) > 5 else 200000
    n = 1 + sum(a + b for a, b in pp)
    assert all(1 + 2 * a + 4 * b == n for a, b in pp)
    tag = "_".join(f"{a}{b}" for a, b in pp)
    rng = np.random.default_rng(1800 + n)
    sols = []; tries = 0
    while tries < maxtries and len(sols) < want:
        tries += 1
        v = (rng.normal(size=n) + 1j * rng.normal(size=n)) * rng.choice([0.5, 1.0, 2.0, 4.0])
        s = newton_np(v, pp)
        if s is None or not good(s, pp): continue
        if all(np.max(np.abs(s - t)) > 1e-6 * max(1, np.max(np.abs(s))) for t in sols):
            sols.append(s); print("found", len(sols), "after", tries, flush=True)
    print(f"n = {n}, passport {pp}: solutions {len(sols)} (expected {want}), tries {tries}")
    mp.mp.dps = 130
    res = []
    for s in sols:
        x0 = [mp.mpc(z) for z in s]
        r = mp_newton(x0, pp)
        res.append(r)
    with open(f"belyiV_{tag}.gpdata", "w") as f:
        f.write(f"S = vector({len(res)});\n")
        for k, r in enumerate(res):
            f.write(f"S[{k + 1}] = [" + ",".join(f"({mp.nstr(z.real, 120)})+I*({mp.nstr(z.imag, 120)})" for z in r) + "];\n")
    print("wrote", f"belyiV_{tag}.gpdata")


if __name__ == "__main__":
    main()
