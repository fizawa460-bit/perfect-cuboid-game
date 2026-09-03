#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state after V39 locator-first routing repair."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

H = Path(__file__).resolve().parent
D = H / "33-12"
ROOT = H.parent.parent
OUT = H / "MAIN-STATE.json"
RETIRED_HANDOFF = H / "MAIN-BATCH-HANDOFF.md"
REMAINING = ["e3", "e1", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]
NEXT = "QUERY_ALL_CURRENT_EVIDENCE_REGISTRIES_THEN_CONSTRUCT_REMAINING_GENUINE_H2_MU2_LIFT_IF_NO_SUITABLE_HIT"
CONTROLLER_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V61_POST_V39_CURRENT_MULTI_REGISTRY_CONSTRUCTION_ACTIVE"
POLICY_V39_SHA = "26e47d41b94caf1cb931f765468d6779a760adec434d4b1b6698f838b3db46b2"
LOCKS = {
    "v25": (D / "j2-genuine-h2-mu2-kummer-adapter-v25.json", "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
    "v33": (D / "j2-current-hs-d2-nonzero-v33.json", "59385430d2806fd600006b8bee1e02170f28d0a598912555d1e905e556c84b8f"),
    "v34": (D / "j2-adapted-first-kummer-column-v34.json", "eb53bd545626efe3b32d407eccd2788e991494203acd718d88100ee7233b909e"),
    "v35": (D / "j2-post-v34-main-handoff-v35.json", "4837ebeb0dd4ea97f196f6e4a405923eede73b53f663f9e0acac66aaf4e5f8e9"),
    "v36": (D / "j2-post-v35-evidence-locator-handoff-v36.json", "065c0ca8a92ad0994a88b2a62337a0ceb33af9823e746590e7de590676d6db7c"),
    "v39": (D / "j2-post-v38-locator-first-construction-policy-v39.json", POLICY_V39_SHA),
}
LOCATOR_BLOBS = {
    ROOT / "docs/evidence-locator/index.json": "a32d83a0e5529b444f0d5f58dcad44517b5fe087",
    ROOT / "docs/evidence-locator/query_evidence.py": "306205983a30932f318e33a0e78c1c53b7233593",
    ROOT / "docs/evidence-locator/stage32-post1498.json": "935bb4f0821af4fd451d45003d4e430a751e68ac",
    ROOT / "docs/evidence-locator/stage33.json": "0ecf26acd08170cea09aba3a4972cdb44428ca6e",
    ROOT / "docs/research-os/policies/repository-asset-discovery.md": "12f35149db732f185c84a17d31f4c9b360624e6c",
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

def git_blob(path):
    return subprocess.check_output(["git", "hash-object", "--", str(path)], cwd=ROOT, text=True).strip()

ap = argparse.ArgumentParser()
ap.add_argument("--check", action="store_true")
a = ap.parse_args()

assert not RETIRED_HANDOFF.exists(), "MAIN-BATCH-HANDOFF.md is retired"
for path, expected in LOCATOR_BLOBS.items():
    assert path.is_file(), path
    assert git_blob(path) == expected, path

# HOSTILE_AUDIT_CURRENT_MULTI_REGISTRY_V40
q = json.loads(subprocess.check_output(["python3", "-B", str(ROOT / "docs/evidence-locator/query_evidence.py"), "genuine full-surface H2(mu2) lift another retained10 adapted source e3 e1 e4 e5 e6 e7 e8 e9 e10", "--stage", "33", "--limit", "20"], cwd=ROOT, text=True))
assert q["schema"] == "PERFECT_CUBOID_EVIDENCE_QUERY_RESULT_V3_MULTI_STAGE"
assert {x["file"] for x in q["registry_sources"]} == {"index.json", "stage32-post1498.json", "stage33.json"}
qm = next(x for x in q["matches"] if x["asset_id"] == "EVID-S33-GERSTEN-CONNECTING-26COL-AUDITED")
assert "this asset does not itself identify a standalone genuine full-surface H2(mu2) lift for any remaining retained10 adapted source" in qm["limitations"]
assert not [x for x in q["matches"] if "this asset does not itself identify a standalone genuine full-surface H2(mu2) lift for any remaining retained10 adapted source" not in x.get("limitations", [])]

c = json.loads((H / "controller.json").read_text())
assert c["schema"] == CONTROLLER_SCHEMA
cb = dict(c)
controller_sha = cb.pop("projection_canonical_sha256")
assert controller_sha == csha(cb)
z = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
p39 = z["v39"]

assert p39["routing_contract"]["query_locator_first_for_existing_evidence"] is True
assert p39["routing_contract"]["construction_authorized_after_locator_miss"] is True
assert p39["routing_contract"]["broad_repository_or_history_fallback_after_miss"] is False
assert p39["audit_finding"]["locator_miss_proves_repository_absence"] is False
assert c["current"]["next_exact_leaf"] == c["next_item"] == c["execution"]["next_item"] == NEXT
assert c["advance_allowed"] is True and c["execution"]["advance_allowed"] is True
assert c["advance_scope"] == "CURRENT_MULTI_REGISTRY_LOCATOR_FIRST_THEN_CONSTRUCT_MISSING_GENUINE_H2_MU2_LIFT"
assert c["post_v39_routing"]["policy_v39_canonical_sha256"] == POLICY_V39_SHA
assert c["post_v39_routing"]["broad_historical_search_permitted"] is False
assert c["post_v39_routing"]["construction_authorized_after_locator_miss"] is True

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
    "schema": "STAGE33_MAIN_COMPACT_STATE_V18_POST_V39_CURRENT_MULTI_REGISTRY_CONSTRUCTION_ACTIVE",
    "role": "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE",
    "detailed_machine_authority": "stages/stage33/controller.json",
    "controller_schema": c["schema"],
    "controller_projection_canonical_sha256": controller_sha,
    "stage33_progress": c["stage33_progress"],
    "current": {k: c["current"][k] for k in ["unit", "logical_internal_branch", "substep", "active_missing_interface", "next_exact_leaf"]},
    "authority_sync": {
        "status": "SYNCHRONIZED_POST_V39_ROUTING",
        "controller_and_generator_synchronized": True,
        "mathematical_authority": "V25_V36_EXACT_CERTIFICATE_CHAIN",
        "operational_routing_authority": "V39_LOCATOR_FIRST_CONSTRUCTION_POLICY",
        "routing_policy": "stages/stage33/33-12/j2-post-v38-locator-first-construction-policy-v39.json",
        "historical_sync_receipt": "stages/stage33/33-12/j2-post-v36-controller-generator-sync-v38.json"
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
        "v36_locator_miss": {"positive_asset_match_materialized": False, "old_origin_search_restarted": False, "sha256": LOCKS["v36"][1], "status": "HISTORICAL_BOUNDED_MISS_NOT_REPO_ABSENCE"},
        "v39_routing_policy": {"sha256": POLICY_V39_SHA, "status": p39["status"], "construction_authorized_after_locator_miss": True}
    },
    "resolved_investigations": {
        "named_J2_genuine_h2_mu2_adapter": "CLOSED_EXACT_V25_DO_NOT_REOPEN",
        "named_J2_current_hs_d2": "CLOSED_EXACT_NONZERO_V33_DO_NOT_REOPEN",
        "first_J2_adapted_kummer_column": "CLOSED_EXACT_V34_DO_NOT_REOPEN",
        "registered_evidence_locator_reuse_first_scan": "V36_BOUNDED_MISS_HISTORICAL_NOT_AN_ORDINARY_MAIN_STOP",
        "locator_miss_routing": "V39_QUERY_FIRST_THEN_CONSTRUCT_MISSING_EXACT_OBJECT",
        "standard_col2_or_col3_from_J2_xor": "FORBIDDEN_INFERENCE_V34_V35",
        "startup_authority_override": "CLEARED_BY_CONTROLLER_GENERATOR_SYNC_V38"
    },
    "anti_loop_policy": {
        "ordinary_main_rule": "Query #1498 first for an existing reusable asset. If there is no suitable hit, construct the missing exact object; do not fall back to broad repository/history origin search.",
        "locator_query_is_repeatable_routing_step": True,
        "locator_miss_proves_repository_absence": False,
        "locator_miss_authorizes_new_construction": True,
        "broad_repository_or_history_fallback_after_locator_miss": False,
        "do_not_split_standard_col2_col3_from_xor": True,
        "do_not_guess_remaining_columns": True
    },
    "current_leaf_working_set": [
        "docs/evidence-locator/index.json",
        "docs/evidence-locator/query_evidence.py",
        "docs/evidence-locator/stage32-post1498.json",
        "docs/evidence-locator/stage33.json",
        "stages/stage33/33-12/j2-post-v35-evidence-locator-handoff-v36.json",
        "stages/stage33/33-12/j2-post-v38-locator-first-construction-policy-v39.json"
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
print(json.dumps({"success": True, "mode": mode, "canonical_sha256": out["canonical_sha256"], "authority_sync": "SYNCHRONIZED_POST_V39_ROUTING", "work_checkpoint_status": "EMPTY", "marker": "MAIN_STATE_GENERATED_FROM_V60"}, sort_keys=True))
