#!/usr/bin/env python3
"""Stage32 D10-LOW-GENUS: residual curves of hyperplane sections through three conics (CONTRACT.md §4).

Explicit cuboid surface S in P^6 (a,b,c,d,e,f,g): d^2 = a^2+b^2, e^2 = a^2+c^2, f^2 = b^2+c^2, g^2 = a^2+b^2+c^2.
32 conics (planes a=0, b=0, c=0, g=0 with sign choices). For every triple of distinct conics the rank of the span
of their planes is computed exactly and recorded by rank (rank 6 = unique hyperplane; rank <= 5 = at least a pencil).
Triples containing g-family conics are moved to rational triples by the automorphisms
  tau:(a,b,c,d,e,f,g) -> (g, ib, ic, e, d, if, a),  rho_b: a<->b, e<->f,  rho_c: a<->c, d<->f
(each checked to preserve the span of the four quadrics), which preserve S, the conic set and residual genera.
Writes one Singular script per rational representative triple and projection (two independent random
projections), and triples.json (every rank-6 triple -> its representative).
usage: python make_residuals.py OUTDIR
"""
import itertools
import json
import sys
from pathlib import Path

import sympy as sp

I = sp.I
V = sp.symbols("a b c d e f g")
a, b, c, d, e, f, g = V
QUADS = [d**2 - a**2 - b**2, e**2 - a**2 - c**2, f**2 - b**2 - c**2, g**2 - a**2 - b**2 - c**2]
CONICS = []
for s in itertools.product((1, -1), repeat=3):
    e1, e2, e3 = s
    CONICS.append(("a0" + str(s), [a, d - e1 * b, e - e2 * c, g - e3 * f]))
    CONICS.append(("b0" + str(s), [b, d - e1 * a, f - e2 * c, g - e3 * e]))
    CONICS.append(("c0" + str(s), [c, e - e1 * a, f - e2 * b, g - e3 * d]))
    CONICS.append(("g0" + str(s), [g, d - e1 * I * c, e - e2 * I * b, f - e3 * I * a]))
PLANES = [sp.Matrix([[sp.diff(l, v) for v in V] for l in L]).nullspace() for _, L in CONICS]
TAU = sp.Matrix([[0, 0, 0, 0, 0, 0, 1], [0, I, 0, 0, 0, 0, 0], [0, 0, I, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, I, 0], [1, 0, 0, 0, 0, 0, 0]])
RHOB = sp.Matrix(7, 7, lambda r, k: 1 if (r, k) in {(0, 1), (1, 0), (2, 2), (3, 3), (4, 5), (5, 4), (6, 6)} else 0)
RHOC = sp.Matrix(7, 7, lambda r, k: 1 if (r, k) in {(0, 2), (1, 1), (2, 0), (3, 5), (4, 4), (5, 3), (6, 6)} else 0)
PROJ = {1: [[3, 5, -7, 2, 11, -4], [2, -9, 1, 6, -3, 8], [1, 1, 4, -5, 7, 2]],
        2: [[-6, 1, 9, -2, 5, 3], [4, 7, -3, 1, -8, 2], [2, -5, 6, 9, 1, -7]]}


def is_automorphism(M):
    sub = dict(zip(V, M * sp.Matrix(V)))
    Qt = [sp.expand(q.subs(sub, simultaneous=True)) for q in QUADS]
    mons = sorted({mm for q in QUADS + Qt for mm in sp.Poly(q, *V).monoms()})
    A = sp.Matrix([[sp.Poly(q, *V).coeff_monomial(mm) for mm in mons] for q in QUADS + Qt])
    return A.rank() == 4


def conics_on_S():
    """each listed conic lies on S: the four quadrics vanish on its plane modulo the plane's quadric."""
    ok = True
    for (_, L), P in zip(CONICS, PLANES):
        t = sp.symbols("t0:3")
        pt = sum((t[k] * P[k] for k in range(3)), sp.zeros(7, 1))
        vals = [sp.expand(q.subs(dict(zip(V, pt)), simultaneous=True)) for q in QUADS]
        # all four restrictions must be proportional to one nonzero quadratic form (the conic)
        polys = [sp.Poly(v_, *t) for v_ in vals if v_ != 0]
        base = polys[0]
        ok &= all(sp.simplify(sp.Matrix([base.coeffs(), p.coeffs()]).rank()) == 1 and len(p.coeffs()) == len(base.coeffs()) for p in polys)
    return ok


