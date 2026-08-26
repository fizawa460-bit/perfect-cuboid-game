#!/usr/bin/env python3
"""Integrate the exact K1/K2/K3 geometric prefixes without promoting actual glue or HS descent."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def verify_canonical(doc, label):
    body = dict(doc)
    stored = body.pop("canonical_sha256", None)
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if stored != got:
        raise SystemExit(f"{label} canonical hash regression: stored={stored} got={got}")
    return stored


k1 = load("nonelementary-k1-geometric-sign-fixed-p7-rescue128-census.json")
k2 = load("nonelementary-k2-geometric-full-q4-retained.json")
k3 = load("nonelementary-k3-full-q4-retained.json")
lock = load("k1-geometric-sign-fixed-evidence-lock.json")
handoff = load("handoff.json")

k1_sha = verify_canonical(k1, "K1")
k2_sha = verify_canonical(k2, "K2")
k3_wrapper_sha = hashlib.sha256(
    json.dumps(k3, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()

if lock["certificate_canonical_sha256"] != k1_sha or lock["workflow_conclusion"] != "success":
    raise SystemExit("K1 evidence lock regression")
if lock["old32_required_and_downloaded"] != 448 or lock["p7_required_and_downloaded"] != 128:
    raise SystemExit("K1 source partition lock regression")
if lock["mathematical_recomputation_performed"] or lock["new_intermediate_artifacts_uploaded"] != 0:
    raise SystemExit("K1 recovery/storage firewall regression")

want_partition = {str(p): (128 if p == 7 else 32) for p in range(15)}
if k1["partition_count_by_P_orbit"] != want_partition:
    raise SystemExit("K1 mixed partition regression")
if not k1["all_14x32_old_and_P7x128_rescue_subshards_present_exactly_once"]:
    raise SystemExit("K1 exact coverage regression")
if k1["support_skeleton_count"] != 20487593 or k1["weighted_H_checked"] != 1311205952:
    raise SystemExit("K1 predecessor total regression")
if sum(k1["rejection_counts"].values()) + k1["representative_section_survivors"] != k1["representative_lift_sections_checked"]:
    raise SystemExit("K1 rejection accounting regression")
if not k1["k1_nonelementary_type_rejected"] or k1["representative_section_survivors"] != 0 or k1["weighted_H_survivors"] != 0:
    raise SystemExit("K1 exact rejection regression")

if k2["input_support_orbit_count"] != 1496:
    raise SystemExit("K2 source orbit regression")
if k2["full_Q4_rejected_orbit_count"] + k2["full_Q4_surviving_orbit_count"] != 1496:
    raise SystemExit("K2 orbit accounting regression")
if not k2["all_orbits_full_survival_or_full_rejection"] or not k2["full_Q4_condition_certified_for_k2"]:
    raise SystemExit("K2 exact Q4 prefix regression")
if k2["full_Q4_surviving_orbit_count"] != 867 or k2["full_Q4_surviving_weighted_structural_H"] != 517873664:
    raise SystemExit("K2 survivor regression")

if k3["abstract_H_type"] != "(Z/4)^3 direct_sum (Z/2)^3":
    raise SystemExit("K3 abstract type regression")
if not k3["k3_abstract_type_rejected"] or k3["t1_q4_survivor_count"] != 0:
    raise SystemExit("K3 exact rejection regression")
if not k3["all_16_prefix_shards_green"] or not k3["aggregate_green"] or k3["fast_or_heuristic_traversal_used"]:
    raise SystemExit("K3 exactness regression")

for label, doc in (("K1", k1), ("K2", k2), ("K3", k3), ("lock", lock)):
    if doc.get("actual_index512_glue_identified") or doc.get("arithmetic_HS_closed"):
        raise SystemExit(f"{label} glue/HS promotion firewall regression")
    if doc.get("stage33_progress") != "6/11":
        raise SystemExit(f"{label} Stage33 progress regression")
    if doc.get("endpoint_credit"):
        raise SystemExit(f"{label} endpoint-credit firewall regression")

if handoff["unit_status"] != "BLOCKED_NEW_KERNEL" or handoff["unit_closed"] or handoff["downstream_released"]:
    raise SystemExit("formal Stage33-07 state regression")
if handoff["new_kernel_id"] != "R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT":
    raise SystemExit("formal Stage33-07 kernel regression")

cert = {
    "schema": "STAGE33_07_NONELEMENTARY_K123_GEOMETRIC_INTEGRATION_V1",
    "source_locks": {
        "k1_canonical_sha256": k1_sha,
        "k1_workflow_run_id": lock["workflow_run_id"],
        "k1_artifact_id": lock["artifact_id"],
        "k1_artifact_zip_digest": lock["artifact_zip_digest"],
        "k2_canonical_sha256": k2_sha,
        "k3_retained_wrapper_sha256": k3_wrapper_sha,
        "k3_source_certificate_canonical_sha256": k3["certificate_canonical_sha256"],
    },
    "abstract_non_elementary_types": {
        "K1": "Z/4 direct_sum (Z/2)^7",
        "K2": "(Z/4)^2 direct_sum (Z/2)^5",
        "K3": "(Z/4)^3 direct_sum (Z/2)^3",
    },
    "exact_geometric_prefix": {
        "K1": {"status": "REJECTED", "surviving_representative_sections": 0, "surviving_weighted_H": 0},
        "K2": {"status": "SURVIVES_PREFIX", "surviving_orbits": 867, "surviving_weighted_H": 517873664},
        "K3": {"status": "REJECTED", "surviving_representative_sections": 0},
    },
    "rejected_non_elementary_types": ["K1", "K3"],
    "remaining_non_elementary_types": ["K2"],
    "remaining_non_elementary_type_count": 1,
    "geometric_abstract_type_reduction_does_not_identify_actual_glue": True,
    "actual_index512_glue_identified": False,
    "arithmetic_HS_closed": False,
    "current_blocking_kernel_id": handoff["new_kernel_id"],
    "next_exact_leaf": k2["next_exact_leaf"],
    "unit_status": "BLOCKED_NEW_KERNEL",
    "unit_closed": False,
    "downstream_released": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "stage33_09_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
raw = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(raw).hexdigest()
(HERE / "nonelementary-k123-geometric-integration.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "rejected_types": cert["rejected_non_elementary_types"],
    "remaining_types": cert["remaining_non_elementary_types"],
    "k2_surviving_orbits": cert["exact_geometric_prefix"]["K2"]["surviving_orbits"],
    "actual_index512_glue_identified": False,
    "arithmetic_HS_closed": False,
    "stage33_progress": "6/11",
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
