"""32R-67: split geometric reps by the audited unibranch node-count Hurwitz condition (Stage32
management/unibranch-node-hurwitz): unibranch g in {0,1} (not a fibre component) needs
nu >= e/2 + max(n1,n2) - 2g + 2, nu = #{j : m_j > 0}. Classes failing it for every allowed g are multibranch-only.
usage: python ub_split.py d"""
import sys, json
import numpy as np
from collections import Counter
d = int(sys.argv[1])
sys.path.insert(0, "C:/Users/fizaw/claudework/stage32_research/d12_run")
import slice_lib as L
L.load("C:/Users/fizaw/claudework/perfect-cuboid-game")
Gn, Pn, Cn = L.D["Gn"], L.D["Pn"], L.D["Cn"]
Fs = sorted(set(tuple(2 * Cn[l - 1] + sum(Cn[k] for k in range(92, 140) if Pn.dot(Cn[l - 1])[k] > 0)) for l in range(33, 45)))
F1r = np.array([int(v) for v in np.array(Fs[0], dtype=object).dot(Gn)], dtype=np.int64)
F2r = np.array([int(v) for v in np.array(Fs[1], dtype=object).dot(Gn)], dtype=np.int64)
PE = np.array([[int(v) for v in Pn[k]] for k in range(92, 140)], dtype=np.int64)
G64 = np.array([[int(v) for v in r] for r in Gn], dtype=np.int64)
if d <= 14:
    R = json.load(open(f"reps_d{d}.json"))["reps"]; X = np.array([r["x"] for r in R], dtype=np.int64)
else:
    X = np.concatenate([np.loadtxt(f"r{d}_out_{s}.txt", dtype=np.int64, ndmin=2).reshape(-1, 64) for s in range(12)])
M = X.dot(PE.T); e = M.sum(1); nu = (M > 0).sum(1); n1 = X.dot(F1r); n2 = X.dot(F2r)
c2 = np.einsum("ij,jk,ik->i", X, G64, X); mx = np.maximum(n1, n2)
def ok(g):
    hur = (e >= 2 * mx + 4 - 4 * g) & (c2 >= 2 * g - 2 - d)
    return hur, hur & (2 * nu >= e + 2 * mx - 4 * g + 4)
h0, u0 = ok(0); h1, u1 = ok(1)
ub = u0 | u1
print(f"d={d}: reps {len(X)}, unibranch-compatible {int(ub.sum())}, multibranch-only {int((~ub).sum())}")
print("  unibranch-compatible by C^2:", sorted(Counter(c2[ub].tolist()).items()))
np.save(f"ub_mask_d{d}.npy", ub)
