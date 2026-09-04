#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state for V41 Arsenal-first bounded search routing."""
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
POLICY = D / "j2-post-v39-arsenal-first-bounded-search-policy-v41.json"
RESEARCH_POLICY = ROOT / "docs/research-os/policies/repository-asset-discovery.md"
ARSENAL = ROOT / "docs/arsenal/index.json"
REMAINING = ["e3", "e1", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]
NEXT = "ARSENAL_FIRST_THEN_ONE_BOUNDED_SEARCH_THEN_CONSTRUCT_OR_REQUEST_USER_AUTHORIZATION"
SCOPE = "ARSENAL_FIRST_ONE_BOUNDED_SEARCH_THEN_CONSTRUCT_OR_USER_AUTHORIZED_BROADENING"
CONTROLLER_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"
POLICY_SHA = "32b2ad7da0ad7ced22bd3d27ebc3abec36ed9d8fe037a4e2c676e3e44471a6f8"
LOCKS = {
    "v25": (D / "j2-genuine-h2-mu2-kummer-adapter-v25.json", "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
    "v33": (D / "j2-current-hs-d2-nonzero-v33.json", "59385430d2806fd600006b8bee1e02170f28d0a598912555d1e905e556c84b8f"),
    "v34": (D / "j2-adapted-first-kummer-column-v34.json", "eb53bd545626efe3b32d407eccd2788e991494203acd718d88100ee7233b909e"),
    "v35": (D / "j2-post-v34-main-handoff-v35.json", "4837ebeb0dd4ea97f196f6e4a405923eede73b53f663f9e0acac66aaf4e5f8e9"),
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
assert RESEARCH_POLICY.is_file(), RESEARCH_POLICY
rp = RESEARCH_POLICY.read_text()
assert "Stage16 and later" in rp and "Stages12–15" in rp and "## Arsenal" in rp
assert ARSENAL.is_file(), ARSENAL
arsenal = json.loads(ARSENAL.read_text())
assert str(arsenal.get("schema", "")).startswith("RESEARCH_ARSENAL_"), arsenal.get("schema")

p = locked(POLICY, POLICY_SHA)
r = p["routing_contract"]
assert r["arsenal_first_for_existing_cross_stage_weapon"] is True
assert r["one_automatic_bounded_repository_search_after_arsenal_miss"] is True
assert r["broader_repository_history_or_origin_search_requires_explicit_user_authorization"] is True
assert r["arsenal_miss_proves_repository_absence"] is False
assert r["bounded_search_miss_proves_repository_absence"] is False
assert p["anti_loop"]["automatic_bounded_search_budget_per_missing_object"] == 1

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
assert c["current"]["next_exact_leaf"] == c["next_item"] == c["execution"]["next_item"] == NEXT
assert c["advance_allowed"] is True and c["execution"]["advance_allowed"] is True
assert c["advance_scope"] == SCOPE
route = c["post_v41_routing"]
assert route["policy_v41_canonical_sha256"] == POLICY_SHA
assert route["arsenal_first"] is True
assert route["automatic_bounded_search_budget_per_missing_object"] == 1
assert route["broader_search_requires_explicit_user_authorization"] is True
assert route["miss_proves_repository_absence"] is False

s = c["stage33_12"]
assert s["finite_v4_kummer_adapted_columns_materialized"] == 1
assert s["finite_v4_kummer_columns_materialized"] == 0

out = {
    "schema": "STAGE33_MAIN_COMPACT_STATE_V19_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE",
    "role": "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE",
    "detailed_machine_authority": "stages/stage33/controller.json",
    "controller_schema": c["schema"],
    "controller_projection_canonical_sha256": controller_sha,
    "stage33_progress": c["stage33_progress"],
    "current": {k: c["current"][k] for k in ["unit", "logical_internal_branch", "substep", "active_missing_interface", "next_exact_leaf"]},
    "authority_sync": {
        "status": "SYNCHRONIZED_V41_ARSENAL_FIRST_BOUNDED_SEARCH",
        "controller_and_generator_synchronized": True,
        "mathematical_authority": "V25_V36_EXACT_CERTIFICATE_CHAIN_UNCHANGED",
        "operational_routing_authority": "V41_ARSENAL_FIRST_BOUNDED_SEARCH_POLICY",
        "routing_policy": "stages/stage33/33-12/j2-post-v39-arsenal-first-bounded-search-policy-v41.json"
    },
    "current_exact_frontier": {
        "current_named_J2_hs_d2_nonzero": True,
        "j2_adapted_columns_materialized": 1,
        "j2_adapted_columns_total": 10,
        "named_J2_retained10_standard_mask_decimal": 6,
        "named_J2_standard_support_1based": [2, 3],
        "original_standard_columns_materialized": 0,
        "remaining_adapted_source_labels": REMAINING
    },
    "locked_facts": {
        "v25_genuine_h2_mu2_adapter": {"retained10_mask_decimal": 6, "sha256": LOCKS["v25"][1], "status": "MATERIALIZED_GENUINE_FULL_SURFACE_H2_MU2_LIFT_FOR_NAMED_J2"},
        "v33_named_J2_hs_d2": {"nonzero": True, "sha256": LOCKS["v33"][1]},
        "v34_first_adapted_column": {"materialized": True, "adapted_columns_materialized": 1, "standard_columns_materialized": 0, "standard_col2_xor_col3_only": True, "sha256": LOCKS["v34"][1]},
        "v41_discovery_routing": {"sha256": POLICY_SHA, "status": p["status"], "mathematical_change": False}
    },
    "resolved_investigations": {
        "named_J2_genuine_h2_mu2_adapter": "CLOSED_EXACT_V25_DO_NOT_REOPEN",
        "named_J2_current_hs_d2": "CLOSED_EXACT_NONZERO_V33_DO_NOT_REOPEN",
        "first_J2_adapted_kummer_column": "CLOSED_EXACT_V34_DO_NOT_REOPEN",
        "historical_bounded_reuse_scan": "NO_DIRECT_HIT_HISTORICAL_NOT_REPOSITORY_ABSENCE",
        "standard_col2_or_col3_from_J2_xor": "FORBIDDEN_INFERENCE_V34_V35"
    },
    "discovery_policy": {
        "ordinary_order": ["ARSENAL", "ONE_BOUNDED_REPOSITORY_SEARCH", "CONSTRUCT_OR_REQUEST_USER_AUTHORIZATION_FOR_BROADER_SEARCH"],
        "arsenal_index": "docs/arsenal/index.json",
        "repository_asset_policy": "docs/research-os/policies/repository-asset-discovery.md",
        "automatic_bounded_search_budget_per_missing_object": 1,
        "broader_repository_history_or_origin_search_requires_explicit_user_authorization": True,
        "miss_proves_repository_absence": False,
        "live_stage_authority_recheck_required_before_reuse": True
    },
    "anti_loop_policy": {
        "repeat_or_broaden_without_new_user_authorization": False,
        "do_not_split_standard_col2_col3_from_xor": True,
        "do_not_guess_remaining_columns": True
    },
    "current_leaf_working_set": [
        "docs/research-os/policies/repository-asset-discovery.md",
        "docs/arsenal/index.json",
        "stages/stage33/33-12/j2-post-v39-arsenal-first-bounded-search-policy-v41.json"
    ],
    "execution_gate": {
        "advance_allowed": c["advance_allowed"],
        "advance_scope": c["advance_scope"],
        "next_expected_command": c["next_expected_command"],
        "construction_priority": REMAINING
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
        "merge_allowed": False
    },
    "work_checkpoint": EMPTY_CHECKPOINT
}
out["canonical_sha256"] = csha(out)
rendered = json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n"
if a.check:
    assert OUT.exists() and OUT.read_text() == rendered, "MAIN-STATE.json is stale; run sync_main_state.py"
    mode = "check"
else:
    OUT.write_text(rendered)
    mode = "write"
print(json.dumps({"success": True, "mode": mode, "canonical_sha256": out["canonical_sha256"], "authority_sync": "SYNCHRONIZED_V41_ARSENAL_FIRST_BOUNDED_SEARCH", "work_checkpoint_status": "EMPTY", "mathematical_change": False}, sort_keys=True))
