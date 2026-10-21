#!/usr/bin/env python3
"""Stage32 D10-LOW-GENUS: shared exact routines for the symmetry-reduced certified enumeration (CONTRACT.md §2).

- load(repo): Picard Gram matrix G, pairing matrix P (140 known curves x 64), curve coordinates, deg row (K.x),
  exceptional row (sum of exceptional pairings), F1 row, boundary sides (V = F1 side, H = F2 side).
- slice_data(...): exact affine slice {K.x = d, F1.x = n1, sum_j Exc_j.x = e, Gamma_l.x = v_l for fixed boundary l}
  -> enumerator input (outward-rounded intervals) exactly as in d8-low-genus/enumeration/certified_driver.py.
- bvectors(n1, n2, e): all boundary vectors b = (C.E_l) allowed by 0 <= b_l <= n_side // 2 and
  sum_V b = (6 n1 - e) / 2, sum_H b = (6 n2 - e) / 2   (F_line.C = 2 b_l + sum of the m_j on the line >= 2 b_l).
- group(gens): closure of permutation generators of the 140 curves.
Everything except the enumerator interval data is exact (python-flint).
"""
import importlib.util
import itertools
import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
from flint import fmpz_mat, fmpq_mat, fmpq

D = {}


def load(repo):
    repo = Path(repo)
    sys.path.insert(0, str(repo / "stages/stage32/residual-32-01-production"))
    from hperp_integral_adapter import HperpIntegralPairingAdapter

    def lr(path, name):
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.load()
    bundle = lr(repo / "stages/stage33/33-07/picard_base_rows_retained.py", "b")
    marking = lr(repo / "stages/stage33/33-07/stage32_picard_marking_retained.py", "m")
    ad = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    Gn = np.array([[int(v) for v in r] for r in bundle["picard_gram_64x64"]], dtype=object)
    Pn = np.array([[int(v) for v in r] for r in ad.pairing_matrix.tolist()], dtype=object)
    Cn = [np.array([int(v) for v in ad.class_coordinates_in_retained_basis[i, :]], dtype=object) for i in range(140)]
    exc = Pn[92:].sum(axis=0)
    deg = (Pn[:92].sum(axis=0) + 5 * exc) // 19
    Fc = {}
    for lbl in range(33, 45):
        pe = Pn.dot(Cn[lbl - 1])
        Fc[lbl] = tuple(2 * Cn[lbl - 1] + sum(Cn[k] for k in range(92, 140) if pe[k] > 0))
    F1 = sorted(set(Fc.values()))[0]
    side = {lbl: ("V" if Fc[lbl] == F1 else "H") for lbl in Fc}
    D.update(Gn=Gn, Pn=Pn, Cn=Cn, exc=exc, deg=deg, F1row=np.array(F1, dtype=object).dot(Gn), side=side,
             V=[l for l in range(33, 45) if side[l] == "V"], H=[l for l in range(33, 45) if side[l] == "H"])
    return D


def iv(q):
    fr = Fraction(int(q.p), int(q.q))
    f = float(fr)
    if Fraction(f) == fr:
        return (f, f)
    return (math.nextafter(f, -math.inf), math.nextafter(f, math.inf))


def flat(vals):
    return " ".join(f"{lo!r} {hi!r}" for lo, hi in (iv(v) for v in vals))


