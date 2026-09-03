#!/usr/bin/env python3
"""Build/check Stage33 MAIN state across the post-V36 authority migration.

V58 + ACTIVE_POST_V36_OVERRIDE is transition/read-only mode.
V59 is the synchronized canonical generator mode.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import runpy
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "33-12"
OUT = H / "MAIN-STATE.json"
RETIRED_HANDOFF = H / "MAIN-BATCH-HANDOFF.md"
V37_VERIFY = D / "verify_j2_post_v36_authority_sync_v37.py"
REMAINING = ["e3", "e1", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]
NEXT = "WAIT_FOR_NEW_GENUINE_H2_MU2_LIFT_OR_REGISTERED_POSITIVE_EVIDENCE_ASSET"
LOCKS = {
    "v25": (D / "j2-genuine-h2-mu2-kummer-adapter-v25.json", "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
    "v33": (D / "j2-current-hs-d2-nonzero-v33.json", "59385430d2806fd600006b8bee1e02170f28d0a598912555d1e905e556c84b8f"),
    "v34": (D / "j2-adapted-first-kummer-column-v34.json", "eb53bd545626efe3b32d407eccd2788e991494203acd718d88100ee7233b909e"),
    "v35": (D / "j2-post-v34-main-handoff-v35.json", "4837ebeb0dd4ea97f196f6e4a405923eede73b53f663f9e0acac66aaf4e5f8e9"),
    "v36": (D / "j2-post-v35-evidence-locator-handoff-v36.json", "065c0ca8a92ad0994a88b2a62337a0ceb33af9823e746590e7de590676d6db7c"),
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
c = json.loads((H / "controller.json").read_text())

# Safe transition behavior until controller V59 lands.
if c["schema"] == "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V58_NAMED_J2_SOURCE_EXACT_GENUINE_KUMMER_ADAPTER_MISSING":
    state = json.loads(OUT.read_text())
    assert state["authority_sync"]["status"] == "ACTIVE_POST_V36_OVERRIDE"
    assert state["authority_sync"]["legacy_generator_must_not_overwrite_main_state"] is True
    runpy.run_path(str(V37_VERIFY), run_name="__main__")
    print(json.dumps({
        "success": True,
        "mode": "transition-check" if a.check else "transition-validate-no-write",
        "authority_sync": "ACTIVE_POST_V36_OVERRIDE",
        "main_state_overwritten": False,
        "marker": "V58_TRANSITION_SAFE",
    }, sort_keys=True))
    raise SystemExit(0)

assert c["schema"] == "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V59_POST_V36_FIRST_ADAPTED_COLUMN_REUSE_STOP"
cb = dict(c)
controller_sha = cb.pop("projection_canonical_sha256")
assert controller_sha == csha(cb)
z = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
pa = c["post_v36_authority"]
assert pa["status"] == "SYNCHRONIZED_EXACT_PROJECTION_NO_MATH_CHANGE"
assert pa["v25_genuine_h2_mu2_adapter_canonical_sha256"] == LOCKS["v25"][1]
assert pa["v33_current_hs_d2_nonzero_canonical_sha256"] == LOCKS["v33"][1]
assert pa["v34_first_adapted_column_canonical_sha256"] == LOCKS["v34"][1]
assert pa["v36_handoff_canonical_sha256"] == LOCKS["v36"][1]
assert c["current"]["next_exact_leaf"] == c["next_item"] == c["execution"]["next_item"] == NEXT
assert c["advance_allowed"] is False and c["execution"]["advance_allowed"] is False
s = c["stage33_12"]
assert s["finite_v4_kummer_adapted_columns_materialized"] == 1
assert s["finite_v4_kummer_columns_materialized"] == 0
assert z["v25"]["genuine_h2_mu2_adapter"]["full_surface_named_j2_h2_mu2_lift_materialized"] is True
assert z["v33"]["exact_information_boundary"]["current_hs_d2_nonzero_proved"] is True
assert z["v34"]["exact_information_boundary"]["adapted_kummer_columns_materialized"] == 1
assert z["v34"]["exact_information_boundary"]["original_standard_kummer_columns_materialized"] == 0
assert z["v36"]["bounded_reuse_first_search"]["positive_asset_match_materialized"] is False
assert z["v36"]["bounded_reuse_first_search"]["old_origin_search_restarted"] is False

out = {
    "schema": "STAGE33_MAIN_COMPACT_STATE_V16_POST_V36_SYNCHRONIZED_REUSE_STOP",
    "role": "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE",
    "detailed_machine_authority": "stages/stage33/controller.json",
    "controller_schema": c["schema"],
    "controller_projection_canonical_sha256": controller_sha,
    "stage33_progress": c["stage33_progress"],
    "current": {k: c["current"][k] for k in ["unit", "logical_internal_branch", "substep", "active_missing_interface", "next_exact_leaf"]},
    "authority_sync": {
        "status": "SYNCHRONIZED_POST_V36",
        "override_active": False,
        "controller_and_generator_synchronized": True,
        "mathematical_authority": "V25_V36_EXACT_CERTIFICATE_CHAIN",
        "synchronization_receipt": "stages/stage33/33-12/j2-post-v36-controller-generator-sync-v38.json",
        "superseded_override_checkpoint": "stages/stage33/33-12/j2-post-v36-startup-authority-repair-v37.json",
    },
    "current_exact_frontier": {
        "current_named_J2_hs_d2_nonzero": True,
        "j2_adapted_columns_materialized": 1,
        "j2_adapted_columns_total": 10,
        "named_J2_retained10_standard_mask_decimal": 6,
        "named_J2_standard_support_1based": [2, 3],
        "original_standard_columns_materialized": 0,
        "remaining_adapted_source_labels": REMAINING,
    },
    "locked_facts": {
        "v25_genuine_h2_mu2_adapter": {"retained10_mask_decimal": 6, "sha256": LOCKS["v25"][1], "status": "MATERIALIZED_GENUINE_FULL_SURFACE_H2_MU2_LIFT_FOR_NAMED_J2"},
        "v33_named_J2_hs_d2": {"nonzero": True, "sha256": LOCKS["v33"][1]},
        "v34_first_adapted_column": {"materialized": True, "adapted_columns_materialized": 1, "standard_columns_materialized": 0, "standard_col2_xor_col3_only": True, "sha256": LOCKS["v34"][1]},
        "v36_reuse_first_stop": {"positive_asset_match_materialized": False, "old_origin_search_restarted": False, "sha256": LOCKS["v36"][1], "status": z["v36"]["status"]},
    },
    "resolved_investigations": {
        "named_J2_genuine_h2_mu2_adapter": "CLOSED_EXACT_V25_DO_NOT_REOPEN",
        "named_J2_current_hs_d2": "CLOSED_EXACT_NONZERO_V33_DO_NOT_REOPEN",
        "first_J2_adapted_kummer_column": "CLOSED_EXACT_V34_DO_NOT_REOPEN",
        "registered_evidence_locator_reuse_first_scan": "BOUNDED_MISS_V36_DO_NOT_REPEAT_WITHOUT_NEW_REGISTERED_ASSET",
        "standard_col2_or_col3_from_J2_xor": "FORBIDDEN_INFERENCE_V34_V35",
        "startup_authority_override": "CLEARED_BY_CONTROLLER_GENERATOR_SYNC_V38",
    },
    "anti_loop_reopen_policy": {
        "ordinary_main_rule": "V36 is the current exact stop. Do not restart old origin/history search, split standard col2/col3 from their XOR, or guess remaining Kummer columns. Without a newly derived genuine lift or newly registered positive evidence asset, stop.",
        "reopen_only_if": [
            "a V25-V36 source lock or verifier fails replay",
            "a newly derived genuine full-surface H2(mu2) lift is supplied",
            "a newly registered positive evidence asset source-locks a remaining adapted source",
            "the user explicitly requests hostile audit or historical revalidation",
        ],
    },
    "current_leaf_working_set": [
        "stages/stage33/33-12/j2-post-v34-main-handoff-v35.json",
        "stages/stage33/33-12/j2-post-v35-evidence-locator-handoff-v36.json",
    ],
    "execution_gate": {
        "advance_allowed": c["advance_allowed"],
        "advance_scope": c["advance_scope"],
        "next_expected_command": c["next_expected_command"],
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
print(json.dumps({
    "success": True,
    "mode": mode,
    "canonical_sha256": out["canonical_sha256"],
    "authority_sync": "SYNCHRONIZED_POST_V36",
    "work_checkpoint_status": "EMPTY",
    "marker": "MAIN_STATE_GENERATED_FROM_V59",
}, sort_keys=True))
