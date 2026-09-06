#!/usr/bin/env python3
"""Exact source-bound diagnostic for the V91C1Q swap12-swap13-swap12 word.

Act on the retained A2_02 boundary-function packages in their literal seven-
coordinate Q(i) linear-form representation.  First test literal closure on the
same eight A2_02 packages; then fingerprint every acted package against the
full retained 14-generator / 134-package function inventory.

This does NOT identify equal 26D residue coordinates with equal H^2(mu_2)
classes and does NOT infer a Brauer coordinate.  Failure of literal closure
means that an explicit Pic/2/Cech correction is still required.
"""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
BOUNDARY = HERE / "boundary-function-generator-source-lock.json"
SWAP_SOURCE = S33 / "33-11d" / "stage33-11d-source-lock.json"
SWAP_VERIFIER = S33 / "33-11d" / "verify_stage33_11d_prime_refinement.py"
Q_DIAG = HERE / "diagnose_e3_v91c1q_shortest_mask20_moving_stabilizer_word.py"

BOUNDARY_SHA = "aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96"
SWAP_SOURCE_SHA = "a7989a2e0bd58371f7eb4692a5f905c55007606d01b6b364f25558823ca52852"
SWAP_VERIFIER_BLOB = "764f9f8d27fc15df326a6145cbd73290235d3a79"
Q_DIAG_BLOB = "1b83812cec6473f04de0e3cf7e2b70bfb47de409"
WORD = ["swap12", "swap13", "swap12"]
COORD_NAMES = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
EXPECTED_COMPONENTS = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


def git_blob_sha(data: bytes):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def qi(z):
    return Fraction(z[0], z[1]), Fraction(z[2], z[3])


ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))


def qmul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def qinv(x):
    d = x[0] * x[0] + x[1] * x[1]
    assert d
    return x[0] / d, -x[1] / d


def qpow(x, n):
    if n < 0:
        return qpow(qinv(x), -n)
    out = ONE
    base = x
    while n:
        if n & 1:
            out = qmul(out, base)
        base = qmul(base, base)
        n >>= 1
    return out


def qenc(x):
    return [x[0].numerator, x[0].denominator, x[1].numerator, x[1].denominator]


def normalize_signature(raw):
    vals = [qi(z) for z in raw]
    pivot = next((x for x in vals if x != ZERO), None)
    assert pivot is not None
    inv = qinv(pivot)
    normalized = [qenc(qmul(x, inv)) for x in vals]
    return normalized, pivot


def compose_perm(perms, word):
    v = list(range(7))
    for name in word:
        p = perms[name]
        v = [v[j] for j in p]
    return v


def permute_signature(sig, perm):
    return [sig[j] for j in perm]


def package_data(package, perm=None):
    divisor = defaultdict(int)
    scalar = ONE
    for factor in package["numerator_factors"]:
        sig = factor["coefficients_Qi"]
        if perm is not None:
            sig = permute_signature(sig, perm)
        norm, pivot = normalize_signature(sig)
        key = csha(norm)
        exponent = int(factor["exponent"])
        divisor[key] += exponent
        scalar = qmul(scalar, qpow(pivot, exponent))
    den = package["denominator"]
    sig = den["coefficients_Qi"]
    if perm is not None:
        sig = permute_signature(sig, perm)
    norm, pivot = normalize_signature(sig)
    key = csha(norm)
    exponent = int(den["exponent"])
    divisor[key] -= exponent
    scalar = qmul(scalar, qpow(pivot, -exponent))
    return tuple(sorted((k, v) for k, v in divisor.items() if v)), scalar


def candidates_for(acted_div, acted_scalar, inventory):
    out = []
    for rec in inventory:
        if acted_div != rec["divisor"]:
            continue
        ratio = qmul(acted_scalar, qinv(rec["scalar"]))
        out.append({
            "source_direction": rec["source_direction"],
            "target_component": rec["component_id"],
            "kind": rec["kind"],
            "function_scalar_ratio_Qi": qenc(ratio),
        })
    return sorted(out, key=lambda x: (x["source_direction"], x["target_component"], x["kind"]))


