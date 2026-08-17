#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S27 = ROOT / "stages" / "stage27"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(text: str, token: str) -> None:
    assert token in text, f"missing marker: {token}"


# Consumed Stage20 parent must be audited and merged.
parent_audit = read(S27 / "27-20-r302a-c" / "audit.md")
for token in (
    "AUDIT_VERDICT=PASS",
    "INTEGRATION_AUDIT=PASS_AFTER_MERGE",
    "PR_MERGED=true",
    "PR_MERGE_COMMIT=2e479836fcb0caa21b62f3dd50748a02eb235832",
    "ADVANCE_ALLOWED=true",
    "ADVANCE_TO_CHECKPOINT50=false",
):
    require(parent_audit, token)
parent_reg = json.loads(read(S27 / "27-20-r302a-c" / "batch-registry.json"))
assert parent_reg["status"] == "AUDITED_PASS_MERGED"
assert parent_reg["advance_allowed"] is True
assert parent_reg["merge_commit"] == "2e479836fcb0caa21b62f3dd50748a02eb235832"

# Imported checkpoint40 weapons must already have hostile PASS records.
aa_ac_audit = read(S27 / "27-40aa-ac" / "audit.md")
require(aa_ac_audit, "AUDIT_VERDICT=PASS")
require(aa_ac_audit, "AUDIT_SCOPE=Stage27-40aa+Stage27-40ab+Stage27-40ac")
require(aa_ac_audit, "STRICT_SUB_SQRT_UPPER_PROVED=false")
ad_audit = read(S27 / "27-40ad" / "audit.md")
require(ad_audit, "AUDIT_VERDICT=PASS")
require(ad_audit, "OUTER_PHYSICAL_WEIGHTED_AVERAGING_THEOREM_PROVED=false")
ae_audit = read(S27 / "27-40ae" / "audit.md")
require(ae_audit, "AUDIT_VERDICT=PASS")
require(ae_audit, "OUTER_WEIGHTED_EXCEPTIONAL_MASS_CONTRACT_ACCEPTED=true")
require(ae_audit, "OUTER_PHYSICAL_WEIGHTED_EXCEPTIONAL_MASS_BOUND_PROVED=false")

# New mathematics and firewalls.
d = read(S27 / "27-20-r302d" / "result.md")
for token in (
    "MAIN_WALL_HOST_OUTER_U_DISINTEGRATION_DERIVED=true",
    "OUTER_U_LABEL_CARDINALITY_RECHARGED=false",
    "MAIN_FIBER_MONOTONE_DOMINATION=F_MAIN<=H_phys_MAIN",
    "R302_UW_RELATIVE_TO_ABSOLUTE_TRANSFER_PROVED=true",
    "MAIN_OUTER_U_PHYSICAL_WEIGHTED_EXCEPTIONAL_MASS_DEFICIT_PROVED=false",
    "NEXT_DERIVED_ROUTE=27-20-r302e",
):
    require(d, token)

e = read(S27 / "27-20-r302e" / "result.md")
for token in (
    "STAGE27_40AE_IMPORTED_AS_WEIGHTED_THEOREM_SHAPE=true",
    "STAGE27_40AE_T_BASELINE_EQUALS_MAIN_HOST_CLAIMED=false",
    "T_TO_MAIN_COMMON_REFINEMENT_DOMINATION_REQUIRED=true",
    "T_TO_MAIN_COMMON_REFINEMENT_DOMINATION_PROVED=false",
    "OUTER_U_CARDINALITY_RECHARGED=false",
    "NEXT_DERIVED_ROUTE=27-20-r302f",
):
    require(e, token)

