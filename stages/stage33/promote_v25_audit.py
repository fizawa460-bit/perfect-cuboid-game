#!/usr/bin/env python3
"""One-shot V25 audited promotion; read-only verifier afterwards."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

H = Path(__file__).resolve().parent
C_PATH = H / "controller.json"
SYNC_PATH = H / "sync_main_state.py"
MAIN_PATH = H / "MAIN-STATE.json"
V25_PATH = H / "33-12/j2-genuine-h2-mu2-kummer-adapter-v25.json"
AUDIT_PATH = H / "33-12/v25-hostile-audit-pass-receipt.json"
V25_SHA = "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"
AUDIT_SHA = "444c038d1bbe1396d312d68d7a7cdfb71509db4419fd35839088dfe53c5066da"
AUDIT_REVIEW = 5090434903
AUDIT_HEAD = "9a01ec5a5c87782e44f1bffe91cc85e89db25fa1"
OLD_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V58_NAMED_J2_SOURCE_EXACT_GENUINE_KUMMER_ADAPTER_MISSING"
NEW_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V59_NAMED_J2_GENUINE_H2_MU2_ADAPTER_MATERIALIZED_PIC2_HS_D2_OPEN"
ADVANCE_SCOPE = "STAGE33_12_CECH_PIC2_HS_D2_ONLY"
ACTIVE_MISSING = "ACTUAL_CECH_LOCAL_RANK2_LATTICES_OVERLAP_TRANSITIONS_PIC_MOD2_DEFECT_AND_HS_D2_FOR_LAMBDA_D"
SUBSTEP = "MATERIALIZE_ACTUAL_CECH_LOCAL_LATTICES_PIC2_AND_HS_D2"


def csha(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def canonical(path: Path, expected: str):
    x = json.loads(path.read_text())
    body = dict(x)
    got = body.pop("canonical_sha256")
    assert got == expected == csha(body), path
    return x


def replace_once(text: str, old: str, new: str) -> str:
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new, 1)


def verify_boundary(c, v25, audit):
    s = c["stage33_12"]
    assert audit["status"] == "PASS_HOSTILE_AUDIT"
    assert audit["audit_review_id"] == AUDIT_REVIEW
    assert audit["audited_head_sha"] == AUDIT_HEAD
    assert audit["audited_pr"] == 1488
    assert v25["status"] == "PASS_EXACT_CURRENT_NAMED_J2_GENUINE_H2_MU2_LIFT_ADAPTER_MATERIALIZED_CONNECTING_COCYCLE_OPEN"
    assert v25["current_named_source"]["retained10_mask_decimal"] == 6
    assert v25["current_named_source"]["two_bit_value_a_b"] == [0, 1]
    assert v25["genuine_h2_mu2_adapter"]["full_surface_named_j2_h2_mu2_lift_materialized"] is True
    assert v25["genuine_h2_mu2_adapter"]["historical_kummer_glue_used"] is False
    assert v25["genuine_h2_mu2_adapter"]["raw_weight15_h1_used_as_kummer_boundary"] is False
    assert v25["remaining_interface"]["standard_kummer_columns_materialized"] == 0
    assert v25["remaining_interface"]["v4_connecting_cocycle_materialized"] is False
    assert c["stage33_progress"] == "6/11"
    assert s["corrected_J2_genuine_h2_mu2_adapter_certificate_sha256"] == V25_SHA
    assert s["corrected_J2_v25_hostile_audit_pass_receipt_sha256"] == AUDIT_SHA
    assert s["corrected_J2_genuine_full_surface_h2_mu2_lift_materialized"] is True
    assert s["corrected_J2_genuine_h2_mu2_adapter_historical_kummer_glue_used"] is False
    assert s["corrected_J2_genuine_h2_mu2_adapter_raw_weight15_h1_used_as_kummer_boundary"] is False
    assert s["corrected_J2_actual_kummer_target_materialized"] is False
    assert s["corrected_J2_named_source_target_relation_materialized"] is False
    assert s["finite_v4_kummer_columns_materialized"] == 0
    assert c["merge_allowed"] is False
    assert c["theorem_credit"] is False
    assert c["receiver_credit"] is False
    assert c["endpoint_credit"] is False


def apply(v25, audit):
    c = json.loads(C_PATH.read_text())
    assert c["schema"] == OLD_SCHEMA
    s = c["stage33_12"]
    q = c["current"]
    nxt = v25["remaining_interface"]["next_exact_leaf"]

    c["schema"] = NEW_SCHEMA
    c["advance_scope"] = ADVANCE_SCOPE
    c["execution"]["advance_scope"] = ADVANCE_SCOPE
    c["current_exact_promotion_scope"] = "V25_GENUINE_H2_MU2_ADAPTER_HOSTILE_AUDIT_PASS_NO_COLUMN_NO_CLOSURE"
    c["current_exact_promotion_audit_required"] = False
    c["current_exact_promotion_audit_review_id"] = AUDIT_REVIEW
    c["current_exact_promotion_audit_head_sha"] = AUDIT_HEAD
    c["current_exact_promotion_audit_receipt_sha256"] = AUDIT_SHA
    q["substep"] = SUBSTEP
    q["active_missing_interface"] = ACTIVE_MISSING
    q["next_exact_leaf"] = nxt
    c["next_item"] = nxt
    c["execution"]["next_item"] = nxt
    c["loop_state"]["last_cycle_route_status"] = "NAMED_J2_GENUINE_H2_MU2_ADAPTER_MATERIALIZED_PIC2_HS_D2_OPEN"
    c["loop_state"]["last_new_view"] = "V25 hostile-audited promotion reattaches exact current named J2 beta1 / mask6 / (0,1) to genuine full-surface lambda_D in H2(mu2). Old weight-15 H1, C2+C3 and historical Kummer glue remain revoked. Standard columns remain 0/10; actual Cech local lattices, Pic/2 defect and HS d2/V4 cocycle are the next leaf."

    s["corrected_J2_genuine_h2_mu2_adapter_certificate"] = "stages/stage33/33-12/j2-genuine-h2-mu2-kummer-adapter-v25.json"
    s["corrected_J2_genuine_h2_mu2_adapter_certificate_sha256"] = V25_SHA
    s["corrected_J2_v25_hostile_audit_pass_receipt"] = "stages/stage33/33-12/v25-hostile-audit-pass-receipt.json"
    s["corrected_J2_v25_hostile_audit_pass_receipt_sha256"] = AUDIT_SHA
    s["corrected_J2_v25_hostile_audit_review_id"] = AUDIT_REVIEW
    s["corrected_J2_v25_hostile_audit_head_sha"] = AUDIT_HEAD
    s["corrected_J2_genuine_full_surface_h2_mu2_lift_materialized"] = True
    s["corrected_J2_genuine_h2_mu2_lift_class"] = "lambda_D=alpha(e_D), represented generically by {f2,g22}"
    s["corrected_J2_genuine_h2_mu2_lift_brauer_image"] = "corrected J2=(f2,1)"
    s["corrected_J2_genuine_h2_mu2_adapter_historical_kummer_glue_used"] = False
    s["corrected_J2_genuine_h2_mu2_adapter_raw_weight15_h1_used_as_kummer_boundary"] = False
    s["corrected_J2_surface_mu2_lift_scope"] = "GENUINE_FULL_SURFACE_H2_MU2_NAMED_J2_LIFT_V25_SOURCE_FIRST_REATTACHMENT"
    s["minimal_missing_exact_datum"] = ACTIVE_MISSING
    s["corrected_J2_order4_route_status"] = "SOURCE_FIRST_NAMED_FUNCTIONAL_EXACT_GENUINE_H2_MU2_ADAPTER_MATERIALIZED_PIC2_HS_D2_OPEN"
    s["status"] = "OPEN_CURRENT_NAMED_SOURCE_AND_GENUINE_H2_MU2_ADAPTER_EXACT_PIC2_HS_D2_OPEN"
    for x in s["logical_internal_sequence"]:
        if x["id"] == "33-13":
            x["status"] = "CURRENT_NAMED_J2_SOURCE_AND_GENUINE_H2_MU2_ADAPTER_EXACT_PIC2_HS_D2_OPEN_STANDARD_COLUMNS_0_OF_10"

    C_PATH.write_text(json.dumps(c, sort_keys=True, separators=(",", ":")) + "\n")

    p = SYNC_PATH.read_text()
    p = replace_once(p,
        'V24_SHA = "9d104c7d4054b5d92f1df382654b152c30ca0be6ef267aa028fe8b9d78a4687d"\n\nEMPTY_CHECKPOINT',
        'V24_SHA = "9d104c7d4054b5d92f1df382654b152c30ca0be6ef267aa028fe8b9d78a4687d"\nV25_PATH = H / "33-12/j2-genuine-h2-mu2-kummer-adapter-v25.json"\nV25_SHA = "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"\nV25_AUDIT_PATH = H / "33-12/v25-hostile-audit-pass-receipt.json"\nV25_AUDIT_SHA = "444c038d1bbe1396d312d68d7a7cdfb71509db4419fd35839088dfe53c5066da"\n\nEMPTY_CHECKPOINT')
    p = replace_once(p,
        'v24 = load_canonical(V24_PATH, V24_SHA)\ncheckpoint = load_work_checkpoint()',
        'v24 = load_canonical(V24_PATH, V24_SHA)\nv25 = load_canonical(V25_PATH, V25_SHA)\nv25audit = load_canonical(V25_AUDIT_PATH, V25_AUDIT_SHA)\ncheckpoint = load_work_checkpoint()')
    p = replace_once(p, f'assert c["schema"] == "{OLD_SCHEMA}"', f'assert c["schema"] == "{NEW_SCHEMA}"')
    p = replace_once(p, 'assert q["substep"] == "MATERIALIZE_GENUINE_H2_MU2_KUMMER_ADAPTER"', f'assert q["substep"] == "{SUBSTEP}"')
    p = replace_once(p, 'assert q["active_missing_interface"] == "ACTUAL_FULL_SURFACE_H2_MU2_KUMMER_EXTENSION_OR_EQUIVALENT_GENUINE_LIFT_ADAPTER_FOR_NAMED_J2"', f'assert q["active_missing_interface"] == "{ACTIVE_MISSING}"')
    p = replace_once(p, 'assert c["advance_scope"] == "STAGE33_12_GENUINE_H2_MU2_KUMMER_ADAPTER_ONLY"', f'assert c["advance_scope"] == "{ADVANCE_SCOPE}"')
    p = replace_once(p,
        'assert s["finite_v4_kummer_named_relation_rank_f2"] == 0\n\nassert c["audit_required"] is False',
        'assert s["finite_v4_kummer_named_relation_rank_f2"] == 0\nassert v25["status"] == "PASS_EXACT_CURRENT_NAMED_J2_GENUINE_H2_MU2_LIFT_ADAPTER_MATERIALIZED_CONNECTING_COCYCLE_OPEN"\nassert v25["current_named_source"]["retained10_mask_decimal"] == 6\nassert v25["current_named_source"]["two_bit_value_a_b"] == [0, 1]\nassert v25["genuine_h2_mu2_adapter"]["full_surface_named_j2_h2_mu2_lift_materialized"] is True\nassert v25["genuine_h2_mu2_adapter"]["historical_kummer_glue_used"] is False\nassert v25["genuine_h2_mu2_adapter"]["raw_weight15_h1_used_as_kummer_boundary"] is False\nassert v25["remaining_interface"]["standard_kummer_columns_materialized"] == 0\nassert v25audit["status"] == "PASS_HOSTILE_AUDIT"\nassert v25audit["audit_review_id"] == 5090434903\nassert v25audit["audited_head_sha"] == "9a01ec5a5c87782e44f1bffe91cc85e89db25fa1"\nassert s["corrected_J2_genuine_h2_mu2_adapter_certificate_sha256"] == V25_SHA\nassert s["corrected_J2_v25_hostile_audit_pass_receipt_sha256"] == V25_AUDIT_SHA\nassert s["corrected_J2_genuine_full_surface_h2_mu2_lift_materialized"] is True\nassert s["corrected_J2_genuine_h2_mu2_adapter_historical_kummer_glue_used"] is False\nassert s["corrected_J2_genuine_h2_mu2_adapter_raw_weight15_h1_used_as_kummer_boundary"] is False\n\nassert c["audit_required"] is False')
    p = replace_once(p,
        '"schema": "STAGE33_MAIN_COMPACT_STATE_V14_NAMED_J2_SOURCE_EXACT_GENUINE_KUMMER_ADAPTER_MISSING",',
        '"schema": "STAGE33_MAIN_COMPACT_STATE_V15_NAMED_J2_GENUINE_H2_MU2_ADAPTER_MATERIALIZED_PIC2_HS_D2_OPEN",')
    p = replace_once(p,
        'out["authority_changes"].update({',
        'out["locked_facts"]["v25_genuine_H2_mu2_adapter"] = {\n    "status": v25["status"],\n    "audit_review_id": v25audit["audit_review_id"],\n    "audited_head_sha": v25audit["audited_head_sha"],\n    "named_J2_retained10_mask_decimal": 6,\n    "two_bit_value_a_b": [0, 1],\n    "full_surface_named_j2_h2_mu2_lift_materialized": True,\n    "lift_class": v25["genuine_h2_mu2_adapter"]["kc_lift_class"],\n    "old_weight15_target_restored": False,\n    "historical_kummer_glue_used": False,\n    "standard_kummer_columns_materialized": 0,\n    "v25_sha256": V25_SHA,\n    "audit_sha256": V25_AUDIT_SHA,\n}\nout["authority_changes"].update({')
    p = replace_once(p,
        '    "old_weight15_raw_H1_as_named_kummer_target": "REVOKED_SCOPE_V24_RAW_H1_EVIDENCE_RETAINED",\n})',
        '    "old_weight15_raw_H1_as_named_kummer_target": "REVOKED_SCOPE_V24_RAW_H1_EVIDENCE_RETAINED",\n    "genuine_H2_mu2_named_J2_adapter": "PROMOTED_EXACT_HOSTILE_AUDITED_V25",\n})')
    p = replace_once(p,
        '    "raw_h1_vs_kummer_target_scope": "CLOSED_EXACT_V24_GENUINE_KUMMER_ADAPTER_MISSING",\n})',
        '    "raw_h1_vs_kummer_target_scope": "CLOSED_EXACT_V24_GENUINE_KUMMER_ADAPTER_MISSING",\n    "genuine_h2_mu2_named_j2_adapter": "CLOSED_EXACT_HOSTILE_AUDITED_V25",\n})')
    old_open = '''out["open_datum"] = {\n    "named_J2_order4_two_bit_value_source_locked": True,\n    "named_J2_order4_functional_actual_s3_behavior_source_locked": True,\n    "named_J2_proper_Br2_source_coordinate_materialized": True,\n    "retained10_named_J2_source_coordinate_materialized": True,\n    "named_J2_source_target_relation_materialized": False,\n    "named_source_target_relation_rank_f2": 0,\n    "matrix_standard_columns_materialized": 0,\n    "target_h1_basis41_adapter_repair_required": False,\n    "genuine_H2_mu2_kummer_adapter_required": True,\n}'''
    new_open = '''out["open_datum"] = {\n    "named_J2_order4_two_bit_value_source_locked": True,\n    "named_J2_order4_functional_actual_s3_behavior_source_locked": True,\n    "named_J2_proper_Br2_source_coordinate_materialized": True,\n    "retained10_named_J2_source_coordinate_materialized": True,\n    "genuine_H2_mu2_kummer_adapter_materialized": True,\n    "genuine_H2_mu2_kummer_adapter_required": False,\n    "actual_cech_local_rank2_lattices_materialized": False,\n    "pic_mod2_defect_1cocycle_materialized": False,\n    "hs_d2_2cocycle_materialized": False,\n    "v4_connecting_cocycle_materialized": False,\n    "named_J2_source_target_relation_materialized": False,\n    "named_source_target_relation_rank_f2": 0,\n    "matrix_standard_columns_materialized": 0,\n    "target_h1_basis41_adapter_repair_required": False,\n}'''
    p = replace_once(p, old_open, new_open)
    start = p.index('out["current_leaf_working_set"] = [')
    end = p.index('out["anti_loop_reopen_policy"] = {', start)
    p = p[:start] + '''out["current_leaf_working_set"] = [\n    "stages/stage33/33-12/j2-genuine-h2-mu2-kummer-adapter-v25.json",\n    "stages/stage33/33-12/verify_j2_genuine_h2_mu2_kummer_adapter_v25.py",\n    "stages/stage33/33-12/v25-hostile-audit-pass-receipt.json",\n    "stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json",\n    "stages/stage33/33-12/j2-full-surface-mu2-zero-defect-contract.json",\n    "stages/stage33/33-12/j2-cc-actual-cech-global-square-overlap.json",\n    "stages/stage33/33-12/j2-ct-six-kc-support-fullpic64-pullbacks.json",\n]\n''' + p[end:]
    start = p.index('out["anti_loop_reopen_policy"] = {')
    end = p.index('out["canonical_sha256"] = csha(out)', start)
    p = p[:start] + '''out["anti_loop_reopen_policy"] = {\n    "ordinary_main_rule": "V25 hostile-audited promotion fixes the genuine full-surface H2(mu2) lift lambda_D for the exact current named J2. Do not reopen the source, old weight-15 H1 target, C2+C3, or historical Kummer glue. Continue only with actual Cech local lattices/overlaps, marked Pic/2 defect, and HS d2/V4 connecting cocycle.",\n    "reopen_only_if": [\n        "a pinned V21-V25 source lock or V25 audit receipt fails replay",\n        "the exact V21 projection or marked Brauer coordinate changes",\n        "the actual Cech compactification/local-lattice convention changes",\n        "the user explicitly requests hostile audit or historical revalidation",\n    ],\n}\n''' + p[end:]
    SYNC_PATH.write_text(p)

    # A promoted boundary starts with no operational-only handoff residue.
    old_main = json.loads(MAIN_PATH.read_text())
    old_main["work_checkpoint"] = {"status": "EMPTY", "authority": "OPERATIONAL_ONLY_NOT_PROOF"}
    MAIN_PATH.write_text(json.dumps(old_main, sort_keys=True, separators=(",", ":")) + "\n")
    subprocess.run([sys.executable, str(SYNC_PATH)], check=True)

    c2 = json.loads(C_PATH.read_text())
    verify_boundary(c2, v25, audit)
    subprocess.run([sys.executable, str(SYNC_PATH), "--check"], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    assert a.apply ^ a.check
    v25 = canonical(V25_PATH, V25_SHA)
    audit = canonical(AUDIT_PATH, AUDIT_SHA)
    if a.apply:
        apply(v25, audit)
        mode = "applied"
    else:
        c = json.loads(C_PATH.read_text())
        verify_boundary(c, v25, audit)
        subprocess.run([sys.executable, str(SYNC_PATH), "--check"], check=True)
        mode = "check"
    print(json.dumps({"success": True, "mode": mode, "v25_sha256": V25_SHA, "audit_sha256": AUDIT_SHA}, sort_keys=True))


if __name__ == "__main__":
    main()