def conic_index(basis):
    for t, P in enumerate(PLANES):
        if sp.Matrix.hstack(*(P + basis)).rank() == 3:
            return t
    raise ValueError


def triples():
    by_rank = {}
    for i, j, k in itertools.combinations(range(32), 3):
        rk = sp.Matrix.hstack(*(PLANES[i] + PLANES[j] + PLANES[k])).rank()
        by_rank.setdefault(rk, []).append((i, j, k))
    return by_rank


def rep_of(i, j, k):
    fam = {CONICS[t][0][:2] for t in (i, j, k)}
    if "g0" not in fam:
        return (i, j, k)
    miss = next(x for x in ("a0", "b0", "c0") if x not in fam)
    M = TAU * {"a0": sp.eye(7), "b0": RHOB, "c0": RHOC}[miss]
    return tuple(sorted(conic_index([M * vv for vv in PLANES[t]]) for t in (i, j, k)))


def sing(x):
    return str(sp.expand(x)).replace("**", "^")


def script(tri, h, proj):
    piv = next(m for m in (6, 5, 4, 3, 2, 1, 0) if h[m] != 0)
    others = [m for m in range(7) if m != piv]
    subs = {V[piv]: -sum(h[m] * V[m] for m in others) / h[piv]}
    names = [str(V[m]) for m in others]
    Ss = [sing(q.subs(subs)) for q in QUADS]
    Cs = [[sing(l.subs(subs)) for l in CONICS[t][1]] for t in tri]
    lin = lambda r: "+".join(f"({r[m]})*{names[m]}" for m in range(6))
    P = PROJ[proj]
    s = 'LIB "elim.lib"; LIB "normal.lib"; LIB "absfact.lib";\n'
    s += f"ring R = 0,({','.join(names)},u,v,w),dp;\n"
    s += "ideal S = " + ",".join(Ss) + ";\n"
    for t in range(3):
        s += f"ideal C{t} = std(S + ideal(" + ",".join(x for x in Cs[t] if x != "0") + "));\n"
    s += "list L = sat(std(S), intersect(C0, intersect(C1, C2))); ideal Res = std(L[1]);\n"
    s += f"ideal Pr = Res, u - ({lin(P[0])}), v - ({lin(P[1])}), w - ({lin(P[2])});\n"
    s += f"ideal E = eliminate(Pr, {'*'.join(names)});\n"
    s += "int ng = size(E); poly F = subst(E[1], w, 1); int rd = mult(Res); int pd = deg(E[1]);\n"
    s += "ring r3 = 0,(u,v),dp; poly F = imap(R, F);\n"
    s += "int na; def AF = absFactorize(F); setring AF; na = size(absolute_factors[1]) - 1; setring r3;\n"
    s += "int gg = -99; if (na == 1) { gg = genus(ideal(F)); }\n"
    s += f'"RESULT {tri[0]} {tri[1]} {tri[2]} proj {proj} resdeg", rd, "planegens", ng, "planedeg", pd, "absfactors", na, "genus", gg;\nquit;\n'
    return s


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    (out / "sing").mkdir(parents=True, exist_ok=True)
    assert all(is_automorphism(M) for M in (TAU, RHOB, RHOC))
    assert conics_on_S()
    by_rank = triples()
    r6 = by_rank.get(6, [])
    reps = {}
    for t in r6:
        reps.setdefault(rep_of(*t), []).append(t)
    assert all(sp.Matrix.hstack(*(PLANES[r[0]] + PLANES[r[1]] + PLANES[r[2]])).rank() == 6 for r in reps)
    info = {"triples_by_span_rank": {str(k): len(v) for k, v in sorted(by_rank.items())}, "representatives": len(reps)}
    print(info)
    for r in reps:
        h = sp.Matrix.hstack(*(PLANES[r[0]] + PLANES[r[1]] + PLANES[r[2]])).T.nullspace()[0]
        h = [sp.nsimplify(x) for x in h]
        for proj in (1, 2):
            (out / "sing" / f"r_{r[0]}_{r[1]}_{r[2]}_p{proj}.sing").write_bytes(script(r, h, proj).encode())
    (out / "triples.json").write_bytes((json.dumps({"info": info, "map": {f"{t[0]},{t[1]},{t[2]}": list(rep_of(*t)) for t in r6},
                                                    "conics": [n for n, _ in CONICS]}, indent=0) + "\n").encode())
