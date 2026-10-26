#!/usr/bin/env python3
"""Stage32 D8-LOW-GENUS: exact tangency ideals over Q(i) for the two matching types (CONTRACT.md §3).

Model: P1_x x P1_y with cusps {0, inf, ±1, ±i}; classes {0, inf}, {±1}, {±i}.
For a class-preserving bijection s, L_s = (4,4) forms F that are singular at the 6 points (c, s(c)) (F and all four
partials vanish there).  u0..u{dim-1} are coordinates on L_s (a sympy nullspace basis, which is deterministic).
Tangency on each of the 12 cusp lines: F|line = (t - root)^2 q(t), and disc(q) = 0.  This holds iff F|line is
(t - root)^2 times a square (a double root of q anywhere, including at root or at infinity).
Writes tangency_swap.sing (s = swap 0<->inf, fixes ±1, ±i) and tangency_id.sing (s = id).
usage: python make_tangency_ideals.py [OUTDIR]   (prints a sha256 of each file)
"""
import hashlib
import sys
from pathlib import Path

import sympy as sp

x0, x1, y0, y1, t = sp.symbols("x0 x1 y0 y1 t")
I = sp.I
MONS = [x0**i * x1**(4 - i) * y0**j * y1**(4 - j) for i in range(5) for j in range(5)]
CUSP = {"0": (0, 1), "inf": (1, 0), "1": (1, 1), "-1": (-1, 1), "i": (I, 1), "-i": (-I, 1)}
SIGMAS = {
    "swap": {"0": "inf", "inf": "0", "1": "1", "-1": "-1", "i": "i", "-i": "-i"},
    "id": {k: k for k in CUSP},
}


def build(sigma):
    cs = sp.symbols("c0:25")
    F = sum(c * m for c, m in zip(cs, MONS))
    eqs = []
    for c in CUSP:
        (a0, a1), (b0, b1) = CUSP[c], CUSP[sigma[c]]
        sub = {x0: a0, x1: a1, y0: b0, y1: b1}
        eqs.append(F.subs(sub))
        for w in (x0, x1, y0, y1):
            eqs.append(sp.diff(F, w).subs(sub))
    ns = sp.Matrix([[sp.diff(e, c) for c in cs] for e in eqs]).nullspace()
    u = sp.symbols(f"u0:{len(ns)}")
    vec = sum((u[i] * ns[i] for i in range(len(ns))), sp.zeros(25, 1))
    FL = sp.expand(sum(vec[k] * MONS[k] for k in range(25)))
    inv = {sigma[k]: k for k in sigma}
    tang = []
    for c in CUSP:
        for vertical in (True, False):
            p0, p1 = CUSP[sigma[c]] if vertical else CUSP[inv[c]]
            a0, a1 = CUSP[c]
            g = sp.expand(FL.subs({x0: a0, x1: a1}) if vertical else FL.subs({y0: a0, y1: a1}))
            zv = (y0, y1) if vertical else (x0, x1)
            if p1 == 0:
                g = sp.expand(g.subs({zv[0]: 1, zv[1]: t})); root = 0
            else:
                g = sp.expand(g.subs({zv[0]: t, zv[1]: 1})); root = sp.nsimplify(p0) / p1
            q, r = sp.div(sp.Poly(g, t), sp.Poly((t - root) ** 2, t))
            assert r.is_zero, "F|line must vanish doubly at the partner point"
            qc = q.all_coeffs()
            qc = [0] * (3 - len(qc)) + qc
            A, B, C = qc
            tang.append(sp.expand(B**2 - 4 * A * C))
    return u, ns, vec, FL, tang


def singular_text(u, vec, tang):
    s = f"ring R = (0,I),({','.join(map(str, u))}),dp;\nminpoly = I^2+1;\n"
    s += "ideal T =\n" + ",\n".join(str(e).replace("**", "^") for e in tang) + ";\n"
    s += "// F as a polynomial in the u's, coefficient list in the 25 monomials x0^i x1^(4-i) y0^j y1^(4-j)\n"
    s += "matrix FC[25][1];\n"
    for k in range(25):
        s += f"FC[{k+1},1] = {str(sp.expand(vec[k])).replace('**', '^')};\n"
    return s


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
    for name, sigma in SIGMAS.items():
        u, ns, vec, FL, tang = build(sigma)
        txt = singular_text(u, vec, tang)
        (out / f"tangency_{name}.sing").write_bytes(txt.encode())
        print(name, "dim L =", len(u), "sha256", hashlib.sha256(txt.encode()).hexdigest())