def slice_data(d, n1, e, c2min, fixes):
    """Return ('CONGRUENCE_EMPTY'|'EMPTY'|'OK', payload). payload for OK: (enumerator input text, x0, Nr)."""
    Gn, Pn = D["Gn"], D["Pn"]
    rows = [list(D["deg"]), list(D["F1row"]), list(D["exc"])] + [list(Pn[lab - 1]) for lab, _ in fixes]
    t = [d, n1, e] + [v for _, v in fixes]
    A = np.array(rows, dtype=object)
    H, U = fmpz_mat([[int(v) for v in r] for r in A.T.tolist()]).hnf(transform=True)
    H = [[int(H[i, j]) for j in range(len(rows))] for i in range(64)]
    U = np.array([[int(U[i, j]) for j in range(64)] for i in range(64)], dtype=object)
    r = sum(1 for i in range(64) if any(H[i]))
    HT = [[H[i][j] for i in range(r)] for j in range(len(rows))]
    piv, rr = [], 0
    for cc in range(r):
        while HT[rr][cc] == 0:
            rr += 1
        piv.append(rr); rr += 1
    sol = fmpq_mat([[HT[piv[i]][j] for j in range(r)] for i in range(r)]).solve(fmpq_mat([[t[piv[i]]] for i in range(r)]))
    if any(sol[i, 0].q != 1 for i in range(r)):
        return "CONGRUENCE_EMPTY", None
    x0 = U.T[:, :r].dot(np.array([int(sol[i, 0].p) for i in range(r)], dtype=object))
    if not (A.dot(x0) == np.array(t, dtype=object)).all():
        return "CONGRUENCE_EMPTY", None
    N = U.T[:, r:]
    n = N.shape[1]
    M0 = -(N.T.dot(Gn).dot(N))
    _, T = fmpz_mat([[int(v) for v in rw] for rw in M0.tolist()]).lll(transform=True, rep="gram", gram="exact")
    T = np.array([[int(T[i, j]) for j in range(n)] for i in range(n)], dtype=object)
    Nr = N.dot(T.T)
    M = [[fmpq(int(v)) for v in rw] for rw in (-(Nr.T.dot(Gn).dot(Nr))).tolist()]
    b = [fmpq(int(v)) for v in Nr.T.dot(Gn).dot(x0)]
    c = fmpq(int(x0.dot(Gn).dot(x0)))
    zsq = fmpq_mat(M).solve(fmpq_mat([[v] for v in b]))
    zs = [zsq[i, 0] for i in range(n)]
    R = c + sum((bi * zi for bi, zi in zip(b, zs)), fmpq(0)) - c2min
    if R < 0:
        return "EMPTY", str(R)
    Dg = [fmpq(0)] * n
    Uu = [[fmpq(0)] * n for _ in range(n)]
    for i in range(n):
        Dg[i] = M[i][i] - sum((Dg[k] * Uu[k][i] ** 2 for k in range(i)), fmpq(0))
        if not Dg[i] > 0:
            raise ValueError("form not positive definite")
        Uu[i][i] = fmpq(1)
        for j in range(i + 1, n):
            Uu[i][j] = (M[i][j] - sum((Dg[k] * Uu[k][i] * Uu[k][j] for k in range(i)), fmpq(0))) / Dg[i]
    pk = fmpq_mat([[fmpq(int(v)) for v in rw] for rw in Pn.dot(Nr).tolist()])
    ak = Pn.dot(x0)
    Uinv = fmpq_mat(Uu).inv()
    f0m = pk * fmpq_mat([[v] for v in zs])
    f0 = [fmpq(int(ak[k])) + f0m[k, 0] for k in range(140)]
    gm = pk * Uinv
    g = [[gm[k, i] for i in range(n)] for k in range(140)]
    S = []
    for k in range(140):
        acc, row = fmpq(0), []
        for i in range(n):
            row.append(acc)
            acc = acc + g[k][i] ** 2 / Dg[i]
        S.append(row)
    inp = "\n".join([f"{n} 140", flat([R]), flat(Dg), flat(zs), flat([Uu[i][j] for i in range(n) for j in range(n)]),
                     flat(f0), flat([g[k][i] for k in range(140) for i in range(n)]),
                     flat([S[k][i] for k in range(140) for i in range(n)])])
    return "OK", (inp, x0, Nr)


def leaf_classes(stdout, x0, Nr, c2min):
    """exact recheck of enumerator leaves: pairing >= 0 with all 140 curves and x^2 >= c2min."""
    Gn, Pn = D["Gn"], D["Pn"]
    out, leaves = [], 0
    for line in stdout.strip().split("\n"):
        if not line.strip():
            continue
        leaves += 1
        x = x0 + Nr.dot(np.array([int(v) for v in line.split()], dtype=object))
        if (Pn.dot(x) >= 0).all() and int(x.dot(Gn).dot(x)) >= c2min:
            out.append([int(v) for v in x])
    return out, leaves


def bvectors(n1, n2, e):
    sv, sh = 6 * n1 - e, 6 * n2 - e
    if sv % 2 or sh % 2 or sv < 0 or sh < 0:
        return []
    sv //= 2; sh //= 2
    vs = [p for p in itertools.product(range(n1 // 2 + 1), repeat=6) if sum(p) == sv]
    hs = [p for p in itertools.product(range(n2 // 2 + 1), repeat=6) if sum(p) == sh]
    return [tuple(zip(D["V"], pv)) + tuple(zip(D["H"], ph)) for pv in vs for ph in hs]


def group(gens):
    ident = tuple(range(140)); grp = {ident}; fr = [ident]
    while fr:
        nf = []
        for g_ in fr:
            for h in gens:
                k = tuple(h[g_[i]] for i in range(140))
                if k not in grp:
                    grp.add(k); nf.append(k)
        fr = nf
    return sorted(grp)


def act_b(g_, b):
    """image of a boundary vector (tuple of (label, value)) under the curve permutation g_ (0-based indices)."""
    return {g_[l - 1] + 1: v for l, v in b}


def orbit_reps(pats, use):
    """deterministic representatives: scan pats in order, take the first unseen, mark its whole orbit."""
    order = D["V"] + D["H"]
    seen, reps = set(), []
    for p in pats:
        key = tuple(v for _, v in p)
        if key in seen:
            continue
        reps.append(p)
        for g_ in use:
            nb = act_b(g_, p)
            seen.add(tuple(nb[l] for l in order))
    return reps
