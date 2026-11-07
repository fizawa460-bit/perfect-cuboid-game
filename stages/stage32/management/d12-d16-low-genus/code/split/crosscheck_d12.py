"""final cross-check d = 12: certified production run (old method, orbit reps per boundary vector) vs split method.
production inventory: (6,12) dropped; (6,16) c2 >= -12; g0 slices c2 >= -14; g1-only slices c2 >= -12."""
import json, sys
import numpy as np
REPO = "C:/Users/fizaw/claudework/perfect-cuboid-game"
sys.path.insert(0, REPO + "/stages/stage32/management/d10-low-genus/enumeration")
import slice_lib as L
L.load(REPO)
from flint import fmpq_mat, fmpq
Cn = L.D["Cn"]
prod = set(); statuses = {}
jobs_done = set()
for fn in ("results.jsonl", "results_wide.jsonl", "results_wide2.jsonl", "results_wide3.jsonl", "results_wide4.jsonl", "results_wide5.jsonl"):
    for l in open("../d12_run/" + fn):
        r = json.loads(l)
        st = r["status"].split()[0]
        statuses[st] = statuses.get(st, 0) + 1
        jobs_done.add(r["job"])
        for c in r.get("classes", []):
            prod.add(tuple(c))
import importlib.util
spec = importlib.util.spec_from_file_location("w", "../d12_run/run_d12_wide.py"); w = importlib.util.module_from_spec(spec); spec.loader.exec_module(w)
inv = set(w.inventory())
print("production statuses:", statuses, " distinct classes:", len(prod))
X = np.array(json.load(open("split_d12_v1.json"))["classes"], dtype=np.int64)
Gn64 = np.array(L.D["Gn"], dtype=np.int64)
F1 = np.array([int(v) for v in L.D["F1row"]], dtype=np.int64)
exc = np.array([int(v) for v in L.D["exc"]], dtype=np.int64)
n1 = X.dot(F1); e = X.dot(exc); c2 = np.einsum("ij,jk,ik->i", X, Gn64, X)
def in_prod_inv(a, b, c):
    # production rules, symmetric under the ruling swap (the swap-skipped orientation is the image of the kept one)
    n2 = 12 - a; M = max(a, n2); m = min(a, n2)
    if a < 1 or n2 < 1 or (a, b) == (6, 12): return False
    if 2 * M + 4 <= b <= 6 * m and (a, b) != (6, 16): return c >= -14
    if 2 * M <= b <= 6 * m: return c >= -12
    return False
keep = np.array([in_prod_inv(int(a), int(b), int(c)) for a, b, c in zip(n1, e, c2)])
Xp = X[keep]
sset = {tuple(r) for r in Xp.tolist()}
print("split classes in the production inventory:", len(sset))
print("production ⊆ split:", prod <= sset, " production not in split:", len(prod - sset))
# closure test: every lattice orbit of the split set (production inventory) must contain a production class
basis_idx, rk = [], 0
for k in range(140):
    T = fmpq_mat([[fmpq(int(v)) for v in Cn[j]] for j in basis_idx + [k]])
    if T.rank() > rk: basis_idx.append(k); rk += 1
    if rk == 64: break
Binv = fmpq_mat([[fmpq(int(v)) for v in Cn[k]] for k in basis_idx]).inv()
def qnp(p):
    Q = Binv * fmpq_mat([[fmpq(int(v)) for v in Cn[p[k]]] for k in basis_idx])
    return np.array([[int(Q[r, s].p) for s in range(64)] for r in range(64)], dtype=np.int64)
gens = [tuple(g) for g in json.load(open("../d12_run/symmetry_generators.json"))["generators"]]
Xl = list(sset); index = {x: i for i, x in enumerate(Xl)}; A = np.array(Xl, dtype=np.int64)
parent = list(range(len(Xl)))
def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]; a = parent[a]
    return a
for g in gens:
    Y = A.dot(qnp(g))
    for i in range(len(Xl)):
        j = index.get(tuple(Y[i]))
        assert j is not None, "split set (production inventory) not closed under the group"
        a, b = find(i), find(j)
        if a != b: parent[a] = b
orbits = {}
for i in range(len(Xl)): orbits.setdefault(find(i), []).append(i)
miss = [r for r, mem in orbits.items() if not any(Xl[i] in prod for i in mem)]
print("lattice orbits:", len(orbits), " orbits with no production class:", len(miss))
