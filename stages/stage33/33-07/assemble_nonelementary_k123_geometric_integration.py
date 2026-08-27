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
k2_sign = load("nonelementary-k2-geometric-sign-fixed-census.json")
k3 = load("nonelementary-k3-full-q4-retained.json")
k1_lock = load("k1-geometric-sign-fixed-evidence-lock.json")
k2_q2_lock = load("k2-geometric-q2-affine-evidence-lock.json")
k2_sign_lock = load("k2-geometric-sign-fixed-evidence-lock.json")
handoff = load("handoff.json")

k1_sha = verify_canonical(k1, "K1")
k2_sha = verify_canonical(k2, "K2")
k2_sign_sha = verify_canonical(k2_sign, "K2 sign census")
k3_wrapper_sha = hashlib.sha256(
    json.dumps(k3, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()

if k1_lock["certificate_canonical_sha256"] != k1_sha or k1_lock["workflow_conclusion"] != "success":
    raise SystemExit("K1 evidence lock regression")
if k1_lock["old32_required_and_downloaded"] != 448 or k1_lock["p7_required_and_downloaded"] != 128:
    raise SystemExit("K1 source partition lock regression")
if k1_lock["mathematical_recomputation_performed"] or k1_lock["new_intermediate_artifacts_uploaded"] != 0:
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
if k2_q2_lock["source_Q4_retained_sha256"] != k2_sha:
    raise SystemExit("K2 Q2-affine source lock regression")
if k2_q2_lock["certificate_canonical_sha256"] != "f9dd684e2813acdbec07fc59575d9d487828c97f6fa8f111983fec5a6fe6b9b0":
    raise SystemExit("K2 Q2-affine certificate lock regression")
if not k2_q2_lock["local_exact_reproduction_performed"] or k2_q2_lock["new_actions_run_launched"]:
    raise SystemExit("K2 Q2-affine reproduction firewall regression")
if (k2_q2_lock["Q2_profile_surviving_orbit_families"],
        k2_q2_lock["Q2_profile_surviving_representative_sections"],
        k2_q2_lock["Q2_profile_surviving_weighted_H"]) != (867, 2183168, 129468416):
    raise SystemExit("K2 Q2-affine total regression")
if k2_sign_lock["source_Q2_affine_certificate_canonical_sha256"] != k2_q2_lock["certificate_canonical_sha256"]:
    raise SystemExit("K2 sign census source lock regression")
if k2_sign_lock["certificate_canonical_sha256"] != k2_sign_sha:
    raise SystemExit("K2 sign census certificate lock regression")
if k2_sign_lock["shard_count"] != 64 or not k2_sign_lock["all_shard_artifacts_downloaded"]:
    raise SystemExit("K2 sign census shard coverage regression")
if not k2_sign_lock["all_shard_canonical_hashes_verified"] or not k2_sign_lock["local_exact_reaggregation_performed"]:
    raise SystemExit("K2 sign census reaggregation regression")
if (k2_sign["representative_sections_checked"], k2_sign["weighted_H_checked"]) != (2183168, 129468416):
    raise SystemExit("K2 sign census total regression")
if set(map(int, k2_sign["shard_certificate_sha256"])) != set(range(64)):
    raise SystemExit("K2 sign census shard identity regression")
if k2_sign["manifest_sha256"] != k2_sign_lock["manifest_canonical_sha256"]:
    raise SystemExit("K2 sign census manifest lock regression")
if sum(k2_sign["rejection_layers"].values()) + k2_sign["representative_section_survivors"] != 2183168:
    raise SystemExit("K2 sign census partition regression")
if (not k2_sign["k2_nonelementary_type_rejected_by_geometric_sign_fixed_filtration"]
        or k2_sign["representative_section_survivors"] != 0
        or k2_sign["weighted_H_survivors"] != 0):
    raise SystemExit("K2 exact rejection regression")

if k3["abstract_H_type"] != "(Z/4)^3 direct_sum (Z/2)^3":
    raise SystemExit("K3 abstract type regression")
if not k3["k3_abstract_type_rejected"] or k3["t1_q4_survivor_count"] != 0:
    raise SystemExit("K3 exact rejection regression")
if not k3["all_16_prefix_shards_green"] or not k3["aggregate_green"] or k3["fast_or_heuristic_traversal_used"]:
    raise SystemExit("K3 exactness regression")

for label, doc in (("K1", k1), ("K2", k2), ("K2 sign census", k2_sign), ("K3", k3),
                   ("K1 lock", k1_lock), ("K2 Q2 lock", k2_q2_lock),
                   ("K2 sign lock", k2_sign_lock)):
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
    "schema": "STAGE33_07_NONELEMENTARY_K123_GEOMETRIC_INTEGRATION_V2",
    "source_locks": {
        "k1_canonical_sha256": k1_sha,
        "k1_workflow_run_id": k1_lock["workflow_run_id"],
        "k1_artifact_id": k1_lock["artifact_id"],
        "k1_artifact_zip_digest": k1_lock["artifact_zip_digest"],
        "k2_full_Q4_canonical_sha256": k2_sha,
        "k2_Q2_affine_canonical_sha256": k2_q2_lock["certificate_canonical_sha256"],
        "k2_sign_census_canonical_sha256": k2_sign_sha,
        "k2_sign_workflow_run_id": k2_sign_lock["workflow_run_id"],
        "k2_sign_aggregate_artifact_id": k2_sign_lock["aggregate_artifact_id"],
        "k2_sign_aggregate_artifact_zip_digest": k2_sign_lock["aggregate_artifact_zip_digest"],
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
        "K2": {
            "status": "REJECTED",
            "full_Q4_surviving_orbits_before_Q2_and_signs": 867,
            "Q2_affine_representative_sections_checked_by_sign_census": 2183168,
            "weighted_H_checked_by_sign_census": 129468416,
            "surviving_representative_sections": 0,
            "surviving_weighted_H": 0,
        },
        "K3": {"status": "REJECTED", "surviving_representative_sections": 0},
    },
    "rejected_non_elementary_types": ["K1", "K2", "K3"],
    "remaining_non_elementary_types": [],
    "remaining_non_elementary_type_count": 0,
    "geometric_abstract_type_reduction_does_not_identify_actual_glue": True,
    "actual_index512_glue_identified": False,
    "arithmetic_HS_closed": False,
    "current_blocking_kernel_id": handoff["new_kernel_id"],
    "next_exact_leaf": handoff["next_item"],
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
    "k2_checked_sections": cert["exact_geometric_prefix"]["K2"]["Q2_affine_representative_sections_checked_by_sign_census"],
    "actual_index512_glue_identified": False,
    "arithmetic_HS_closed": False,
    "stage33_progress": "6/11",
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
