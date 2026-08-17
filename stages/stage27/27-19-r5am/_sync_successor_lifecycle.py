from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ctl_path = ROOT / "stages/stage27/27-controller.json"
doc_path = ROOT / "docs/00_CURRENT_RESEARCH_STATUS.md"
ctl = json.loads(ctl_path.read_text(encoding="utf-8"))

rj = ctl["derived_routes"]["Stage27-19-r5aj-r5ak"]
rj.update({
    "status": "AUDITED_PASS_MERGED",
    "audit_status": "PASS",
    "audit_record": "stages/stage27/27-19-r5aj/audit-final.md",
    "pr": 1056,
    "merge_commit": "80b8017a246e3519dd5e699ecea4ce944824d02f",
    "advance_allowed": True,
    "merge_allowed": True,
    "next_derived_route": "27-19-r5al",
})

ral = ctl["derived_routes"]["Stage27-19-r5al"]
ral.update({
    "status": "AUDITED_PASS_MERGED_CLOSED",
    "audit_status": "PASS",
    "audit_record": "stages/stage27/27-19-r5al/audit-final.md",
    "pr": 1059,
    "merge_commit": "ed26c2b0b127223e777a668f4f9f79ab31cf5367",
    "fresh_audit_required": False,
    "advance_allowed": True,
    "merge_allowed": True,
    "next_derived_route": "27-19-r5am",
})

ctl["derived_routes"]["Stage27-19-r5am-r5an"] = {
    "status": "BATCH_SUBMITTED_PENDING_FRESH_AUDIT",
    "trigger_checkpoint": 40,
    "route_kind": "UPPER_REENTRY_PARALLEL",
    "source_stage": "Stage19",
    "parent_route": "Stage27-19-r5al",
    "batch_routes": ["27-19-r5am", "27-19-r5an"],
    "purpose": "uniform Pell compression of one completion direction plus the kappa growing-modulus paired-slope receiver",
    "result_paths": [
        "stages/stage27/27-19-r5am/result.md",
        "stages/stage27/27-19-r5an/result.md",
    ],
    "route_contract": "stages/stage27/27-19-r5am/route-contract.json",
    "uniform_pell_count_lemma_proved": True,
    "eight_outer_variable_completion_subpower_proved": True,
    "kappa_divides_m2_minus_n2_proved": True,
    "kappa_divides_r2_plus_s2_proved": True,
    "kappa_coprime_to_mnrs_proved": True,
    "kappa_paired_slope_residue_receiver_proved": True,
    "global_growing_kappa_proved": False,
    "strict_sub_sqrt_upper_proved": False,
    "new_mu_lt_half_proved": False,
    "true_N2_exponent_identified": False,
    "audit_status": "PENDING",
    "advance_to_checkpoint50": False,
    "advance_allowed": False,
    "merge_allowed": False,
    "next_derived_route": "27-19-r5ao",
    "next_target": "DYADIC_KAPPA_SPLIT_COMBINING_LARGE_MODULUS_SLOPE_SIEVE_WITH_SMALL_KAPPA_PELL_COMPRESSION",
}

ctl["status"] = "OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R5AM_R5AN_PENDING_FRESH_AUDIT"
ctl["checkpoint_status"]["40"] = "UPPER_ATTACK_AUDITED_PASS_MERGED_WITH_R5AJ_R5AK_AUDITED_PASS_MERGED_AND_R5AL_AUDITED_PASS_MERGED_CLOSED_AND_R5AM_R5AN_PENDING_AUDIT"
ctl["state"]["CURRENT_CHECKPOINT"] = 40
ctl["state"]["MAIN_STATUS"] = "UPPER_REENTRY_STAGE27_19_R5AM_R5AN_SUBMITTED_PENDING_FRESH_AUDIT"
ctl["state"]["AUDIT_STATUS"] = "PENDING"
ctl["state"]["ADVANCE_ALLOWED"] = False
ctl["state"]["NEXT_CHECKPOINT"] = 40
ctl["state"]["MERGE_ALLOWED"] = False
ctl["next_expected_command"] = "Stage27-19-r5-audit"
ctl_path.write_text(json.dumps(ctl, indent=2) + "\n", encoding="utf-8")

doc = doc_path.read_text(encoding="utf-8")
repls = {
    "CURRENT_STAGE=Stage27-19-r5aj-r5ak-BATCH-SUBMITTED-PENDING-FRESH-AUDIT": "CURRENT_STAGE=Stage27-19-r5am-r5an-BATCH-SUBMITTED-PENDING-FRESH-AUDIT",
    "STAGE27_STATUS=OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R5AJ_R5AK_PENDING_FRESH_AUDIT": "STAGE27_STATUS=OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R5AM_R5AN_PENDING_FRESH_AUDIT",
    "STAGE27_19_R5AJ_R5AK_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT": "STAGE27_19_R5AJ_R5AK_STATUS=AUDITED_PASS_MERGED_PR1056\nSTAGE27_19_R5AL_STATUS=AUDITED_PASS_MERGED_CLOSED_PR1059\nSTAGE27_19_R5AM_R5AN_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT",
    "STAGE27_ACTIVE_UPPER_REENTRY=27-19-r5aj-r5ak": "STAGE27_ACTIVE_UPPER_REENTRY=27-19-r5am-r5an",
}
for old, new in repls.items():
    if old not in doc:
        raise SystemExit(f"missing status marker: {old}")
    doc = doc.replace(old, new, 1)
anchor = "STAGE27_STRICT_SUB_SQRT_UPPER_PROVED=false"
extra = "STAGE27_R5AM_UNIFORM_PELL_COMPLETION_SUBPOWER_PROVED=true\nSTAGE27_R5AN_KAPPA_PAIRED_SLOPE_RECEIVER_PROVED=true\n"
if extra.strip() not in doc:
    if anchor not in doc:
        raise SystemExit("missing strict upper status anchor")
    doc = doc.replace(anchor, extra + anchor, 1)
doc_path.write_text(doc, encoding="utf-8")

print("Stage27-19 r5 successor lifecycle sync prepared")
