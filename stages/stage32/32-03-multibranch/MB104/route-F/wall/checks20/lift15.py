#!/usr/bin/env python3
"""checks20 / lift15.py -- 17-adic Newton lift of the F_p solutions of vfp20 (normal form c x A1^2 B1^4 - A2^2 B2^4 =
c (x - 1) A3^2 B3^4), then the minimal polynomial of c over Q is found with PARI/GP algdep (p-adic).
Usage: python -I lift15.py n p 'passport-json' K"""
import sys, json, subprocess
from sympy import symbols, Poly, expand, GF
from sympy import Matrix
x = symbols("x")
GP = r"C:/Program Files (x86)/Pari64-2-19-0/gp.exe"

def main():
    n, p = int(sys.argv[1]), int(sys.argv[2]); pp = json.loads(sys.argv[3]); K = int(sys.argv[4])
    (a1, b1), (a2, b2), (a3, b3) = pp
    recs = [json.loads(l) for l in open("vfp20.jsonl") if l.strip()]
    rec = [r for r in recs if r["n"] == n and r["p"] == p and r["passport"] == pp][-1]
    names = (["c"] + [f"u{i}" for i in range(a1)] + [f"v{i}" for i in range(b1)] + [f"w{i}" for i in range(a2)]
             + [f"z{i}" for i in range(b2)] + [f"r{i}" for i in range(a3)] + [f"s{i}" for i in range(b3)])
    V = symbols(" ".join(names)); V = list(V) if isinstance(V, tuple) else [V]
    it = iter(V); c = next(it)
    def mon(d): return x ** d + sum(next(it) * x ** i for i in range(d))
    A1, B1, A2, B2, A3, B3 = mon(a1), mon(b1), mon(a2), mon(b2), mon(a3), mon(b3)
    E = Poly(expand(c * x * A1 ** 2 * B1 ** 4 - A2 ** 2 * B2 ** 4 - c * (x - 1) * A3 ** 2 * B3 ** 4), x)
    eqs = [E.coeff_monomial(x ** k) for k in range(n)]
    assert len(eqs) == len(V), (len(eqs), len(V))
    J = Matrix(eqs).jacobian(V)
    from sympy import lambdify
    fE = lambdify(V, eqs, "math"); fJ = lambdify(V, J.tolist(), "math")
    out = []
    for si, (cc, LA1, LB1, LA2, LB2) in enumerate(rec["solutions"]):
        # A3, B3 from q = R / (c (x - 1)) over F_p
        dom = GF(p)
        P = lambda L: Poly([int(t) for t in L[::-1]], x, domain=dom)
        q = (cc * Poly([1, 0], x, domain=dom) * P(LA1) ** 2 * P(LB1) ** 4 - P(LA2) ** 2 * P(LB2) ** 4).quo(Poly([cc, -cc], x, domain=dom))
        A3p = Poly(1, x, domain=dom); B3p = Poly(1, x, domain=dom)
        for f, e in q.factor_list()[1]:
            if e == 2: A3p *= f
            elif e == 4: B3p *= f
            else: raise SystemExit("bad shape")
        lc = q.LC()
        def low(Pl, d):
            cf = [int(t) % p for t in Pl.monic().all_coeffs()[::-1]]
            return cf[:d]
        x0 = [cc] + [int(t) for t in LA1[:a1]] + [int(t) for t in LB1[:b1]] + [int(t) for t in LA2[:a2]] + \
             [int(t) for t in LB2[:b2]] + low(A3p, a3) + low(B3p, b3)
        x0 = [t % p for t in x0]
        assert all(v % p == 0 for v in fE(*x0)), "not a solution mod p"
        M = p; xs = x0
        while M < p ** K:
            M2 = min(M * M, p ** K)
            Ev = [v % M2 for v in fE(*xs)]; Jv = [[v % M2 for v in row] for row in fJ(*xs)]
            delta = solve_mod(Jv, Ev, M2, p)
            xs = [(a - d) % M2 for a, d in zip(xs, delta)]; M = M2
        assert all(v % p ** K == 0 for v in fE(*xs))
        out.append(xs)
        print(f"solution {si}: lifted to {p}^{K}", flush=True)
    # PARI: minimal polynomials of c (and of the sum / product of the two c's)
    lines = [f"K={K}; p={p};"]
    for si, xs in enumerate(out):
        lines.append(f"c{si} = {xs[0]} + O(p^K);")
    for si in range(len(out)):
        for d in (1, 2, 4, 6, 8, 12):
            lines.append(f"P = algdep(c{si}, {d}); print(\"sol {si} deg {d}: \", P, \"  height \", round(log(normlp(Vec(P)))/log(10)), \"  |val| \", valuation(subst(P,'x,c{si}),p));")
    if len(out) == 2:
        for d in (1, 2, 4):
            lines.append(f"P = algdep(c0+c1, {d}); print(\"sum deg {d}: \", P);")
            lines.append(f"P = algdep(c0*c1, {d}); print(\"prod deg {d}: \", P);")
    open("lift15.gp", "w").write("\n".join(lines) + "\nquit\n")
    r = subprocess.run([GP, "-q", "-f", "lift15.gp"], capture_output=True, text=True, timeout=3000)
    print(r.stdout); print(r.stderr[-2000:])

def solve_mod(A, b, M, p):
    n = len(A); A = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] % p)
        A[col], A[piv] = A[piv], A[col]
        inv = pow(A[col][col], -1, M)
        A[col] = [(v * inv) % M for v in A[col]]
        for r in range(n):
            if r != col and A[r][col]:
                f = A[r][col]; A[r] = [(v - f * w) % M for v, w in zip(A[r], A[col])]
    return [A[i][n] for i in range(n)]

if __name__ == "__main__":
    main()
