#!/usr/bin/env python3
"""Independent exact verifier for Stage30-07 defect transport."""
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
DATA = HERE / "defect-classification.json"
ACTION = ROOT / "stages/stage30/30-02C/action-tables.json"


def require(c, m):
    if not c:
        raise AssertionError(m)


def mm(A, B, n):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % n for j in range(2)) for i in range(2))


def neg(A, n):
    return tuple(tuple((-x) % n for x in row) for row in A)


def canon(A, n):
    return min(A, neg(A, n))


def inv2(A):
    return ((A[1][1] % 2, (-A[0][1]) % 2), ((-A[1][0]) % 2, A[0][0] % 2))


def conj2(g, A):
    return mm(mm(g, A, 2), inv2(g), 2)


def det2(A):
    return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 2


def phi(A):
    a, b, c = A[0][0], A[0][1], A[1][0]
    return ((a + b) % 2, (a + c) % 2, a)


def pcompose(left, right):
    return tuple(left[right[i]] for i in range(3))


def papply(bits, perm):
    out = [0, 0, 0]
    for i, j in enumerate(perm):
        out[j] = bits[i]
    return tuple(out)


payload = json.loads(DATA.read_text(encoding="utf-8"))
require(payload["schema"] == "STAGE30_07_EIGHT_K8_DEFECT_TRANSPORT_V1", "wrong schema")
rows = payload["rows"]
require(len(rows) == 8, "classification does not contain eight rows")

# Reconstruct concrete residual PSL2(Z/4) and verify Task-A label order.
SL4 = [
    ((a, b), (c, d))
    for a, b, c, d in product(range(4), repeat=4)
    if (a * d - b * c) % 4 == 1
]
G4 = sorted({canon(M, 4) for M in SL4})
require(len(SL4) == 48 and len(G4) == 24, "wrong residual group order")
idx = {g: i for i, g in enumerate(G4)}
mul = [[idx[canon(mm(a, b, 4), 4)] for b in G4] for a in G4]
e = idx[canon(((1, 0), (0, 1)), 4)]
s = idx[canon(((0, 3), (1, 0)), 4)]
t = idx[canon(((1, 1), (0, 1)), 4)]

action = json.loads(ACTION.read_text(encoding="utf-8"))
require([r["id"] for r in action["modular"]["elements"]] == [f"g{i:02d}" for i in range(24)], "Task-A IDs mismatch")
for i, row in enumerate(action["modular"]["elements"]):
    frozen = tuple(tuple(x for x in line) for line in row["matrix"])
    require(frozen == G4[i], f"Task-A matrix mismatch at g{i:02d}")

# Source-derived sign-coordinate action: S swaps u,v; T swaps v,w.
perms = {e: (0, 1, 2)}
queue = [e]
for g in queue:
    for h, ph in ((s, (1, 0, 2)), (t, (0, 2, 1))):
        hg = mul[h][g]
        candidate = pcompose(ph, perms[g])
        if hg not in perms:
            perms[hg] = candidate
            queue.append(hg)
        else:
            require(perms[hg] == candidate, "inconsistent source S3 action")
require(len(perms) == 24, "S,T did not cover residual S4")
require(len(set(perms.values())) == 6, "residual action on sign bits is not S3")

expected = {}
for a, b, c in product((0, 1), repeat=3):
    A = ((a, b), (c, a))
    did = f"K8-{a}{b}{c}"
    bits = phi(A)
    orbit = set()
    stabilizer = []
    for gi, g4 in enumerate(G4):
        g2 = tuple(tuple(x % 2 for x in line) for line in g4)
        image = conj2(g2, A)
        orbit.add(image)
        require(phi(image) == papply(bits, perms[gi]), f"adapter is not equivariant at {did}/g{gi:02d}")
        if image == A:
            stabilizer.append(f"g{gi:02d}")

    if A == ((0, 0), (0, 0)):
        legacy = "zero"
    elif A == ((1, 0), (0, 1)):
        legacy = "identity"
    elif det2(A) == 0:
        legacy = "nonzero_det0"
    else:
        legacy = "det1_nonidentity"

    names = [name for bit, name in zip(bits, ("u", "v", "w")) if bit]
    bnames = [name for bit, name in zip(bits, ("b1", "b2", "b3")) if bit]
    expected[did] = {
        "A_f2": [list(A[0]), list(A[1])],
        "kappa_mod8": [[(1 + 4*a) % 8, (4*b) % 8], [(4*c) % 8, (1 + 4*a) % 8]],
        "legacy_stage29_ordinary_class": legacy,
        "ordinary_s4_orbit_id": f"ORB-W{sum(bits)}",
        "ordinary_s4_orbit_size": len(orbit),
        "stabilizer_order": len(stabilizer),
        "stabilizer_ids": stabilizer,
        "sigma_image": did,
        "g0_sign_bits": {"u": bits[0], "v": bits[1], "w": bits[2]},
        "qi_representative": "identity" if not names else "flip_{" + ",".join(names) + "}",
        "endpoint_adapter_image": "identity" if not bnames else "delta_{" + ",".join(bnames) + "}",
        "q_descent_class": f"QDC-{did}",
        "arithmetic_equivalence_status": "MARKED_SINGLETON_DISTINCT",
        "eliminated": False,
    }

by_id = {row["defect_id"]: row for row in rows}
require(set(by_id) == set(expected), "defect IDs mismatch")
for did, exp in expected.items():
    got = dict(by_id[did])
    got.pop("defect_id")
    require(got == exp, f"stored row mismatch for {did}")

# Direct sigma check with D=diag(1,-1) modulo 8.
def inv_mod8_diag_D(M):
    # D^-1=D for diag(1,-1).
    D = ((1, 0), (0, 7))
    return mm(mm(D, M, 8), D, 8)

for row in rows:
    M = tuple(tuple(x for x in line) for line in row["kappa_mod8"])
    require(inv_mod8_diag_D(M) == M, f"sigma is not trivial on {row['defect_id']}")

require(sorted({r["ordinary_s4_orbit_id"] for r in rows}) == ["ORB-W0", "ORB-W1", "ORB-W2", "ORB-W3"], "wrong ordinary orbit set")
require(len({r["q_descent_class"] for r in rows}) == 8, "marked classes collapsed")
require(all(r["arithmetic_equivalence_status"] == "MARKED_SINGLETON_DISTINCT" for r in rows), "non-singleton marked class")
require(sum(bool(r["eliminated"]) for r in rows) == 0, "a defect was improperly eliminated")
require(payload["ordinary_orbit_sizes"] == [1, 3, 3, 1], "ordinary orbit summary mismatch")
require(payload["marked_q_descent_class_count"] == 8, "marked class count mismatch")
require(payload["defect_elimination_count"] == 0, "elimination count mismatch")

print("K8_DEFECT_ROWS=8")
print("RESIDUAL_S4_ORDER=24")
print("SOURCE_SIGN_IMAGE_ORDER=6")
print("ALL24_ADAPTER_EQUIVARIANCE=PASS")
print("ORDINARY_S4_ORBIT_SIZES=1,3,3,1")
print("MARKED_Q_DESCENT_CLASS_COUNT=8")
print("SIGMA_ACTION_ON_K8=TRIVIAL")
print("DEFECT_ELIMINATION_COUNT=0")
print("PASS")
