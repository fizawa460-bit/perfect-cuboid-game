#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state with V58 repeatable bounded-search override."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "33-12"
ROOT = H.parent.parent
OUT = H / "MAIN-STATE.json"
RETIRED_HANDOFF = H / "MAIN-BATCH-HANDOFF.md"
V41 = D / "j2-post-v39-arsenal-first-bounded-search-policy-v41.json"
V57 = D / "e3-mask20-b1-gysin-image-gate-v57.json"
V58 = D / "e3-search-routing-supersession-v58.json"
RESEARCH_POLICY = ROOT / "docs/research-os/policies/repository-asset-discovery.md"
ARSENAL = ROOT / "docs/arsenal/index.json"
REMAINING = ["e3", "e1", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]
INHERITED_NEXT = "ARSENAL_FIRST_THEN_ONE_BOUNDED_SEARCH_THEN_CONSTRUCT_OR_REQUEST_USER_AUTHORIZATION"
CONTROLLER_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"
V41_SHA = "32b2ad7da0ad7ced22bd3d27ebc3abec36ed9d8fe037a4e2c676e3e44471a6f8"
LOCKS = {
    "v25": (D / "j2-genuine-h2-mu2-kummer-adapter-v25.json", "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
    "v33": (D / "j2-current-hs-d2-nonzero-v33.json", "59385430d2806fd600006b8bee1e02170f28d0a598912555d1e905e556c84b8f"),
    "v34": (D / "j2-adapted-first-kummer-column-v34.json", "eb53bd545626efe3b32d407eccd2788e991494203acd718d88100ee7233b909e"),
}
EMPTY_CHECKPOINT = {"status": "EMPTY", "authority": "OPERATIONAL_ONLY_NOT_PROOF"}

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def locked(path, expected):
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj

ap = argparse.ArgumentParser()
ap.add_argument("--check", action="store_true")
a = ap.parse_args()

assert not RETIRED_HANDOFF.exists(), "MAIN-BATCH-HANDOFF.md is retired"
assert not (ROOT / "docs/evidence-locator").exists(), "retired evidence-locator directory must stay absent"
assert RESEARCH_POLICY.is_file() and ARSENAL.is_file()
rp = RESEARCH_POLICY.read_text()
assert "Stage16 and later" in rp and "Stages12–15" in rp and "## Arsenal" in rp
arsenal = json.loads(ARSENAL.read_text())
assert str(arsenal.get("schema", "")).startswith("RESEARCH_ARSENAL_")

p41 = locked(V41, V41_SHA)
r41 = p41["routing_contract"]
assert r41["one_automatic_bounded_repository_search_after_arsenal_miss"] is True
assert p41["anti_loop"]["automatic_bounded_search_budget_per_missing_object"] == 1
assert r41["arsenal_miss_proves_repository_absence"] is False
assert r41["bounded_search_miss_proves_repository_absence"] is False

p58 = json.loads(V58.read_text())
assert p58["schema"] == "stage33.search_routing_supersession.v58"
assert p58["role"] == "OPERATIONAL_ROUTING_ONLY_NO_MATHEMATICAL_CHANGE"
r58 = p58["routing_contract"]
assert r58["arsenal_first"] is True
assert r58["fixed_per_object_search_count_cap"] is None
assert r58["repeated_bounded_repository_search_allowed"] is True
assert r58["search_miss_proves_repository_absence"] is False
assert r58["search_miss_proves_mathematical_nonexistence"] is False
assert "unlimited or open-ended repository search" in r58["forbidden"]
assert p58["credit_firewall"]["genuine_full_surface_h2_mu2_lift_for_e3"] is False
assert p58["credit_firewall"]["merge_allowed"] is False

p57 = json.loads(V57.read_text())
assert p57["schema"] == "stage33.e3.mask20_b1_gysin_image_gate.v57"
assert p57["exact_b1_route_geometry"]["branch_H1_total_dimension_f2"] == 4
assert p57["exact_b1_route_geometry"]["proper_geometric_Br2_dimension_f2"] == 14
assert p57["exact_b1_route_geometry"]["required_marked_matrix_shape"] == [14, 4]
assert p57["e3_membership_gate"]["proper14_mask_decimal"] == 20
assert p57["e3_membership_gate"]["membership_in_im_Phi_B1"] == "OPEN_NOT_COMPUTED"
assert p57["next_exact_leaf"] == "MATERIALIZE_EXACT_B1_BRANCH_H1_TO_PROPER14_PHI_MATRIX_AND_SOLVE_E3_MASK20_MEMBERSHIP"

z = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
assert z["v25"]["genuine_h2_mu2_adapter"]["full_surface_named_j2_h2_mu2_lift_materialized"] is True
assert z["v33"]["exact_information_boundary"]["current_hs_d2_nonzero_proved"] is True
assert z["v34"]["exact_information_boundary"]["adapted_kummer_columns_materialized"] == 1
assert z["v34"]["exact_information_boundary"]["original_standard_kummer_columns_materialized"] == 0

c = json.loads((H / "controller.json").read_text())
assert c["schema"] == CONTROLLER_SCHEMA
cb = dict(c)
controller_sha = cb.pop("projection_canonical_sha256")
assert controller_sha == csha(cb)
assert c["current"]["next_exact_leaf"] == c["next_item"] == c["execution"]["next_item"] == INHERITED_NEXT
assert c["post_v41_routing"]["automatic_bounded_search_budget_per_missing_object"] == 1
assert c["stage33_12"]["finite_v4_kummer_adapted_columns_materialized"] == 1
assert c["stage33_12"]["finite_v4_kummer_columns_materialized"] == 0

out = {
    "schema": "STAGE33_MAIN_COMPACT_STATE_V20_V58_REPEATABLE_BOUNDED_SEARCH_ACTIVE",
    "role": "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE",
    "detailed_machine_authority": "stages/stage33/controller.json",
    "controller_schema": c["schema"],
    "controller_projection_canonical_sha256": controller_sha,
    "stage33_progress": c["stage33_progress"],
    "current": {
        "unit": "33-12",
        "logical_internal_branch": "33-13_FINITE_V4_KUMMER_MATRIX_REPAIR",
        "substep": "E3_A2_4B_MATERIALIZE_B1_BRANCH_H1_TO_PROPER14_MATRIX",
        "active_missing_interface": "B1_BRANCH_H1_TO_PROPER14_BRAUER_IMAGE_MATRIX",
        "next_exact_leaf": p57["next_exact_leaf"],
    },
    "authority_sync": {
        "status": "SYNCHRONIZED_V58_REPEATABLE_BOUNDED_SEARCH_OVERRIDE",
        "controller_and_generator_synchronized": True,
        "mathematical_authority": "V25_V36_EXACT_CERTIFICATE_CHAIN_PLUS_BRANCH_E3_V41_V57",
        "inherited_operational_routing_authority": "V41_ARSENAL_FIRST_ONE_BOUNDED_SEARCH_POLICY",
        "operational_routing_authority": "V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP",
        "inherited_routing_policy": "stages/stage33/33-12/j2-post-v39-arsenal-first-bounded-search-policy-v41.json",
        "routing_policy": "stages/stage33/33-12/e3-search-routing-supersession-v58.json",
        "supersession_scope": "FIXED_SEARCH_COUNT_CAP_ONLY_NO_MATHEMATICAL_CHANGE",
    },
    "current_exact_frontier": {
        "current_named_J2_hs_d2_nonzero": True,
        "j2_adapted_columns_materialized": 1,
        "j2_adapted_columns_total": 10,
        "named_J2_retained10_standard_mask_decimal": 6,
        "named_J2_standard_support_1based": [2, 3],
        "original_standard_columns_materialized": 0,
        "remaining_adapted_source_labels": REMAINING,
        "e3_proper14_mask_decimal": 20,
        "e3_b1_branch_h1_dimension": 4,
        "e3_b1_to_proper14_matrix_shape": [14, 4],
        "e3_b1_membership_status": "OPEN_NOT_COMPUTED",
        "e3_genuine_full_surface_h2_mu2_lift_materialized": False,
    },
    "locked_facts": {
        "v25_genuine_h2_mu2_adapter": {"retained10_mask_decimal": 6, "sha256": LOCKS["v25"][1], "status": "MATERIALIZED_GENUINE_FULL_SURFACE_H2_MU2_LIFT_FOR_NAMED_J2"},
        "v33_named_J2_hs_d2": {"nonzero": True, "sha256": LOCKS["v33"][1]},
        "v34_first_adapted_column": {"materialized": True, "adapted_columns_materialized": 1, "standard_columns_materialized": 0, "standard_col2_xor_col3_only": True, "sha256": LOCKS["v34"][1]},
        "v41_discovery_routing": {"sha256": V41_SHA, "status": p41["status"], "mathematical_change": False},
        "v57_b1_gysin_gate": {"status": p57["status"], "proper14_target_mask_decimal": 20, "matrix_shape": [14, 4], "membership_computed": False, "mathematical_change_after_v57": False},
        "v58_discovery_routing": {"path": "stages/stage33/33-12/e3-search-routing-supersession-v58.json", "status": p58["status"], "fixed_per_object_search_count_cap": None, "repeated_bounded_repository_search_allowed": True, "mathematical_change": False},
    },
    "resolved_investigations": {
        "named_J2_genuine_h2_mu2_adapter": "CLOSED_EXACT_V25_DO_NOT_REOPEN",
        "named_J2_current_hs_d2": "CLOSED_EXACT_NONZERO_V33_DO_NOT_REOPEN",
        "first_J2_adapted_kummer_column": "CLOSED_EXACT_V34_DO_NOT_REOPEN",
        "historical_bounded_reuse_scan": "NO_DIRECT_HIT_HISTORICAL_NOT_REPOSITORY_ABSENCE",
        "standard_col2_or_col3_from_J2_xor": "FORBIDDEN_INFERENCE_V34_V35",
    },
    "discovery_policy": {
        "ordinary_order": ["ARSENAL", "REPEATABLE_BOUNDED_REPOSITORY_SEARCH_WHEN_MATERIALLY_NEW_SIGNAL", "CONSTRUCT_WHEN_CURRENT_LEAF_HAS_ENOUGH_INFORMATION"],
        "arsenal_index": "docs/arsenal/index.json",
        "repository_asset_policy": "docs/research-os/policies/repository-asset-discovery.md",
        "effective_routing_override": "stages/stage33/33-12/e3-search-routing-supersession-v58.json",
        "fixed_per_object_search_count_cap": None,
        "repeated_bounded_repository_search_allowed": True,
        "each_repeat_requires_materially_new_mathematical_signal": True,
        "unlimited_or_open_ended_repository_search_allowed": False,
        "recursive_repository_wide_enumeration_as_ordinary_discovery_allowed": False,
        "automatic_branch_history_archaeology_after_miss_allowed": False,
        "unconstrained_keyword_expansion_allowed": False,
        "near_equivalent_miss_chasing_allowed": False,
        "miss_proves_repository_absence": False,
        "miss_proves_mathematical_nonexistence": False,
        "live_stage_authority_recheck_required_before_reuse": True,
    },
    "anti_loop_policy": {
        "repeat_bounded_search_without_materially_new_signal": False,
        "unbounded_repository_search": False,
        "do_not_split_standard_col2_col3_from_xor": True,
        "do_not_guess_remaining_columns": True,
    },
    "current_leaf_working_set": [
        "docs/research-os/policies/repository-asset-discovery.md",
        "docs/arsenal/index.json",
        "stages/stage33/ROADMAP-33-12-MICROGOALS.md",
        "stages/stage33/33-12/j2-post-v39-arsenal-first-bounded-search-policy-v41.json",
        "stages/stage33/33-12/e3-mask20-b1-gysin-image-gate-v57.json",
        "stages/stage33/33-12/e3-search-routing-supersession-v58.json",
    ],
    "execution_gate": {
        "advance_allowed": c["advance_allowed"],
        "advance_scope": "A2_4B_EXACT_B1_14X4_MATRIX_CONSTRUCTION_WITH_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH",
        "next_expected_command": "SOURCE_LOCK_B1_PIC0_2_DOMAIN_BASIS_AND_PROPER14_GYSIN_PRODUCER_THEN_BUILD_14X4_MATRIX",
        "construction_priority": REMAINING,
    },
    "firewalls": {
        "stage33_12_closed_exact": False,
        "stage33_07_reclosed": False,
        "stage33_08_released": False,
        "stage33_13_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
        "merge_allowed": False,
    },
    "work_checkpoint": EMPTY_CHECKPOINT,
}
out["canonical_sha256"] = csha(out)
rendered = json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n"
if a.check:
    assert OUT.exists() and OUT.read_text() == rendered, "MAIN-STATE.json is stale; run sync_main_state.py"
    mode = "check"
else:
    OUT.write_text(rendered)
    mode = "write"
print(json.dumps({"success": True, "mode": mode, "canonical_sha256": out["canonical_sha256"], "authority_sync": out["authority_sync"]["status"], "work_checkpoint_status": "EMPTY", "mathematical_change": False}, sort_keys=True))
