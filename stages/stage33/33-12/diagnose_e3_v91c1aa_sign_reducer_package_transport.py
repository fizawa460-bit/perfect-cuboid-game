#!/usr/bin/env python3
"""V91C1AA NONCREDIT literal-package transport for the V91C1Z reducers.

Act the A2_02 boundary-function packages by the exact coordinate sign changes
sign_a2 and sign_b1 selected by V91C1Z.  Test literal closure first against the
same eight A2_02 packages, then against the full retained package inventory.
No H2(mu2), Pic/2, or marked-Brauer fixedness is inferred from package matching
alone.
"""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOUNDARY = HERE / "boundary-function-generator-source-lock.json"
Z = HERE / "diagnose_e3_v91c1z_next_stabilizer_reducers.py"

BOUNDARY_SHA = "aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96"
Z_BLOB = "1a17331e2b939389075be2571e21c2619ea2d704"
COORD_NAMES = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
ACTIONS = {
    "sign_a2": [1, -1, 1, 1, 1, 1, 1],
    "sign_b1": [1, 1, 1, -1, 1, 1, 1],
}
EXPECTED_COMPONENTS = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def gitblob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


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
    out = ONE; base = x
    while n:
        if n & 1:
            out = qmul(out, base)
        base = qmul(base, base); n >>= 1
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


def act_signature(sig, signs):
    out = []
    for z, s in zip(sig, signs):
        if s == 1:
            out.append(list(z))
        else:
            out.append([-int(z[0]), int(z[1]), -int(z[2]), int(z[3])])
    return out


def package_data(package, signs=None):
    divisor = defaultdict(int)
    scalar = ONE
    for factor in package["numerator_factors"]:
        sig = factor["coefficients_Qi"]
        if signs is not None:
            sig = act_signature(sig, signs)
        norm, pivot = normalize_signature(sig)
        key = csha(norm)
        exponent = int(factor["exponent"])
        divisor[key] += exponent
        scalar = qmul(scalar, qpow(pivot, exponent))
    den = package["denominator"]
    sig = den["coefficients_Qi"]
    if signs is not None:
        sig = act_signature(sig, signs)
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
assert gitblob(Z.read_bytes()) == Z_BLOB

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

records = {}
for action, signs in ACTIONS.items():
    local = {}; global_hits = {}
    for cid, package in packages.items():
        acted_div, acted_scalar = package_data(package, signs)
        local[cid] = candidates_for(acted_div, acted_scalar, a2_inventory)
        global_hits[cid] = candidates_for(acted_div, acted_scalar, inventory)
    all_local = all(bool(local[cid]) for cid in EXPECTED_COMPONENTS)
    all_unique = all(len(local[cid]) == 1 for cid in EXPECTED_COMPONENTS)
    all_unit = all(
        len(local[cid]) == 1 and local[cid][0]["function_scalar_ratio_Qi"] == [1, 1, 0, 1]
        for cid in EXPECTED_COMPONENTS
    )
    permutation = all_unique and len({local[cid][0]["target_component"] for cid in EXPECTED_COMPONENTS}) == 8
    identity = all_unique and all(local[cid][0]["target_component"] == cid for cid in EXPECTED_COMPONENTS)
    records[action] = {
        "every_acted_package_has_a2_02_candidate": all_local,
        "every_acted_package_has_unique_a2_02_candidate": all_unique,
        "all_unique_candidate_scalar_ratios_one": all_unit,
        "literal_package_action_is_permutation_of_same_eight": permutation,
        "literal_package_action_is_identity": identity,
        "component_candidate_transport_within_a2_02": local,
        "global_candidate_counts": {cid: len(global_hits[cid]) for cid in EXPECTED_COMPONENTS},
    }

result = {
    "success": True,
    "marker": "V91C1AA_SIGN_REDUCER_LITERAL_PACKAGE_TRANSPORT",
    "actions": records,
    "component_count": 8,
    "retained_global_package_inventory_count": len(inventory),
    "literal_h2_seed_fixedness_materialized": False,
    "pic2_difference_computed": False,
    "actual_marked_brauer_image_computed": False,
    "credit": False,
}
print(json.dumps(result, sort_keys=True))
print(
    "::warning file=stages/stage33/33-12/diagnose_e3_v91c1aa_sign_reducer_package_transport.py,"
    "title=V91C1AA_SIGN_TRANSPORT::"
    + json.dumps(result, sort_keys=True, separators=(",", ":"))
)
