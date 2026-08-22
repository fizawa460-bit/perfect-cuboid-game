#!/usr/bin/env python3
"""Build the exact Stage30-07 eight-defect transport table."""
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
OUT = HERE / "defect-classification.json"


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


def bit_perm(bits, perm):
    out = [0, 0, 0]
    for i, j in enumerate(perm):
        out[j] = bits[i]
    return tuple(out)


# Concrete residual PSL2(Z/4), in the same canonical order used by Stage30-06C.
SL4 = [
    ((a, b), (c, d))
    for a, b, c, d in product(range(4), repeat=4)
    if (a * d - b * c) % 4 == 1
]
G4 = sorted({canon(M, 4) for M in SL4})
assert len(SL4) == 48 and len(G4) == 24

S4 = canon(((0, 3), (1, 0)), 4)
T4 = canon(((1, 1), (0, 1)), 4)
S2 = tuple(tuple(x % 2 for x in row) for row in S4)
T2 = tuple(tuple(x % 2 for x in row) for row in T4)

# Source X(8): residual S swaps u,v and residual T swaps v,w.
for a, b, c in product((0, 1), repeat=3):
    A = ((a, b), (c, a))
    assert phi(conj2(S2, A)) == bit_perm(phi(A), (1, 0, 2))
    assert phi(conj2(T2, A)) == bit_perm(phi(A), (0, 2, 1))

rows = []
for a, b, c in product((0, 1), repeat=3):
    A = ((a, b), (c, a))
    bits = phi(A)
    defect_id = f"K8-{a}{b}{c}"
    kappa = [[(1 + 4 * a) % 8, (4 * b) % 8], [(4 * c) % 8, (1 + 4 * a) % 8]]

    orbit = set()
    stabilizer = []
    for idx, g4 in enumerate(G4):
        g2 = tuple(tuple(x % 2 for x in row) for row in g4)
        image = conj2(g2, A)
        orbit.add(image)
        if image == A:
            stabilizer.append(f"g{idx:02d}")

    if A == ((0, 0), (0, 0)):
        legacy_class = "zero"
    elif A == ((1, 0), (0, 1)):
        legacy_class = "identity"
    elif det2(A) == 0:
        legacy_class = "nonzero_det0"
    else:
        legacy_class = "det1_nonidentity"

    weight = sum(bits)
    sign_names = [name for bit, name in zip(bits, ("u", "v", "w")) if bit]
    endpoint_names = [name for bit, name in zip(bits, ("b1", "b2", "b3")) if bit]

    # sigma transport is trivial: D=diag(1,-1) is I modulo 2, and
    # conjugation of I+4A modulo 8 depends only on D modulo 2.
    sigma_image = defect_id

    rows.append({
        "defect_id": defect_id,
        "A_f2": [list(A[0]), list(A[1])],
        "kappa_mod8": kappa,
        "legacy_stage29_ordinary_class": legacy_class,
        "ordinary_s4_orbit_id": f"ORB-W{weight}",
        "ordinary_s4_orbit_size": len(orbit),
        "stabilizer_order": len(stabilizer),
        "stabilizer_ids": stabilizer,
        "sigma_image": sigma_image,
        "g0_sign_bits": {"u": bits[0], "v": bits[1], "w": bits[2]},
        "qi_representative": "identity" if not sign_names else "flip_{" + ",".join(sign_names) + "}",
        "endpoint_adapter_image": "identity" if not endpoint_names else "delta_{" + ",".join(endpoint_names) + "}",
        "q_descent_class": f"QDC-{defect_id}",
        "arithmetic_equivalence_status": "MARKED_SINGLETON_DISTINCT",
        "eliminated": False,
    })

assert len(rows) == 8
assert sorted(row["ordinary_s4_orbit_size"] for row in rows) == [1, 1, 3, 3, 3, 3, 3, 3]
assert {row["ordinary_s4_orbit_id"] for row in rows} == {"ORB-W0", "ORB-W1", "ORB-W2", "ORB-W3"}
assert len({row["q_descent_class"] for row in rows}) == 8
assert all(row["sigma_image"] == row["defect_id"] for row in rows)
assert sum(row["eliminated"] for row in rows) == 0

payload = {
    "schema": "STAGE30_07_EIGHT_K8_DEFECT_TRANSPORT_V1",
    "stage": "30-07",
    "source_receiver": "R29-KUM5",
    "k8_order": 8,
    "residual_s4_order": 24,
    "adapter_formula": "phi([[a,b],[c,a]])=(a+b,a+c,a) on (u,v,w), hence (b1,b2,b3)",
    "ordinary_orbit_sizes": [1, 3, 3, 1],
    "ordinary_orbit_interpretation": "Hamming weights 0,1,2,3 of endpoint b-sign pattern",
    "marked_q_descent_class_count": 8,
    "sigma_action_on_k8": "TRIVIAL",
    "defect_elimination_count": 0,
    "rows": rows,
    "firewalls": {
        "ordinary_s4_orbit_equals_marked_arithmetic_class": False,
        "coordinate_cocycle_equals_kappa": False,
        "k8_equals_v_mod": False,
        "physical_endpoint_exclusion_proved": False,
        "r29_kum5_discharged": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("K8_ORDER=8")
print("ORDINARY_ORBIT_SIZES=1,3,3,1")
print("MARKED_Q_DESCENT_CLASS_COUNT=8")
print("SIGMA_ACTION_ON_K8=TRIVIAL")
print("DEFECT_ELIMINATION_COUNT=0")
print("PASS")
