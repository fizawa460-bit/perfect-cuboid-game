#!/usr/bin/env python3
"""Stage32 D8-LOW-GENUS: certified enumeration driver for one slice (CONTRACT.md §2).

Slice: integer classes x in Pic (rank 64) with K.x = d, F1.x = n1, sum_j Exc_j.x = e, and optionally Gamma49.x = v.
Constraints: x^2 >= c2min and x.Gamma >= 0 for all 140 known curves.

Everything here is EXACT (integers / rationals via python-flint):
  - particular solution x0 and kernel basis N (HNF), LLL-reduced basis Nr = N T;
  - M = -Nr^T G Nr (positive definite by Hodge; checked: every pivot d_i > 0);
  - M = U^T D U (U unit upper triangular), zs = M^-1 b, R = c + b.zs - c2min,
    so x^2 - c2min = R - sum_i d_i y_i^2 with y_i = (z_i - zs_i) + sum_{j>i} U_ij (z_j - zs_j);
  - linear forms l_k(z) = Gamma_k.x = f0_k + sum_i g_ki y_i (g = p U^-1), and the Cauchy-Schwarz constants
    S_k(i) = sum_{j<i} g_kj^2 / d_j.
Every rational is passed to certified_enum.c as an outward-rounded double interval [lo, hi] (lo <= q <= hi), so
every pruning decision there is a rigorous consequence of exact data. Leaves are rechecked here exactly.
If R < 0 (exactly), the slice is EMPTY.
Modes: default = enumerate the slice; --bound-only = only certify (exactly) that Gamma49.x <= 10 on the real
ellipsoid of the (unsplit) slice, which justifies splitting it by v = Gamma49.x in [0, 10] (v >= 0 is a constraint).
usage: python certified_driver.py REPO d n1 e c2min [--fix 49=v] [--bound-only] [--enum CMD]   -> one JSON line
"""
import json
import math
import shlex
import subprocess
import sys
import importlib.util
from fractions import Fraction
from pathlib import Path

import numpy as np
from flint import fmpz_mat, fmpq_mat, fmpq

REPO = Path(sys.argv[1]).resolve()
d, n1, e, c2min = (int(a) for a in sys.argv[2:6])
FIX = sys.argv[sys.argv.index("--fix") + 1] if "--fix" in sys.argv else None
ENUM = sys.argv[sys.argv.index("--enum") + 1] if "--enum" in sys.argv else str(Path(__file__).with_name("certified_enum"))
sys.path.insert(0, str(REPO / "stages/stage32/residual-32-01-production"))
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402


