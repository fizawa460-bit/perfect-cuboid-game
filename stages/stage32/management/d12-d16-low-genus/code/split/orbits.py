"""32R-61: orbits of the full d-class set under the lattice group (6144, used by the certified runs) and the geometric
group (1536, Stoll's 9 substitutions), by union-find over generator images. Output orbit representatives with sizes."""
import sys, json, time
import numpy as np
REPO = "C:/Users/fizaw/claudework/perfect-cuboid-game"
sys.path.insert(0, REPO + "/stages/stage32/management/d10-low-genus/enumeration")
import slice_lib as L
L.load(REPO)
Cn = L.D["Cn"]
from flint import fmpq_mat, fmpq
d = int(sys.argv[1])
X = np.load(f"split_d{d}.npy").astype(np.int64)  # int8 on disk since 32R-64
print("classes", len(X), flush=True)
basis_idx, rk = [], 0
for k in range(140):
    T = fmpq_mat([[fmpq(int(v)) for v in Cn[j]] for j in basis_idx + [k]])
    if T.rank() > rk:
        basis_idx.append(k); rk += 1
    if rk == 64: break
Binv = fmpq_mat([[fmpq(int(v)) for v in Cn[k]] for k in basis_idx]).inv()
def qnp(p):
    Q = Binv * fmpq_mat([[fmpq(int(v)) for v in Cn[p[k]]] for k in basis_idx])
    return np.array([[int(Q[r, s].p) for s in range(64)] for r in range(64)], dtype=np.int64)
lat_gens = [tuple(g) for g in json.load(open("../d12_run/symmetry_generators.json"))["generators"]]
geo_gens = [tuple(p) for p in json.load(open("../stoll/geo_perms.json"))["perms"]]
V = np.dtype((np.void, 64 * 8))
Xv = np.ascontiguousarray(X).view(V).ravel()
ordr = np.argsort(Xv, kind="stable"); Xs = Xv[ordr]
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
def uf_orbits(gens):
    I, J = [], []
    for g in gens:
        Q = qnp(g)
        Y = np.ascontiguousarray(X.dot(Q)).view(V).ravel()
        pos = np.searchsorted(Xs, Y)
        pos[pos >= len(Xs)] = 0
        if not np.all(Xs[pos] == Y):
            raise SystemExit("class set not closed under the group")
        I.append(np.arange(len(X))); J.append(ordr[pos])
    I = np.concatenate(I); J = np.concatenate(J)
    G = coo_matrix((np.ones(len(I), dtype=np.int8), (I, J)), shape=(len(X), len(X)))
    nc, lab = connected_components(G, directed=True, connection="weak")
    first = {}
    orbs = [[] for _ in range(nc)]
    for i, l in enumerate(lab): orbs[l].append(i)
    return orbs
t0 = time.time()
lat = uf_orbits(lat_gens); print("lattice-group orbits:", len(lat), f"{time.time()-t0:.0f}s", flush=True)
geo = uf_orbits(geo_gens); print("geometric-group orbits:", len(geo), f"{time.time()-t0:.0f}s", flush=True)
Gn = np.array(L.D["Gn"], dtype=np.int64)
reps = []
for orb in geo:
    x = X[min(orb)]
    reps.append({"x": [int(v) for v in x], "orbit": len(orb), "C2": int(x.dot(Gn).dot(x))})
json.dump({"d": d, "classes": len(X), "lattice_orbits": len(lat), "reps": reps}, open(f"reps_d{d}.json", "w"))
from collections import Counter
print("geometric reps by C^2:", sorted(Counter(r["C2"] for r in reps).items()))
