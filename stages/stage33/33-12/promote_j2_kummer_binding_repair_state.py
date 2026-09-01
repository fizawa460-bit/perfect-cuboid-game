#!/usr/bin/env python3
"""Promote the exact J2 source-target module-compatibility failure into Stage33 state.

This is a downgrade/reopen operation under the research-credit firewall.  The
independently exact J2 proper-Br2 source and independently exact raw/75D target
remain retained; only their previously asserted Kummer connecting relation is
revoked.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
CONTROLLER = S33 / "controller.json"
RESULT = HERE / "result.md"
AUDIT = HERE / "j2-kummer-source-target-module-compatibility-audit.json"
AUDIT_SHA = "463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229"
OLD_REL_SHA = "0563af417d41765e39ecb1b73fdabf33c1bc831e78f74d2227d286227c3aa082"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


audit = json.loads(AUDIT.read_text(encoding="utf-8"))
body = dict(audit)
claimed = body.pop("canonical_sha256")
assert claimed == AUDIT_SHA == csha(body)
assert audit["status"] == "FAIL_EXACT_LOCKED_J2_SOURCE_TARGET_MODULE_COMPATIBILITY"
assert audit["locked_named_j2"]["locked_75D_target_reachable_from_locked_source"] is False
assert audit["consequence"]["named_source_target_relation_rank_credit_after_this_audit"] == 0
assert audit["promotion_firewall"]["only_source_target_binding_revoked"] is True
assert audit["promotion_firewall"]["J2_source_certificate_revoked"] is False
assert audit["promotion_firewall"]["J2_target_certificate_revoked"] is False

ctl = json.loads(CONTROLLER.read_text(encoding="utf-8"))
stage = ctl["stage33_12"]
current = ctl["current"]

# Refuse to silently promote from an unexpected predecessor state.
assert ctl["schema"] == "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V51_J2_PICARD_ADJOINT_RELATION_RANK1"
assert stage["corrected_J2_named_source_target_relation_materialized"] is True
assert stage["corrected_J2_named_source_target_relation_sha256"] == OLD_REL_SHA
assert stage["finite_v4_kummer_named_relations_materialized"] == 1
assert stage["finite_v4_kummer_named_relation_rank_f2"] == 1
assert stage["finite_v4_kummer_columns_materialized"] == 0
assert stage["first_exact_kummer_column_materialized"] is False
assert ctl["theorem_credit"] is False and ctl["receiver_credit"] is False and ctl["endpoint_credit"] is False
assert ctl["perfect_cuboid_existence_claim"] is False
assert ctl["perfect_cuboid_nonexistence_claim"] is False

ctl["schema"] = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V52_J2_KUMMER_BINDING_REPAIR"
current.update({
    "logical_internal_branch": "33-13_FINITE_V4_KUMMER_MATRIX_REPAIR",
    "substep": "REPAIR_J2_SOURCE_TARGET_KUMMER_MODULE_COMPATIBILITY",
    "active_missing_interface": "J2_SOURCE_TARGET_BINDING_INCOMPATIBLE_WITH_LOCKED_V4_MODULE_ACTIONS",
    "next_exact_leaf": "IDENTIFY_EXACT_SOURCE_OR_COORDINATE_ADAPTER_FOR_LOCKED_J2_RAW_75D_TARGET_AND_REQUIRE_V4_MODULE_EXTENSION_COMPATIBILITY",
})

stage.update({
    "corrected_J2_named_source_target_relation_materialized": False,
    "corrected_J2_named_source_target_relation_status": "REVOKED_BY_EXACT_V4_MODULE_COMPATIBILITY_AUDIT",
    "corrected_J2_named_source_target_relation_historical_certificate": "stages/stage33/33-12/j2-named-kummer-source-target-relation.json",
    "corrected_J2_named_source_target_relation_historical_sha256": OLD_REL_SHA,
    "corrected_J2_named_standard_column_relation_1based": "REVOKED: C2 + C3 = h_J2",
    "corrected_J2_named_standard_column_relation_valid": False,
    "corrected_J2_kummer_source_target_module_compatibility": False,
    "corrected_J2_kummer_source_target_module_compatibility_audit": "stages/stage33/33-12/j2-kummer-source-target-module-compatibility-audit.json",
    "corrected_J2_kummer_source_target_module_compatibility_audit_sha256": AUDIT_SHA,
    "corrected_J2_kummer_locked_source_reachable_H1_dimension_f2": 13,
    "corrected_J2_kummer_locked_target_reachable_from_locked_source": False,
    "finite_v4_kummer_named_relations_materialized": 0,
    "finite_v4_kummer_named_relation_rank_f2": 0,
    "minimal_missing_exact_datum": "EXACT_COORDINATE_OR_SEMANTIC_ADAPTER_RECONCILING_J2_PROPER_BR2_SOURCE_WITH_J2_RAW_75D_TARGET_UNDER_LOCKED_V4_MODULE_ACTIONS",
})

for row in stage["logical_internal_sequence"]:
    if row["id"] == "33-13":
        row["status"] = "CURRENT_J2_SOURCE_TARGET_BINDING_REPAIR_RELATION_RANK_0_STANDARD_COLUMNS_0_OF_10"

ctl["execution"].update({
    "advance_scope": "STAGE33_12_INTERNAL_33_13_J2_KUMMER_BINDING_REPAIR_ONLY_NO_PARENT_RECLOSURE",
    "next_item": "Stage33-12_33-13_REPAIR_J2_SOURCE_TARGET_KUMMER_BINDING",
})
ctl["loop_state"].update({
    "stagnation_count": 0,
    "last_cycle_route_status": "FAIL_EXACT_J2_SOURCE_TARGET_MODULE_COMPATIBILITY_RELATION_CREDIT_REVOKED",
    "last_new_view": "The independently exact corrected J2 proper-Br2 source retained10=e2+e3 and independently exact J2 raw/75D H1 target cannot be the boundary pair of any F2[V4]-module extension with the locked Pic/2 and proper-Br2 actions. All-extension audit: 1792 variables, rank 781, nullity 1011; J2 reachable H1 subspace dimension 13; locked target unreachable. Revoke only C2+C3=h_J2 relation credit and repair the semantic/coordinate binding.",
})
ctl["audit_scope"] = "STAGE33_12_INTERNAL_33_13_J2_KUMMER_SOURCE_TARGET_BINDING_REPAIR"
ctl["advance_scope"] = "STAGE33_12_INTERNAL_33_13_J2_KUMMER_BINDING_REPAIR_ONLY_NO_PARENT_RECLOSURE"
ctl["next_item"] = "Stage33-12_33-13_REPAIR_J2_SOURCE_TARGET_KUMMER_BINDING"

# Firewalls remain closed.
assert stage["closed_exact"] is False
assert ctl["release_gates"]["stage33_07_reclosed"] is False
assert ctl["release_gates"]["stage33_08_released"] is False
assert ctl["merge_allowed"] is False
assert ctl["theorem_credit"] is False and ctl["receiver_credit"] is False and ctl["endpoint_credit"] is False
assert ctl["perfect_cuboid_existence_claim"] is False
assert ctl["perfect_cuboid_nonexistence_claim"] is False

CONTROLLER.write_text(json.dumps(ctl, indent=2, sort_keys=False) + "\n", encoding="utf-8")

heading = "## J2 Kummer source-target binding — exact compatibility audit revokes rank-one relation"
text = RESULT.read_text(encoding="utf-8").rstrip()
if heading not in text:
    text += f"\n\n{heading}\n\n"
    text += (
        "A later exact V4-module-extension audit tested the independently fixed corrected J2 proper-Br2 source "
        "against the independently fixed raw/75D J2 target under the locked Pic/2 and proper-Br2 actions. "
        "Across the full compatible F2[V4]-module-extension solution space (1792 block variables, rank 781, nullity 1011), "
        "the locked J2 source reaches only a 13-dimensional H1 subspace and the locked weight-15 target is not in it. "
        "All 896 elementary section-change gauge checks independently reproduce pure Picard coboundaries.\n\n"
    )
    text += "```text\n"
    text += "J2_LOCKED_SOURCE_RETAINED10=e2+e3\n"
    text += "J2_LOCKED_SOURCE_REACHABLE_H1_DIM=13\n"
    text += "J2_LOCKED_TARGET_REACHABLE_FROM_LOCKED_SOURCE=false\n"
    text += f"COMPATIBILITY_AUDIT_SHA256={AUDIT_SHA}\n"
    text += "NAMED_SOURCE_TARGET_RELATION_RANK_F2=0\n"
    text += "STANDARD_KUMMER_COLUMNS_MATERIALIZED=0/10\n"
    text += "```
\n"
    text += (
        "Therefore the earlier `C2 + C3 = h_J2` statement is revoked as a Kummer-matrix relation. "
        "This does not revoke the J2 proper-Br2 source certificate or the J2 raw/75D target certificate separately; "
        "it revokes only their semantic/source-target binding. The next exact leaf is to identify the coordinate or semantic "
        "adapter that places both exact objects in one compatible Kummer V4-module extension. Stage33-12 remains open; "
        "no parent reclosure, downstream release, theorem, receiver, endpoint, or perfect-cuboid claim is promoted."
    )
RESULT.write_text(text.rstrip() + "\n", encoding="utf-8")

print(json.dumps({
    "success": True,
    "controller_schema": ctl["schema"],
    "relation_rank_f2": stage["finite_v4_kummer_named_relation_rank_f2"],
    "relation_materialized": stage["corrected_J2_named_source_target_relation_materialized"],
    "next_exact_leaf": current["next_exact_leaf"],
    "compatibility_audit_sha256": AUDIT_SHA,
}, sort_keys=True))
