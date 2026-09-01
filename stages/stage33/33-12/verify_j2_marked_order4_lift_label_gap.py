#!/usr/bin/env python3
"""Verify the exact source-side ambiguity for the named J2 order-4 lift.

This verifier deliberately does not use the raw 75D target or V4-extension
compatibility to choose a source label.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEGACY = HERE.parent / "33-07"
CERT = HERE / "j2-marked-order4-lift-label-gap.json"
U1 = HERE / "j2-semantic-u1-full-surface-smith-source.json"
PROPER = LEGACY / "proper-brauer2-from-discriminant.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"
ROUTE = HERE / "j2-marked-adapter-source-route-audit.json"
GLUE_GAP = HERE / "j2-marked-glue-geometric-sign-route-gap.json"
ENUMERATOR = HERE / "certify_j2_order4_half_lift_functional_space.py"

LOCKS = {
    U1: "ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec",
    PROPER: "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
    TARGET: "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890",
    ROUTE: "5fec609e3ee75fddc3833124dde81f75514de6ca8600200e594366e30022f3f8",
    GLUE_GAP: "23b6fc3e9cf666e81f0c11c4c57c7070a1cc4c459c35515a6d934db3a84f3ee9",
}
ENUMERATOR_BLOB = "a62218b7fe34fa3fa536dd6f20b9ada28b1d46a3"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj


def git_blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def rowmul(v, matrix):
    return [sum((int(v[i]) & 1) * (int(matrix[i][j]) & 1) for i in range(len(v))) & 1 for j in range(len(matrix[0]))]


def solve10(basis, target):
    for bits in itertools.product((0, 1), repeat=10):
        value = [0] * 14
        for bit, row in zip(bits, basis):
            if bit:
                value = [a ^ (int(b) & 1) for a, b in zip(value, row)]
        if value == target:
            return list(bits)
    return None


cert = json.loads(CERT.read_text(encoding="utf-8"))
cert_body = dict(cert)
cert_claimed = cert_body.pop("canonical_sha256")
assert cert_claimed == csha(cert_body)
u1 = locked(U1)
proper = locked(PROPER)
target = locked(TARGET)
route = locked(ROUTE)
glue_gap = locked(GLUE_GAP)
assert git_blob(ENUMERATOR) == ENUMERATOR_BLOB

assert route["exact_route_audit"]["index512_glue_route"]["current_actual_labeled_glue_subgroup_identified"] is False
assert glue_gap["exact_findings"]["actual_labeled_glue_generator_set_identified"] is False
assert cert["source_locks"] == {
    "half_lift_enumerator_git_blob_sha1": ENUMERATOR_BLOB,
    "marked_adapter_source_route_audit_sha256": LOCKS[ROUTE],
    "marked_glue_geometric_sign_route_gap_sha256": LOCKS[GLUE_GAP],
    "proper_brauer2_sha256": LOCKS[PROPER],
    "retained_10D_target_basis_sha256": LOCKS[TARGET],
    "semantic_u1_full_surface_smith_source_sha256": LOCKS[U1],
}

mods = u1["retained_common_smith_source"]["discriminant_moduli"]
y2 = u1["exact_normalization"]["nontrivial_smith_coordinates_mixed_moduli"]
b8 = u1["retained_common_smith_source"]["discriminant_bilinear_numerator_over_8_reduced"]
assert mods == [2] * 4 + [4] * 6 + [8] * 4
choices = [[x for x in range(m) if (2 * x) % m == value] for value, m in zip(y2, mods)]
assert all(len(x) == 2 for x in choices)

functionals = {}
fixed = {}
divisibility_failures = 0
for w in itertools.product(*choices):
    numerators = [sum(w[i] * (mods[j] // 2) * int(b8[i][j]) for i in range(14)) for j in range(14)]
    if any(value % 4 for value in numerators):
        divisibility_failures += 1
        continue
    functional = tuple((value // 4) & 1 for value in numerators)
    functionals[functional] = functionals.get(functional, 0) + 1
    if rowmul(functional, proper["proper_Br2_cc_action_f2"]) == list(functional) and rowmul(functional, proper["proper_Br2_ct_action_f2"]) == list(functional):
        qnum = sum(int(w[i]) * int(w[j]) * int(b8[i][j]) for i in range(14) for j in range(14)) % 16
        record = fixed.setdefault(functional, {"count": 0, "qnums": {}})
        record["count"] += 1
        record["qnums"][qnum] = record["qnums"].get(qnum, 0) + 1

basis10 = target["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]
rows = []
for functional, record in fixed.items():
    retained = solve10(basis10, list(functional))
    assert retained is not None
    rows.append({
        "proper14_f2": list(functional),
        "proper14_mask_decimal": sum(bit << i for i, bit in enumerate(functional)),
        "quadratic_numerator_mod16": next(iter(record["qnums"])),
        "retained10_f2": retained,
        "retained10_mask_decimal": sum(bit << i for i, bit in enumerate(retained)),
    })
    assert record == {"count": 1024, "qnums": {12: 1024}}
rows.sort(key=lambda row: row["retained10_mask_decimal"])

exact = cert["exact_enumeration"]
assert exact["half_lifts_total"] == 16384
assert exact["half_lifts_per_joint_v4_fixed_functional"] == 1024
assert divisibility_failures == exact["pairing_divisibility_failures"] == 0
assert len(functionals) == exact["distinct_bilinear_proper_br2_functionals"] == 16
assert len(fixed) == exact["joint_v4_fixed_functional_count"] == 4
assert rows == exact["joint_v4_fixed_functionals"]
assert [row["retained10_mask_decimal"] for row in rows] == [4, 5, 6, 7]
assert exact["q_equals_one_half_filter_survivors"] == 0

gap = cert["exact_gap"]
assert gap["current_constraints_determine_unique_functional"] is False
assert gap["historical_mask6_is_only_one_of_four_current_source_side_candidates"] is True
fw = cert["promotion_firewall"]
assert fw["candidate_retained_masks_4_5_6_7_promoted"] is False
assert fw["historical_mask6_restored"] is False
assert fw["raw_75D_target_used_to_choose_source_label"] is False
assert fw["marked_adapter_materialized"] is False

print(json.dumps({
    "success": True,
    "status": cert["status"],
    "half_lifts": 16384,
    "distinct_functionals": 16,
    "joint_v4_fixed_retained_masks": [4, 5, 6, 7],
    "q_equals_one_half_survivors": 0,
    "minimal_positive_datum": cert["minimal_positive_datum"]["for_named_j2_row"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