f = read(S27 / "27-20-r302f" / "result.md")
for token in (
    "CURRENT_IMPORTED_WEIGHTED_THEOREM_CLOSES_MAIN_WALL=false",
    "NEXT_THEOREM=UniformWallSlabMAINOuterUPhysicalHostWeightedExceptionalMassOrWeightedSecondMomentDeficit",
    "MAIN_OUTER_U_PHYSICAL_WEIGHTED_EXCEPTIONAL_MASS_DEFICIT_PROVED=false",
    "MAIN_OUTER_U_WEIGHTED_SECOND_MOMENT_PROVED=false",
    "T_TO_MAIN_COMMON_REFINEMENT_DOMINATION_PROVED=false",
    "WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false",
    "NEXT_DERIVED_ROUTE=27-20-r302g",
):
    require(f, token)

for text in (d, e, f):
    require(text, "STRICT_SUB_SQRT_UPPER_PROVED=false")
    require(text, "NEW_MU_LT_HALF_PROVED=false")
    require(text, "TRUE_N2_EXPONENT_IDENTIFIED=false")
    require(text, "ADVANCE_TO_CHECKPOINT50=false")

# Fresh hostile audit must be materialized for exactly PR #1069 / audited content head.
audit = read(S27 / "27-20-r302d-f" / "audit.md")
for token in (
    "AUDIT_VERDICT=PASS",
    "MATHEMATICAL_AUDIT=PASS",
    "CI_AUDIT=PASS",
    "INTEGRATION_AUDIT=PASS_PREMERGE",
    "AUDIT_PR=1069",
    "AUDITED_CONTENT_COMMIT=15357b59efc5dfc0f995c8ceef177f0374850168",
    "DEDICATED_CI_RUN=32008546216",
    "MERGE_ALLOWED=true",
    "ADVANCE_ALLOWED=false",
    "FRESH_REAUDIT_REQUIRED=false",
    "NEXT_DERIVED_ROUTE=27-20-r302g",
):
    require(audit, token)

reg = json.loads(read(S27 / "27-20-r302d-f" / "batch-registry.json"))
assert reg["status"] == "AUDITED_PASS_PENDING_MERGE"
assert reg["audit_status"] == "PASS"
assert reg["merge_allowed"] is True
assert reg["advance_allowed"] is False
assert reg["fresh_reaudit_required"] is False
assert reg["audit_pr"] == 1069
assert reg["audited_content_commit"] == "15357b59efc5dfc0f995c8ceef177f0374850168"
assert reg["dedicated_ci_run"] == 32008546216
assert reg["claims"]["outer_u_label_cardinality_recharged"] is False
assert reg["claims"]["t_to_main_common_refinement_domination_proved"] is False
assert reg["claims"]["strict_sub_sqrt_upper_proved"] is False
assert reg["advance_to_checkpoint50"] is False
assert reg["next_derived_route"] == "27-20-r302g"
assert reg["parallel_same_serial_pr"] == 1070
assert reg["parallel_same_serial_not_approved_by_this_audit"] is True

sync = json.loads(read(S27 / "27-20-r302d-f" / "controller-sync-delta.json"))
assert sync["global_controller_rewritten"] is False
assert sync["base_main_sha"] == "2e479836fcb0caa21b62f3dd50748a02eb235832"
assert sync["stage20_delta"]["Stage27-20-r302a-c"]["status"] == "AUDITED_PASS_MERGED"
for route in ("Stage27-20-r302d", "Stage27-20-r302e", "Stage27-20-r302f"):
    assert sync["stage20_delta"][route]["status"] == "AUDITED_PASS_PENDING_MERGE"
    assert sync["stage20_delta"][route]["audit_status"] == "PASS"
assert sync["stage20_delta"]["audit_pr"] == 1069
assert sync["stage20_delta"]["merge_allowed"] is True
assert sync["stage20_delta"]["advance_allowed"] is False
assert sync["stage20_delta"]["fresh_reaudit_required"] is False
assert sync["stage20_delta"]["parallel_same_serial_pr"] == 1070
assert sync["stage20_delta"]["next_derived_route"] == "27-20-r302g"
assert sync["stage20_delta"]["advance_to_checkpoint50"] is False

print("Stage27-20-r302d-f hostile-audit closeout verification: PASS")
