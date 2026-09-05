#!/usr/bin/env python3
"""Verify the exact V88 direct-Cech seed construction contract.

V88 is deliberately a non-credit narrowing leaf.  It extracts only the
reusable geometric layer of the corrected J2 literal-Cech construction and
keeps every e3 lift/column/closure firewall closed until a source-specific
mask20 seed is actually materialized and residue-audited.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "e3-direct-cech-seed-contract-v88.json"


def csha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


v88 = load_json(CERT)
assert v88["schema"] == "stage33.e3.direct_cech_seed_contract.v88"
assert v88["canonical_sha256"] == "1d8f7b9478f48a3aa2137524180afea0a8e0bbf909e4ece04b1a07ee44d365b7"
assert csha(v88) == v88["canonical_sha256"]

# Fail-close every exact source blob named by the V88 contract.
for name, lock in v88["source_locks"].items():
    path = ROOT / lock["path"]
    assert path.is_file(), (name, path)
    assert git_blob_sha1(path) == lock["git_blob_sha1"], name
    if "canonical_sha256" in lock:
        obj = load_json(path)
        assert obj.get("canonical_sha256") == lock["canonical_sha256"], name
        assert csha(obj) == lock["canonical_sha256"], name

# Independent e3 target: exact mask20, not a J2 XOR reconstruction.
v41 = load_json(HERE / "e3-independent-proper14-source-v41.json")
target = v88["exact_target"]
assert target["adapted_basis_label"] == "e3"
assert target["proper14_mask_decimal"] == 20
assert target["proper14_coordinate_f2"] == [0,0,1,0,1,0,0,0,0,0,0,0,0,0]
assert target["retained10_standard_mask_decimal"] == 4
assert target["derived_from_j2_xor_split"] is False
assert v41["e3_source"]["proper14_mask_decimal"] == target["proper14_mask_decimal"]
assert v41["e3_source"]["proper14_coordinate_f2"] == target["proper14_coordinate_f2"]
assert v41["e3_source"]["derived_from_j2_xor_split"] is False

# Abstract Pic/2 cohomology still lacks the Kummer extension class, so it is
# not a substitute for a literal/source-bound e3 representative.
full = load_json(HERE / "full-surface-pic2-kummer-target.json")
assert full["canonical_sha256"] == "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890"
assert full["exact_information_boundary"]["kummer_extension_class_missing"] is True

# The corrected J2 example proves the layer ordering used by V88: the genuine
# geometric surface H2(mu2) lift is already materialized at the literal symbol
# + complete residue audit layer, while integral Pic/Galois-descent data remain
# open there. Later cc/ct overlap certificates therefore belong downstream.
j2 = load_json(HERE / "j2-corrected-explicit-cech-mu2-lift.json")
assert j2["schema"] == "STAGE33_12_J2_CORRECTED_EXPLICIT_CECH_MU2_LIFT_V1"
assert j2["explicit_cech_preimage"]["concrete_Cech_preimage_e_D_materialized"] is True
assert j2["explicit_cech_preimage"]["class"] == "e_D={f2,g22}=kum(f2) cup kum(g22) in H^2(Ubar,mu_2)"
assert j2["codimension_one_residue_audit"]["all_nonboundary_residues_zero"] is True
assert j2["resolution_residue_audit"]["all_exceptional_residues_zero"] is True
assert j2["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True
assert j2["surface_mu2_lift"]["brauer_image"] == "corrected nonzero J2=(f2,1)"
assert j2["exact_information_boundary"]["pic_mod2_defect_1cocycle_materialized"] is False
assert j2["exact_information_boundary"]["integral_Pic_lift_materialized"] is False

cc = load_json(HERE / "j2-cc-actual-cech-global-square-overlap.json")
ct = load_json(HERE / "j2-ct-actual-cech-overlap-parities-and-marked-pic-mod2.json")
assert cc["exact_information_boundary"]["actual_cc_cech_overlap_transition_materialized"] is True
assert ct["exact_information_boundary"]["actual_ct_overlap_determinant_parities_materialized"] is True
assert v88["template_extraction"]["arithmetic_galois_overlap_not_required_for_current_geometric_lift"] is True

# V87 remains route-local and supplies no ready exact mask20 Gersten class.
v87 = load_json(HERE / "e3-legacy-gersten-mask20-source-binding-gap-v87.json")
assert v87["canonical_sha256"] == "c7daf46a4e05d4692f1065e8ed677d5be9a172126952e93207a26d5b2c839447"
assert v87["exact_legacy_pipeline_status"]["exact_connecting_columns_certified"] == 0
assert v87["exact_conclusion"]["global_H2_mu2_nonexistence_claim"] is False
assert v87["exact_conclusion"]["route_local_only"] is True

neg = v88["bounded_negative_findings"]
assert neg["current_locked_chain_supplies_v88_seed"] is False
assert neg["full_surface_pic2_target_supplies_explicit_kummer_extension_class"] is False
assert neg["legacy_stage33_11_supplies_ready_mask20_gersten_class"] is False
assert neg["proper14_axis_labels_3_and_5_supply_literal_geometry"] is False
assert neg["repo_wide_absence_claim"] is False
assert neg["mathematical_nonexistence_claim"] is False

contract = v88["v88_construction_contract"]
assert len(contract["accepted_seed_types"]) == 2
assert contract["success_postcondition"]["proper14_brauer_image_mask_decimal"] == 20
assert contract["success_postcondition"]["genuine_full_surface_h2_mu2_lift_for_e3"] is True
assert contract["success_postcondition"]["q_defined_descent_credit"] == "not granted by this contract"

fw = v88["credit_firewall"]
for key in (
    "e3_kummer_column_materialized",
    "e3_literal_cech_preimage_materialized",
    "endpoint_credit",
    "genuine_full_surface_h2_mu2_lift_for_e3",
    "merge_allowed",
    "receiver_credit",
    "stage33_12_closed_exact",
    "stage33_13_released",
    "theorem_credit",
):
    assert fw[key] is False, key
assert fw["stage33_progress"] == "6/11"
assert v88["status"] == "PASS_EXACT_V88_DIRECT_CECH_SEED_CONTRACT_CURRENT_SEED_UNMATERIALIZED"
assert v88["next_exact_leaf"] == "V88A_CONSTRUCT_ONE_SOURCE_BOUND_LITERAL_GEOMETRIC_SEED_FOR_E3_MASK20_THEN_RESIDUE_AUDIT_ITS_FULL_SURFACE_H2_MU2_REPRESENTATIVE"

print(json.dumps({
    "success": True,
    "marker": "V88_DIRECT_CECH_SEED_CONTRACT_REPLAY_COMPLETE",
    "canonical_sha256": v88["canonical_sha256"],
    "e3_target_mask": 20,
    "current_seed_materialized": False,
    "geometric_lift_gate_requires_arithmetic_cc_ct_first": False,
    "next_exact_leaf": v88["next_exact_leaf"],
    "stage33_progress": "6/11",
    "merge_allowed": False,
}, sort_keys=True))
