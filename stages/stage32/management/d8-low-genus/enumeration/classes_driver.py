#!/usr/bin/env python3
"""32R-21 driver: complete enumeration of numerical classes with fixed (d, n1, e) via the C enumerator fp_enum.

Fixed rows: K.C = d, F1.C = n1 (so F2.C = d - n1), sum_j C.E_j = e.  Constraints: C^2 >= c2min, C.Gamma >= 0 for all 140.
Exact verification of every leaf in Python (integer arithmetic).  Prints classes with their invariants.
usage: python 32R-21_classes_driver.py REPO d n1 e [c2min] [--enum PATH]
"""
import importlib.util, math, subprocess, sys, json
from pathlib import Path
import numpy as np
from flint import fmpz_mat, fmpq_mat

REPO = Path(sys.argv[1]).resolve()
d, n1, e = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
c2min = int(sys.argv[5]) if len(sys.argv) > 5 and not sys.argv[5].startswith("--") else -2 - d
ENUM = sys.argv[sys.argv.index("--enum") + 1] if "--enum" in sys.argv else "./fp_enum"
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
G = np.array([[int(v) for v in r] for r in bundle["picard_gram_64x64"]], dtype=object)
P = np.array([[int(v) for v in r] for r in ad.pairing_matrix.tolist()], dtype=object)
exc = P[92:].sum(axis=0)
deg = (P[:92].sum(axis=0) + 5 * exc) // 19
coords = [np.array([int(v) for v in ad.class_coordinates_in_retained_basis[i, :]], dtype=object) for i in range(140)]
Fs = []
for lbl in range(33, 45):
    E = coords[lbl - 1]; pe = P.dot(E)
    F = 2 * E + sum(coords[k] for k in range(92, 140) if pe[k] > 0)
    if not any((F == X).all() for X in Fs):
        Fs.append(F)
F1 = Fs[0].dot(G)
rows = [list(deg), list(F1), list(exc)]
t = [d, n1, e]
if "--fix" in sys.argv:
    lab, val = sys.argv[sys.argv.index("--fix") + 1].split("=")
    rows.append(list(P[int(lab) - 1])); t.append(int(val))
A = np.array([[int(v) for v in r] for r in rows], dtype=object)
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
    print(json.dumps({"d": d, "n1": n1, "e": e, "status": "CONGRUENCE_EMPTY", "classes": []})); sys.exit(0)
x0 = U.T[:, :r].dot(np.array([int(sol[i, 0].p) for i in range(r)], dtype=object))
if not (A.dot(x0) == np.array(t, dtype=object)).all():
    print(json.dumps({"d": d, "n1": n1, "e": e, "status": "CONGRUENCE_EMPTY", "classes": []})); sys.exit(0)
N = U.T[:, r:]
dim = N.shape[1]
M = -(N.T.dot(G).dot(N))
red, T = fmpz_mat([[int(v) for v in rw] for rw in M.tolist()]).lll(transform=True, rep="gram", gram="exact")
T = np.array([[int(T[i, j]) for j in range(dim)] for i in range(dim)], dtype=object)
Nr = N.dot(T.T)
Mf = (-(Nr.T.dot(G).dot(Nr))).astype(float)
Rc = np.linalg.cholesky(Mf).T
b = Nr.T.dot(G).dot(x0).astype(float); c = float(x0.dot(G).dot(x0))
zs = np.linalg.solve(Mf, b); R = c + b @ zs - c2min
Pk = P.dot(Nr).astype(float)
Rk = Pk @ np.linalg.inv(Rc)
Sf = np.concatenate([np.zeros((140, 1)), np.cumsum(Rk ** 2, axis=1)], axis=1)
f0 = P.dot(x0).astype(float) + Pk @ zs
inp = [f"{int(dim)} 140 {float(R)!r}"]
inp += [" ".join(repr(float(v)) for v in Rc.flatten())]
inp += [" ".join(repr(float(v)) for v in zs)]
inp += [" ".join(repr(float(v)) for v in Rk.flatten())]
inp += [" ".join(repr(float(v)) for v in Sf.flatten())]
inp += [" ".join(repr(float(v)) for v in f0)]
import shlex
proc = subprocess.run(shlex.split(ENUM) + ([sys.argv[sys.argv.index("--limit") + 1]] if "--limit" in sys.argv else []), input="\n".join(inp), capture_output=True, text=True)
status = (proc.stderr.strip().split("\n")[-1] if proc.stderr else "?") + f" rc={proc.returncode} outlen={len(proc.stdout)}"
classes = []
for line in proc.stdout.strip().split("\n"):
    if not line.strip():
        continue
    zz = np.array([int(v) for v in line.split()], dtype=object)
    x = x0 + Nr.dot(zz)
    pr = P.dot(x)
    if not (pr >= 0).all():
        continue
    c2 = int(x.dot(G).dot(x))
    if c2 < c2min:
        continue
    nu = int(sum(1 for v in pr[92:] if v > 0))
    classes.append({"C2": c2, "nu": nu, "maxm": int(max(pr[92:])), "x": [int(v) for v in x]})
print(json.dumps({"fix": sys.argv[sys.argv.index("--fix") + 1] if "--fix" in sys.argv else None, "d": d, "n1": n1, "e": e, "c2min": c2min, "status": status, "radius2": R, "classes": classes}))