def load_retained(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


bundle = load_retained(REPO / "stages/stage33/33-07/picard_base_rows_retained.py", "b")
marking = load_retained(REPO / "stages/stage33/33-07/stage32_picard_marking_retained.py", "m")
ad = HperpIntegralPairingAdapter.from_retained(marking, bundle)
G = [[int(v) for v in r] for r in bundle["picard_gram_64x64"]]
P = [[int(v) for v in r] for r in ad.pairing_matrix.tolist()]
coords = [[int(v) for v in ad.class_coordinates_in_retained_basis[i, :]] for i in range(140)]
Gn = np.array(G, dtype=object); Pn = np.array(P, dtype=object)
exc = Pn[92:].sum(axis=0)
deg = (Pn[:92].sum(axis=0) + 5 * exc) // 19
Fs = []
for lbl in range(33, 45):
    E = np.array(coords[lbl - 1], dtype=object); pe = Pn.dot(E)
    F = 2 * E + sum(np.array(coords[k], dtype=object) for k in range(92, 140) if pe[k] > 0)
    if not any((F == X).all() for X in Fs):
        Fs.append(F)
F1 = Fs[0].dot(Gn)
rows = [list(deg), list(F1), list(exc)]
t = [d, n1, e]
if FIX:
    lab, val = FIX.split("=")
    rows.append(list(Pn[int(lab) - 1])); t.append(int(val))
out = {"d": d, "n1": n1, "e": e, "c2min": c2min, "fix": FIX}


def emit(status, classes=(), **kw):
    out.update(status=status, classes=list(classes), **kw)
    print(json.dumps(out)); sys.exit(0)


# exact affine slice
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
    emit("CONGRUENCE_EMPTY")
x0 = U.T[:, :r].dot(np.array([int(sol[i, 0].p) for i in range(r)], dtype=object))
if not (A.dot(x0) == np.array(t, dtype=object)).all():
    emit("CONGRUENCE_EMPTY")
N = U.T[:, r:]
n = N.shape[1]
M0 = -(N.T.dot(Gn).dot(N))
_, T = fmpz_mat([[int(v) for v in rw] for rw in M0.tolist()]).lll(transform=True, rep="gram", gram="exact")
T = np.array([[int(T[i, j]) for j in range(n)] for i in range(n)], dtype=object)
Nr = N.dot(T.T)
Mi = -(Nr.T.dot(Gn).dot(Nr))
M = [[fmpq(int(v)) for v in rw] for rw in Mi.tolist()]
b = [fmpq(int(v)) for v in Nr.T.dot(Gn).dot(x0)]
c = fmpq(int(x0.dot(Gn).dot(x0)))
# x^2 = c + 2 b.z - z^T M z ;  zs = M^-1 b ;  x^2 - c2min = R - (z - zs)^T M (z - zs)
zsq = fmpq_mat(M).solve(fmpq_mat([[v] for v in b]))
zs = [zsq[i, 0] for i in range(n)]
R = c + sum((bi * zi for bi, zi in zip(b, zs)), fmpq(0)) - c2min
if R < 0:
    emit("EMPTY", nodes=0)
# M = U^T D U with U unit upper triangular (pivots in ascending order). Then with w = z - zs,
# (z - zs)^T M (z - zs) = sum_i d_i y_i^2,  y_i = w_i + sum_{j>i} U_ij w_j,
# so fixing z_{n-1}, ..., z_i fixes y_{n-1}, ..., y_i, matching the recursion order of certified_enum.c.
Dg = [fmpq(0)] * n
Uu = [[fmpq(0)] * n for _ in range(n)]
for i in range(n):
    Dg[i] = M[i][i] - sum((Dg[k] * Uu[k][i] ** 2 for k in range(i)), fmpq(0))
    if not Dg[i] > 0:
        emit("ERROR M not positive definite")
    Uu[i][i] = fmpq(1)
    for j in range(i + 1, n):
        Uu[i][j] = (M[i][j] - sum((Dg[k] * Uu[k][i] * Uu[k][j] for k in range(i)), fmpq(0))) / Dg[i]
# linear forms: l_k = Gamma_k.(x0 + Nr z) = a_k + p_k.z = f0_k + (p_k U^-1) y
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
        row.append(acc)                       # S_k(i) = sum_{j<i} g_kj^2 / d_j
        acc = acc + g[k][i] ** 2 / Dg[i]
    S.append(row)
S49 = S[48][n - 1] + g[48][n - 1] ** 2 / Dg[n - 1]
# exact certificate that Gamma49.x <= 10 on the whole real ellipsoid of this slice:
# sup over {sum d_j y_j^2 <= R} of f0_49 + g_49.y equals f0_49 + sqrt(R * S49).
LE10 = bool((fmpq(10) - f0[48] >= 0) and ((fmpq(10) - f0[48]) ** 2 >= R * S49))
if "--bound-only" in sys.argv:
    emit("BOUND", gamma49_le_10_on_ellipsoid=LE10)


def iv(q):
    fr = Fraction(int(q.p), int(q.q))
    f = float(fr)                               # correctly rounded
    if Fraction(f) == fr:                       # exactly representable (e.g. 0): degenerate interval, no subnormals
        return (f, f)
    return (math.nextafter(f, -math.inf), math.nextafter(f, math.inf))


def flat(vals):
    return " ".join(f"{lo!r} {hi!r}" for lo, hi in (iv(v) for v in vals))


inp = [f"{n} 140", flat([R]), flat(Dg), flat(zs),
       flat([Uu[i][j] for i in range(n) for j in range(n)]),
       flat(f0), flat([g[k][i] for k in range(140) for i in range(n)]),
       flat([S[k][i] for k in range(140) for i in range(n)])]
proc = subprocess.run(shlex.split(ENUM), input="\n".join(inp), capture_output=True, text=True)
status = (proc.stderr.strip().split("\n")[-1] if proc.stderr.strip() else "?")
if proc.returncode != 0 or not status.startswith("COMPLETE"):
    emit("ERROR " + status + f" rc={proc.returncode}")
classes, leaves = [], 0
for line in proc.stdout.strip().split("\n"):
    if not line.strip():
        continue
    leaves += 1
    zz = np.array([int(v) for v in line.split()], dtype=object)
    x = x0 + Nr.dot(zz)
    pr = Pn.dot(x)
    if not (pr >= 0).all():
        continue
    c2 = int(x.dot(Gn).dot(x))
    if c2 < c2min:
        continue
    nu = int(sum(1 for v in pr[92:] if v > 0))
    classes.append({"C2": c2, "nu": nu, "maxm": int(max(pr[92:])), "x": [int(v) for v in x]})
emit(status, classes, leaves=leaves)