boundary = load(BOUNDARY, BOUNDARY_SHA)
swap_source = load(SWAP_SOURCE, SWAP_SOURCE_SHA)
assert git_blob_sha(SWAP_VERIFIER.read_bytes()) == SWAP_VERIFIER_BLOB
assert git_blob_sha(Q_DIAG.read_bytes()) == Q_DIAG_BLOB
verifier_text = SWAP_VERIFIER.read_text(encoding="utf-8")
assert 'COORD_NAMES = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]' in verifier_text
perms = swap_source["certified_actions"]
assert perms["swap12"] == [1, 0, 2, 4, 3, 5, 6]
assert perms["swap13"] == [2, 1, 0, 5, 4, 3, 6]
perm = compose_perm(perms, WORD)
assert perm == [0, 2, 1, 3, 5, 4, 6]

row = next(r for r in boundary["generator_records"] if r["source_direction"] == "A2_02")
assert row["raw_order"] == 2
packages = {p["component_id"]: p for p in row["component_packages"]}
assert sorted(packages) == sorted(EXPECTED_COMPONENTS)

inventory = []
for grow in boundary["generator_records"]:
    for package in grow["component_packages"]:
        div, scalar = package_data(package)
        inventory.append({
            "source_direction": grow["source_direction"],
            "component_id": package["component_id"],
            "kind": package["kind"],
            "divisor": div,
            "scalar": scalar,
        })
assert len(inventory) == 134

a2_inventory = [x for x in inventory if x["source_direction"] == "A2_02"]
transport = {}
global_transport = {}
all_candidates = True
all_unique = True
all_unit = True
for cid, package in packages.items():
    acted_div, acted_scalar = package_data(package, perm)
    local_candidates = candidates_for(acted_div, acted_scalar, a2_inventory)
    global_candidates = candidates_for(acted_div, acted_scalar, inventory)
    transport[cid] = local_candidates
    global_transport[cid] = global_candidates
    all_candidates &= bool(local_candidates)
    all_unique &= len(local_candidates) == 1
    all_unit &= bool(local_candidates) and all(x["function_scalar_ratio_Qi"] == [1, 1, 0, 1] for x in local_candidates)

literal_identity = all_unique and all(
    transport[cid][0]["target_component"] == cid for cid in EXPECTED_COMPONENTS
)
literal_permutation = all_unique and len({transport[cid][0]["target_component"] for cid in EXPECTED_COMPONENTS}) == len(EXPECTED_COMPONENTS)
global_candidate_counts = {cid: len(global_transport[cid]) for cid in EXPECTED_COMPONENTS}
side_global_candidates = {cid: global_transport[cid] for cid in EXPECTED_COMPONENTS if cid.startswith("SIDE_")}

result = {
    "success": True,
    "marker": "V91C1R_SWAP23_LITERAL_BOUNDARY_FUNCTION_PACKAGE_TRANSPORT_DIAGNOSTIC",
    "q_word": WORD,
    "coordinate_order": COORD_NAMES,
    "composed_coordinate_permutation": perm,
    "composed_coordinate_action": "a2<->a3,b2<->b3,a1/b1/c fixed",
    "retained_global_package_inventory_count": len(inventory),
    "a2_02_component_count": len(packages),
    "every_acted_package_has_original_a2_02_divisor_candidate": all_candidates,
    "every_acted_package_has_unique_original_a2_02_divisor_candidate": all_unique,
    "all_candidate_function_scalar_ratios_one": all_unit,
    "literal_package_action_is_identity": literal_identity,
    "literal_package_action_is_permutation_of_same_eight": literal_permutation,
    "component_candidate_transport_within_a2_02": transport,
    "global_candidate_counts": global_candidate_counts,
    "side_component_global_candidate_transport": side_global_candidates,
    "pic2_cech_correction_computed": False,
    "seed_fixed_mod_pic2": False,
    "a2_02_marked_brauer_image_excluded_from_mask20": False,
    "credit": False,
}
print(json.dumps(result, sort_keys=True))
print(
    "::warning file=stages/stage33/33-12/diagnose_e3_v91c1r_swap23_boundary_function_package_transport.py,"
    "title=V91C1R_SWAP23_PACKAGE_TRANSPORT::"
    + "all_candidates=" + str(all_candidates).lower()
    + ";literal_permutation=" + str(literal_permutation).lower()
    + ";side_global_counts=" + ",".join(f"{k}:{global_candidate_counts[k]}" for k in EXPECTED_COMPONENTS if k.startswith("SIDE_"))
)
