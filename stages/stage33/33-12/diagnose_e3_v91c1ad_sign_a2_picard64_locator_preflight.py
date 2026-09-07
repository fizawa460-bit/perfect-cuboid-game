#!/usr/bin/env python3
"""V91C1AD NONCREDIT locator preflight for the eight sign_a2 strict primes.

V91C1AB proves that sign_a2 leaves only EXC_003/004 nonzero and that all eight
strict-prime IDs needed by the complete package difference remain inside the
retained actual-prime inventory. This preflight asks, for those exact eight
IDs only, which already source-bound V91C1V/W Picard64 resolution forms apply:
known92 component decomposition and/or a multiplicity-one carrier relation.
No Pic/2 or H2 fixedness is promoted here.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
AB = HERE / "diagnose_e3_v91c1ab_sign_prime_attached_cech_difference.py"
V = HERE / "diagnose_e3_v91c1v_actual_prime_known140_locator.py"
W_CERT = HERE / "e3-v91c1w-a2-02-all8-picard64-reduction.json"
AB_BLOB = "d787830a712c6a0639fe35d6d57ba6c8cba39e90"
V_BLOB = "d2b0fabca7adb27eb63438499b8fd918eec5ff5e"
W_CERT_SHA = "e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7"


def gitblob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


assert gitblob(AB.read_bytes()) == AB_BLOB
assert gitblob(V.read_bytes()) == V_BLOB
wcert = load(W_CERT, W_CERT_SHA)
assert wcert["exact_result"]["strict_scheme_count"] == 8
assert wcert["exact_result"]["strict_scheme_picard64_classes_materialized"] is True
assert wcert["exact_result"]["all_eight_exact_decomposition_or_source_bound_relation"] is True

abns = runpy.run_path(str(AB)); ab = abns["result"]
assert ab["success"] is True
siga2 = ab["actions"]["sign_a2"]
assert siga2["acted_actual_primes_outside_retained_inventory_count"] == 0
assert siga2["needed_strict_prime_class_count"] == 8
needed = list(siga2["needed_strict_prime_ids"])
assert csha(needed) == siga2["needed_strict_prime_ids_sha256"]

vns = runpy.run_path(str(V))
sns = vns["sns"]
canonical_generators = sns["canonical_generators"]
old_to_canonical = sns["old_to_canonical"]
prime_records = sns["prime_records"]
carrier_refinements = sns["e11"]["prime_inventory"]["carrier_refinements"]
assert all(p in canonical_generators for p in needed)
canonical_to_old = {}
for old, cid in old_to_canonical.items():
    canonical_to_old.setdefault(cid, []).append(old)
for olds in canonical_to_old.values():
    olds.sort()

# Only query the pinned V91C1V known92 geometry for the exact sign_a2 set.
matches = {
    p: vns["contained_known_classes"](canonical_generators[p])
    for p in needed
}

# Record exact retained provenance and candidate total-transform relations.
records = {}
for p in needed:
    olds = canonical_to_old.get(p, [])
    recs = [prime_records[o] for o in olds]
    carriers = []
    for carrier_id, pieces in carrier_refinements.items():
        for piece in pieces:
            if old_to_canonical[piece["prime_id"]] == p:
                carriers.append({
                    "carrier_id": carrier_id,
                    "piece_count": len(pieces),
                    "target_multiplicity": int(piece["multiplicity"]),
                    "single_multiplicity_one_candidate": len(pieces) == 1 and int(piece["multiplicity"]) == 1,
                    "piece_prime_ids": [q["prime_id"] for q in pieces],
                })
    records[p] = {
        "known92_component_matches_1based": matches[p],
        "known92_component_match_count": len(matches[p]),
        "retained_old_prime_ids": olds,
        "retained_record_kinds": sorted({r["kind"] for r in recs}),
        "carrier_relation_candidates": sorted(carriers, key=lambda r: r["carrier_id"]),
        "has_single_multiplicity_one_carrier_relation": any(r["single_multiplicity_one_candidate"] for r in carriers),
    }

# V91C1V's exact swap23-needed ID set is precisely the eight objects that
# V91C1W certifies as Picard64-resolved. Reuse only exact ID overlap.
swap23_needed = set(vns["needed"])
assert len(swap23_needed) == 8
overlap = sorted(set(needed) & swap23_needed)
zero_match = sorted(p for p in needed if not matches[p])
nonzero_match = sorted(p for p in needed if matches[p])
sole_carrier = sorted(p for p in needed if records[p]["has_single_multiplicity_one_carrier_relation"])

result = {
    "success": True,
    "credit": False,
    "marker": "V91C1AD_SIGN_A2_PICARD64_LOCATOR_PREFLIGHT",
    "needed_strict_prime_count": len(needed),
    "needed_strict_prime_ids_sha256": csha(needed),
    "v91c1w_certificate_sha256": W_CERT_SHA,
    "already_resolved_by_exact_v91c1w_id_overlap_count": len(overlap),
    "already_resolved_by_exact_v91c1w_id_overlap": overlap,
    "known92_nonzero_match_count": len(nonzero_match),
    "known92_zero_match_count": len(zero_match),
    "known92_match_count_histogram": {
        str(k): sum(len(matches[p]) == k for p in needed)
        for k in sorted({len(matches[p]) for p in needed})
    },
    "single_multiplicity_one_carrier_relation_candidate_count": len(sole_carrier),
    "single_multiplicity_one_carrier_relation_candidates": sole_carrier,
    "records": records,
    "picard64_rows_materialized_for_sign_a2": False,
    "sign_a2_pic2_difference_computed": False,
    "sign_a2_literal_h2_seed_fixed": False,
    "actual_marked_brauer_image_computed": False,
}
print(json.dumps(result, sort_keys=True))
print(
    "::warning file=stages/stage33/33-12/diagnose_e3_v91c1ad_sign_a2_picard64_locator_preflight.py,"
    "title=V91C1AD_SIGN_A2_LOCATORS::"
    + json.dumps({
        "overlap": len(overlap),
        "nonzero_matches": len(nonzero_match),
        "zero_matches": len(zero_match),
        "sole_carrier": len(sole_carrier),
        "histogram": result["known92_match_count_histogram"],
    }, sort_keys=True, separators=(",", ":"))
)
