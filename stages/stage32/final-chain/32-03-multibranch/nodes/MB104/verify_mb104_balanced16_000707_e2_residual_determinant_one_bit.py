#!/usr/bin/env python3
import hashlib
import itertools
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
PASS = "PASS STAGE32_MB104_000707_E2_RESIDUAL_DETERMINANT_ONE_BIT_V1"
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-DETERMINANT-ONE-BIT.md",
        "c0e89e66afee11bbba39fa8bce20019a664fa8dc",
    ),
    "CONDUCTOR_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-CONDUCTOR-DETERMINANT-REDUCTION-CERTIFICATE.json",
        "1623eba91f97e9ed56db26cd6320c85c4e6b08a5",
    ),
    "EXPLICIT_BASIS_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-G-FIXED-JACOBIAN-EXPLICIT-BASIS-CERTIFICATE.json",
        "f6f925ed221d4b11c78d53f9c2e9a0ff76033298"
    ),
    "G_FIXED_VERIFIER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_e2_g_fixed_jacobian_torsion.py",
        "07e54f9f5eb5c01f17dcdd099aada75ef6e95716",
    ),
}


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def repo_root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def f2_rank(rows):
    a = [r[:] for r in rows]
    if not a:
        return 0
    rank = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][c] & 1), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(len(a)):
            if i != rank and (a[i][c] & 1):
                a[i] = [x ^ y for x,y in zip(a[i], a[rank])]
        rank += 1
    return rank


def f2_nullspace(matrix):
    a = [row[:] for row in matrix]
    m = len(a)
    n = len(a[0])
    pivots = []
    rank = 0
    for c in range(n):
        pivot = next((i for i in range(rank,m) if a[i][c] & 1), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(m):
            if i != rank and (a[i][c] & 1):
                a[i] = [x ^ y for x,y in zip(a[i], a[rank])]
        pivots.append(c)
        rank += 1
    free = [c for c in range(n) if c not in pivots]
    out = []
    for f in free:
        v = [0]*n
        v[f] = 1
        for i,c in enumerate(pivots):
            if a[i][f] & 1:
                v[c] = 1
        out.append(v)
    return out


def mat_vec_mod2(m, v):
    return [sum(row[j]*v[j] for j in range(len(v))) & 1 for row in m]


root = repo_root()
for name,(rel,expected) in LOCKS.items():
    p = root / rel
    req(p.is_file(), f"missing lock {name}: {rel}")
    got = blob_sha1(p)
    req(got == expected, f"SOURCE_LOCK_FAIL {name}: {got} != {expected}")

note = (root / LOCKS["HUMAN_NOTE"][0]).read_text(encoding="utf-8")
cond = json.loads((root / LOCKS["CONDUCTOR_CERT"][0]).read_text(encoding="utf-8"))
explicit = json.loads((root / LOCKS["EXPLICIT_BASIS_CERT"][0]).read_text(encoding="utf-8"))
req(cond.get("active_leaf") == ACTIVE, "conductor active leaf")
req(cond.get("H_fixed_determinant_group", {}).get("size") == 64, "H fixed size 64")
req(explicit.get("deduction", {}).get("J_C8_G_fixed_structure") == "(Z/2)^5", "G fixed structure")

for token in [
    "dim ker(N_res)=5",
    "dim im(N_res)=1",
    "kappa = tau1 + tau5",
    "im(T-1) = {0,kappa}",
    "No e=2 closure is claimed",
]:
    req(token in note, f"semantic token missing: {token}")

ns = runpy.run_path(str(root / LOCKS["G_FIXED_VERIFIER"][0]), run_name="stage32_mb104_gfixed_parent")
q = ns["q"]
eye = ns["eye"]
msub = ns["msub"]
transpose = ns["transpose"]

# Point coordinates are half-lattice column vectors; fixedness is tested by
# (Q-I)^T on their mod-two numerators.
def diff_matrix(h):
    return [[x & 1 for x in row] for row in transpose(msub(q[h], eye(10)))]

M1 = diff_matrix((1,0,0))
M2 = diff_matrix((0,1,0))
M3 = diff_matrix((0,0,1))
BH = M1 + M2
BG = M1 + M2 + M3
H_basis = f2_nullspace(BH)
G_basis = f2_nullspace(BG)
req(len(H_basis) == 6, "H fixed F2 dimension")
req(len(G_basis) == 5, "G fixed F2 dimension")

images = [mat_vec_mod2(M3, v) for v in H_basis]
nonzero = [v for v in images if any(v)]
req(f2_rank(nonzero) == 1, "residual T-1 image rank one")
unique_nonzero = {tuple(v) for v in nonzero}
req(len(unique_nonzero) == 1, "unique nonzero residual image vector")
kappa = list(next(iter(unique_nonzero)))
req(kappa == [1,1,0,1,1,1,0,1,1,0], "kappa numerator")

# Retained full-G basis numerators tau1,...,tau5.
taus = explicit["fixed_generators_mod2_numerators"]
req(len(taus) == 5 and f2_rank(taus) == 5, "explicit tau basis")
tau1_plus_tau5 = [(a ^ b) for a,b in zip(taus[0], taus[4])]
req(tau1_plus_tau5 == kappa, "kappa=tau1+tau5")

# Count fixed versus nonfixed H-fixed determinant classes directly.
def add_vec(a,b): return [x^y for x,y in zip(a,b)]
classes=[]
for coeffs in itertools.product([0,1], repeat=6):
    v=[0]*10
    for c,b in zip(coeffs,H_basis):
        if c:
            v=add_vec(v,b)
    classes.append(v)
fixed=sum(1 for v in classes if not any(mat_vec_mod2(M3,v)))
req(len(classes)==64, "64 H fixed classes")
req(fixed==32, "32 residual-fixed determinant classes")
req((64-fixed)//2==16, "16 nontrivial residual orbits")

print(PASS)
