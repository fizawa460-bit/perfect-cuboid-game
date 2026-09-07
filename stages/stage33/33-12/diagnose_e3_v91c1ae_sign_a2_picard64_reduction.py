#!/usr/bin/env python3
"""V91C1AE NONCREDIT exact Picard64/Pic2 reduction for sign_a2.

V91C1AB materializes the complete sign_a2 acted-minus-original strict and
exceptional divisor difference. V91C1AD proves that the eight strict primes
needed by that difference each have exactly one known92 locator. Here we
strengthen that preflight to exact canonical-ideal equality with known curves
1..8, attach their retained Picard64 rows, attach the frozen exceptional rows,
and reduce the complete difference mod 2.

No H2(mu2) seed fixedness is inferred here even if the Pic/2 class vanishes;
that semantic promotion remains a separate source-bound Kummer leaf.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
AB = HERE / "diagnose_e3_v91c1ab_sign_prime_attached_cech_difference.py"
AD = HERE / "diagnose_e3_v91c1ad_sign_a2_picard64_locator_preflight.py"
V = HERE / "diagnose_e3_v91c1v_actual_prime_known140_locator.py"
AB_BLOB = "d787830a712c6a0639fe35d6d57ba6c8cba39e90"
AD_BLOB = "4abb5a9dd7137f525d1167d82489e0eae6c4f6dc"
V_BLOB = "d2b0fabca7adb27eb63438499b8fd918eec5ff5e"
ACTION = "sign_a2"
COORD_INDEX = 1


def gitblob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def add64(*rows):
    out = [0] * 64
    for row in rows:
        for i, x in enumerate(row):
            out[i] += int(x)
    return out


def scale64(a, row):
    return [int(a) * int(x) for x in row]


assert gitblob(AB.read_bytes()) == AB_BLOB
assert gitblob(AD.read_bytes()) == AD_BLOB
assert gitblob(V.read_bytes()) == V_BLOB
abns = runpy.run_path(str(AB))
ab = abns["result"]
assert ab["success"] is True
siga2 = ab["actions"][ACTION]
assert siga2["needed_strict_prime_class_count"] == 8
assert siga2["acted_actual_primes_outside_retained_inventory_count"] == 0
assert siga2["full_codim1_package_difference_zero"] is False
needed = list(siga2["needed_strict_prime_ids"])
assert csha(needed) == siga2["needed_strict_prime_ids_sha256"]

# Recompute the exact sign_a2 package difference from V91C1AB's locked
# actual-prime namespace and literal exceptional valuations.
ens = abns["ens"]
variables = abns["variables"]
canonical_generators = abns["canonical_generators"]
strict_original = abns["strict_original"]
packages = abns["packages"]
EXPECTED_COMPONENTS = abns["EXPECTED_COMPONENTS"]
add = abns["add"]
subtract = abns["subtract"]
sum_vectors = abns["sum_vectors"]
act_expr = abns["act_expr"]
exceptional_vector = abns["exceptional_vector"]
exceptional_original = abns["exceptional_original"]

prime_action = {}
for pid, generators in canonical_generators.items():
    acted_generators = [act_expr(poly, COORD_INDEX) for poly in generators]
    image_id, _basis = ens["canonical_ideal"](acted_generators, variables)
    prime_action[pid] = image_id

strict_acted = {}
for cid, vector in strict_original.items():
    acted = {}
    for pid, coeff in vector.items():
        add(acted, prime_action[pid], coeff)
    strict_acted[cid] = dict(sorted(acted.items()))
strict_package_difference = subtract(
    sum_vectors(strict_acted.values()), sum_vectors(strict_original.values())
)
assert sorted(strict_package_difference) == needed
assert csha(strict_package_difference) == siga2["strict_package_difference_sha256"]

exceptional_acted = {
    cid: exceptional_vector(pkg, COORD_INDEX) for cid, pkg in packages.items()
}
exceptional_package_difference = subtract(
    sum_vectors(exceptional_acted.values()), sum_vectors(exceptional_original.values())
)
assert len(exceptional_package_difference) == siga2["exceptional_package_difference_nonzero_coefficients"] == 16
assert csha(exceptional_package_difference) == siga2["exceptional_package_difference_sha256"]

# Strengthen V91C1AD's unique containment signal to exact canonical-ideal
# equality with the first eight known curves, then use only those exact rows.
vns = runpy.run_path(str(V))
kns = vns["kns"]
known = kns["known"]
known_generators = vns["known_generators"]
assert len(known) == 140 and len(known_generators) >= 92

known_id_to_index = {}
for j in range(8):
    kid, _basis = ens["canonical_ideal"](known_generators[j], variables)
    if kid in known_id_to_index:
        raise SystemExit(f"duplicate known canonical id among first 8: {kid}")
    known_id_to_index[kid] = j + 1
assert set(known_id_to_index) == set(needed)
strict_locator = {pid: known_id_to_index[pid] for pid in needed}
assert sorted(strict_locator.values()) == list(range(1, 9))

strict_picard64 = [0] * 64
for pid, coeff in strict_package_difference.items():
    j = strict_locator[pid]
    strict_picard64 = add64(strict_picard64, scale64(coeff, known[j - 1]))

# Frozen Stage33 exceptional locator: EXC_j is known140 class 92+j.
exceptional_picard64 = [0] * 64
exceptional_locator = {}
for eid, coeff in exceptional_package_difference.items():
    assert eid.startswith("EXC_")
    j = int(eid.split("_")[1])
    known_index_1based = 92 + j
    assert 93 <= known_index_1based <= 140
    exceptional_locator[eid] = known_index_1based
    exceptional_picard64 = add64(
        exceptional_picard64, scale64(coeff, known[known_index_1based - 1])
    )

full = add64(strict_picard64, exceptional_picard64)
mod2 = [x & 1 for x in full]
support = [i + 1 for i, x in enumerate(mod2) if x]

result = {
    "success": True,
    "credit": False,
    "marker": "V91C1AE_SIGN_A2_PICARD64_REDUCTION",
    "sign_a2_strict_prime_count": len(needed),
    "strict_prime_exact_known92_locator_materialized": True,
    "strict_prime_known92_indices_1based": strict_locator,
    "strict_prime_known92_index_set": sorted(strict_locator.values()),
    "exceptional_locator_materialized": True,
    "exceptional_locator_known140_indices_1based": exceptional_locator,
    "strict_package_picard64_row": strict_picard64,
    "exceptional_package_picard64_row": exceptional_picard64,
    "complete_sign_a2_difference_picard64_row": full,
    "complete_sign_a2_difference_mod2_row": mod2,
    "complete_sign_a2_difference_mod2_support_one_based": support,
    "sign_a2_pic2_difference_computed": True,
    "sign_a2_pic2_difference_zero": not support,
    "sign_a2_literal_h2_seed_fixedness_promoted": False,
    "actual_marked_brauer_image_computed": False,
    "stage33_progress": "6/11",
}
print(json.dumps(result, sort_keys=True))
print(
    "::warning file=stages/stage33/33-12/diagnose_e3_v91c1ae_sign_a2_picard64_reduction.py,"
    "title=V91C1AE_SIGN_A2_PIC2::"
    + json.dumps({
        "strict_known_indices": result["strict_prime_known92_index_set"],
        "support": support,
        "zero": not support,
    }, sort_keys=True, separators=(",", ":"))
)
