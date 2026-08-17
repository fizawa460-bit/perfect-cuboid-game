#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S27 = ROOT / "stages" / "stage27"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(text: str, token: str) -> None:
    assert token in text, f"missing marker: {token}"


# Parent lifecycle gate must already be closed on the consumed base.
r301z_audit = read(S27 / "27-20-r301z" / "audit.md")
for token in (
    "AUDIT_VERDICT=PASS",
    "ADVANCE_ALLOWED=true",
    "FRESH_REAUDIT_REQUIRED=false",
    "NEXT_BATCH=Stage27-20-r302-main-batch",
):
    require(r301z_audit, token)

r301z_reg = json.loads(read(S27 / "27-20-r301z" / "batch-registry.json"))
assert r301z_reg["status"] == "AUDITED_PASS_MERGED"
assert r301z_reg["audit_status"] == "PASS"
assert r301z_reg["advance_allowed"] is True
assert r301z_reg["fresh_reaudit_required"] is False

# Mathematics/status firewalls.
a = read(S27 / "27-20-r302a" / "result.md")
for token in (
    "WALL_SLAB_MAIN_FIRST_MOMENT_SPECIALIZATION_DERIVED=true",
    "MAIN_NESTED_DIVISOR_SYSTEM_RETAINED=true",
    "MAIN_TWO_SIMULTANEOUS_ROOT_CONGRUENCES_RETAINED=true",
    "STAGE14_LOCAL_ROOT_LEDGER_RECHARGED=false",
    "WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false",
    "OFF_THE_SHELF_FIRST_MOMENT_APPLICABLE=false",
    "NEXT_DERIVED_ROUTE=27-20-r302b",
):
    require(a, token)

b = read(S27 / "27-20-r302b" / "result.md")
for token in (
    "HOST_TO_Q1_WALL_SUPPORT_MONOTONE_TRANSFER_PROVED=true",
    "Q1_WALL_TO_GLOBAL_GLUE_FORMULA_PROVED=true",
    "GLOBAL_DEFICIT_IF_R302_WFM=Delta=min(delta,2eta0,1/16)",
    "WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false",
    "ADVANCE_TO_CHECKPOINT50=false",
    "NEXT_DERIVED_ROUTE=27-20-r302c",
):
    require(b, token)

c = read(S27 / "27-20-r302c" / "result.md")
for token in (
    "PHYSICALLY_WEIGHTED_EXCEPTIONAL_CELL_DICHOTOMY_DERIVED=true",
    "UNWEIGHTED_EXCEPTIONAL_CELL_COUNT_SUFFICIENT=false",
    "UNRELATED_LABEL_AVERAGE_SUFFICIENT=false",
    "BAD_CELL_PHYSICAL_HOST_MASS_DEFICIT_REQUIRED=true",
    "BAD_CELL_FIXED_POWER_MASS_DEFICIT_PROVED=false",
    "NEXT_DERIVED_ROUTE=27-20-r302d",
):
    require(c, token)

for text in (a, b, c):
    require(text, "STRICT_SUB_SQRT_UPPER_PROVED=false")
    require(text, "NEW_MU_LT_HALF_PROVED=false")
    require(text, "TRUE_N2_EXPONENT_IDENTIFIED=false")

# Fresh hostile audit is materialized, but advancement remains blocked until merge to main.
audit = read(S27 / "27-20-r302a-c" / "audit.md")
for token in (
    "AUDIT_VERDICT=PASS",
    "MATHEMATICAL_AUDIT=PASS",
    "CI_AUDIT=PASS",
    "INTEGRATION_AUDIT=PASS_PREMERGE",
    "AUDIT_PR=1065",
    "AUDITED_CONTENT_COMMIT=5241f8334f706f1d3e4c2b9ebbb158e0d6662238",
    "MERGE_ALLOWED=true",
    "ADVANCE_ALLOWED=false",
    "ADVANCE_TO_CHECKPOINT50=false",
    "NEXT_DERIVED_ROUTE=27-20-r302d",
):
    require(audit, token)

reg = json.loads(read(S27 / "27-20-r302a-c" / "batch-registry.json"))
assert reg["batch_id"] == "Stage27-20-r302a-c"
assert reg["status"] == "AUDITED_PASS_PENDING_MERGE"
assert reg["audit_status"] == "PASS"
assert reg["merge_allowed"] is True
assert reg["advance_allowed"] is False
assert reg["fresh_reaudit_required"] is False
assert reg["advance_to_checkpoint50"] is False
assert reg["audited_content_commit"] == "5241f8334f706f1d3e4c2b9ebbb158e0d6662238"
assert reg["claims"]["wall_slab_aggregate_deficit_theorem_proved"] is False
assert reg["claims"]["strict_sub_sqrt_upper_proved"] is False
assert reg["claims"]["new_mu_lt_half_proved"] is False
assert reg["next_derived_route"] == "27-20-r302d"

sync = json.loads(read(S27 / "27-20-r302a-c" / "controller-sync-delta.json"))
assert sync["global_controller_rewritten"] is False
assert sync["base_main_sha"] == "366548fbc2d41536cd0d0e285784e932ec27bad7"
for route in ("Stage27-20-r302a", "Stage27-20-r302b", "Stage27-20-r302c"):
    assert sync["stage20_delta"][route]["status"] == "AUDITED_PASS_PENDING_MERGE"
    assert sync["stage20_delta"][route]["audit_status"] == "PASS"
    assert sync["stage20_delta"][route]["merge_allowed"] is True
    assert sync["stage20_delta"][route]["advance_allowed"] is False
assert sync["stage20_delta"]["next_derived_route"] == "27-20-r302d"
assert sync["stage20_delta"]["advance_to_checkpoint50"] is False
assert sync["stage20_delta"]["strict_sub_sqrt_upper_proved"] is False

print("Stage27-20-r302a-c audited pre-merge verification: PASS")
