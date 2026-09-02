#!/usr/bin/env python3
"""Materialize the exact integral-correction torsor left by the v18 numerator."""
from __future__ import annotations

import hashlib
import itertools
import json
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
S07 = S33 / "33-07"
OUT = HERE / "j2-order4-integral-correction-torsor-v19.json"

LOCKS = {
    "v18": (HERE / "j2-order4-source-coordinate-v18.json", "a0378a7d7191d537347435d11002faa3692f91781dd15f53fe3063443e9d50d1"),
    "u1": (HERE / "j2-semantic-u1-full-surface-smith-source.json", "ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec"),
    "proper": (S07 / "proper-brauer2-from-discriminant.json", "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"),
    "target": (HERE / "full-surface-pic2-kummer-target.json", "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890"),
    "half_lift": (HERE / "j2-marked-order4-lift-label-gap.json", "4ca10da7ea214258dd57d1e42c2dc7ea7b66ae29c8cfd5b75ecd6a3eb0fd0101"),
    "glue_index": (S07 / "coordinate-k3-transcendental-glue-index.json", "0cc5321d02b56cea801b8def71a4c3b0946bd8011d8c30767a9602faba2fa8d8"),
}
BASE_SHA = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"


def csha(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


def rowmul(v, m):
    return [sum(v[k] * m[k][j] for k in range(len(v))) for j in range(len(m[0]))]


def rowmul_f2(v, m):
    return [sum((v[k] & 1) * (int(m[k][j]) & 1) for k in range(len(v))) & 1 for j in range(len(m[0]))]


def solve_retained(basis, target):
    found = []
    for bits in itertools.product((0, 1), repeat=len(basis)):
        v = [0] * len(target)
        for bit, row in zip(bits, basis):
            if bit:
                v = [a ^ (int(b) & 1) for a, b in zip(v, row)]
        if v == target:
            found.append(list(bits))
    assert len(found) == 1
    return found[0]


data = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
base = runpy.run_path(str(S07 / "picard_base_rows_retained.py"))["load"]()
assert base["canonical_sha256"] == BASE_SHA
G = [[int(x) for x in row] for row in base["picard_gram_64x64"]]
v18 = data["v18"]
n4 = [int(x) for x in v18["semantic_order4_numerator"]["weighted_fullPic64_historical_Magma_numerator"]]
raw_pairing = rowmul(n4, G)
assert raw_pairing == v18["semantic_order4_numerator"]["n4_times_picard_gram"]
assert all(x % 2 == 0 for x in raw_pairing) and any(x % 4 for x in raw_pairing)

# Seek r in Pic(S)/2 with (n4+2r)G = 0 mod 4, equivalently rG=b mod 2.
b = [(x // 2) & 1 for x in raw_pairing]
A = [[G[j][i] & 1 for j in range(64)] + [b[i]] for i in range(64)]
rank = 0
pivots = []
for col in range(64):
    pivot = next((i for i in range(rank, 64) if A[i][col]), None)
    if pivot is None:
        continue
    A[rank], A[pivot] = A[pivot], A[rank]
    for i in range(64):
        if i != rank and A[i][col]:
            A[i] = [x ^ y for x, y in zip(A[i], A[rank])]
    pivots.append(col)
    rank += 1
assert not any(not any(row[:-1]) and row[-1] for row in A)
free = [i for i in range(64) if i not in pivots]
assert rank == 50 and len(free) == 14

particular = [0] * 64
for i, col in enumerate(pivots):
    particular[col] = A[i][-1]
kernel = []
for f in free:
    x = [0] * 64
    x[f] = 1
    for i, col in enumerate(pivots):
        x[col] = A[i][f]
    assert rowmul_f2(x, G) == [0] * 64
    kernel.append(x)
assert rowmul_f2(particular, G) == b

u1 = data["u1"]
mods = u1["retained_common_smith_source"]["discriminant_moduli"]
C = u1["retained_common_smith_source"]["v_nontrivial_columns_mod8_64x14"]
b8 = u1["retained_common_smith_source"]["discriminant_bilinear_numerator_over_8_reduced"]
u1_mixed = u1["exact_normalization"]["nontrivial_smith_coordinates_mixed_moduli"]
scales = [m // 2 for m in mods]
proper = data["proper"]
basis10 = data["target"]["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]

mixed_seen = set()
functional_counts = {}
fixed_records = {}
for selector in itertools.product((0, 1), repeat=14):
    r = list(particular)
    for bit, basis_row in zip(selector, kernel):
        if bit:
            r = [x ^ y for x, y in zip(r, basis_row)]
    corrected = [x + 2 * y for x, y in zip(n4, r)]
    prod = rowmul(corrected, G)
    assert all(x % 4 == 0 for x in prod)
    z = [x // 4 for x in prod]
    y = tuple(sum(z[k] * C[k][j] for k in range(64)) % mods[j] for j in range(14))
    assert tuple((2 * y[j]) % mods[j] for j in range(14)) == tuple(u1_mixed)
    mixed_seen.add(y)
    pairing = [sum(y[i] * scales[j] * int(b8[i][j]) for i in range(14)) for j in range(14)]
    assert all(x % 4 == 0 for x in pairing)
    f = tuple((x // 4) & 1 for x in pairing)
    functional_counts[f] = functional_counts.get(f, 0) + 1
    if rowmul_f2(list(f), proper["proper_Br2_cc_action_f2"]) == list(f) and rowmul_f2(list(f), proper["proper_Br2_ct_action_f2"]) == list(f):
        if f not in fixed_records:
            coord10 = solve_retained(basis10, list(f))
            fixed_records[f] = {
                "proper14_f2": list(f),
                "proper14_mask_decimal": sum(bit << i for i, bit in enumerate(f)),
                "retained10_f2": coord10,
                "retained10_mask_decimal": sum(bit << i for i, bit in enumerate(coord10)),
            }

assert len(mixed_seen) == 16384
assert len(functional_counts) == 16
assert set(functional_counts.values()) == {1024}
fixed = sorted(fixed_records.values(), key=lambda x: x["retained10_mask_decimal"])
assert [x["retained10_mask_decimal"] for x in fixed] == [4, 5, 6, 7]
assert [x["proper14_mask_decimal"] for x in fixed] == [20, 22, 25, 27]
historical = data["half_lift"]["exact_enumeration"]
assert historical["half_lifts_total"] == len(mixed_seen)
assert historical["distinct_bilinear_proper_br2_functionals"] == len(functional_counts)
assert historical["half_lifts_per_joint_v4_fixed_functional"] == 1024
historical_fixed = [
    {k: rec[k] for k in ("proper14_f2", "proper14_mask_decimal", "retained10_f2", "retained10_mask_decimal")}
    for rec in historical["joint_v4_fixed_functionals"]
]
assert historical_fixed == fixed

glue = data["glue_index"]
assert glue["integral_glue"]["index_T_over_L0"] == 512
assert glue["integral_glue"]["actual_glue_subgroup_identified"] is False

out = {
    "schema": "STAGE33_12_J2_ORDER4_INTEGRAL_CORRECTION_TORSOR_V19",
    "stage": "33-12",
    "status": "PASS_EXACT_CORRECTION_TORSOR_MATERIALIZED_NAMED_ELEMENT_UNLABELED",
    "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
    "full_surface_picard_base_sha256": BASE_SHA,
    "integrality_equation": {
        "formula": "choose r in Pic(S)/2 so that (n4+2r)G_S is divisible by 4; equivalently rG_S=(n4G_S/2) mod 2",
        "right_hand_side_f2": b,
        "coefficient_rank_f2": rank,
        "solution_affine_dimension_f2": len(free),
        "solution_count": 1 << len(free),
        "rref_pivot_positions_1based": [x + 1 for x in pivots],
        "rref_free_positions_1based": [x + 1 for x in free],
        "canonical_free_zero_particular_correction_f2": particular,
        "canonical_particular_support_1based": [i + 1 for i, x in enumerate(particular) if x],
        "kernel_basis_f2_14x64": kernel,
    },
    "exact_enumeration": {
        "corrected_integral_order4_lifts": len(mixed_seen),
        "distinct_mixed_smith_half_lifts": len(mixed_seen),
        "every_lift_doubles_to_locked_semantic_u1": True,
        "distinct_proper14_functionals": len(functional_counts),
        "preimages_per_proper14_functional": 1024,
        "joint_cc_ct_fixed_functionals": fixed,
        "joint_cc_ct_fixed_retained10_masks": [4, 5, 6, 7],
        "unique_named_element_selected": False,
    },
    "glue_interpretation": {
        "degree_two_scaled_seven_piece_lattice": "L0=<8>^10 direct_sum <16>^4",
        "full_surface_overlattice_index": 512,
        "actual_labeled_index512_glue_known": False,
        "meaning": "The exact rows determine the affine correction torsor but not the point representing the Kc t1/4 component inside the actual integral full-surface glue.",
        "minimal_missing_object": "one source-locked 14-bit correction selector in this torsor, equivalently the labeled image of semantic Kc t1/4 in the actual index-512 glue/marked NS-T anti-isometry",
    },
    "anti_inference": {
        "historical_mask6_assumed": False,
        "s3_fixedness_used_to_select_label": False,
        "target_compatibility_used": False,
        "rep88_used_as_actual_integral_glue": False,
    },
    "promotion_firewall": {
        "mathematical_state_promotion_performed": False,
        "named_j2_source_coordinate_materialized": False,
        "first_75D_matrix_column_materialized": False,
        "finite_v4_kummer_columns_materialized": 0,
        "stage33_progress": "6/11",
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    },
}
out["canonical_sha256"] = csha(out)
if "--check" in sys.argv:
    assert locked(OUT, out["canonical_sha256"]) == out
else:
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "solution_count": out["integrality_equation"]["solution_count"],
    "fixed_retained10_masks": out["exact_enumeration"]["joint_cc_ct_fixed_retained10_masks"],
    "named_selected": False,
    "canonical_sha256": out["canonical_sha256"],
    "marker": "PROOF_REPLAY_COMPLETE",
}, sort_keys=True))
