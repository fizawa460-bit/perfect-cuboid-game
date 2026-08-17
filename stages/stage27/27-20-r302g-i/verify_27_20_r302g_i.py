#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S27 = ROOT / "stages" / "stage27"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(text: str, token: str) -> None:
    assert token in text, f"missing marker: {token}"

# Canonical predecessor must be audited and merged.
parent_audit = read(S27 / "27-20-r302d-f" / "audit.md")
for token in (
    "AUDIT_VERDICT=PASS",
    "INTEGRATION_AUDIT=PASS_AFTER_MERGE",
    "PR_MERGED=true",
    "PR_MERGE_COMMIT=2a0bb9ee116c0de7f9a5e20c4c56b8cd76134d75",
    "ADVANCE_ALLOWED=true",
):
    require(parent_audit, token)
parent_reg = json.loads(read(S27 / "27-20-r302d-f" / "batch-registry.json"))
assert parent_reg["status"] == "AUDITED_PASS_MERGED"
assert parent_reg["advance_allowed"] is True
assert parent_reg["parallel_same_serial_disposition"] == "CLOSED_UNMERGED_NOT_CANONICAL"

# New route contracts.
g = read(S27 / "27-20-r302g" / "result.md")
for token in (
    "MAIN_OUTER_U_OCCUPANCY_RATIO_DEFINED=true",
    "MAIN_OCCUPANCY_WEIGHT_IS_PHYSICAL_HOST=true",
    "MAIN_OCCUPANCY_L1_DEFICIT_IMPLIES_WALL_DEFICIT=true",
    "COMPLETE_WALL_HOST_DEFICIT_IS_ALTERNATIVE_SUCCESS=true",
    "OUTER_U_CARDINALITY_RECHARGED=false",
    "MAIN_OCCUPANCY_FIXED_POWER_DEFICIT_PROVED=false",
    "NEXT_DERIVED_ROUTE=27-20-r302h",
):
    require(g, token)

h = read(S27 / "27-20-r302h" / "result.md")
for token in (
    "SAME_MEASURE_OCCUPANCY_L2_IMPLIES_L1=true",
    "SAME_MEASURE_OCCUPANCY_L1_IMPLIES_L2=true",
    "SAME_MEASURE_OCCUPANCY_TAIL_IMPLIES_L1=true",
    "SAME_MEASURE_OCCUPANCY_L1_IMPLIES_TAIL=true",
    "FIXED_POWER_OCCUPANCY_L1_L2_TAIL_EXISTENCE_EQUIVALENT=true",
    "SECOND_MOMENT_REWEIGHTING_ALONE_NEW_SAVING=false",
    "NEXT_DERIVED_ROUTE=27-20-r302i",
):
    require(h, token)

i = read(S27 / "27-20-r302i" / "result.md")
for token in (
    "NEXT_THEOREM=UniformWallSlabMAINHighOccupancyPhysicalMassDeficit",
    "HIGH_OCCUPANCY_THRESHOLD_USES_MAIN_PHYSICAL_HOST=true",
    "HIGH_OCCUPANCY_MASS_DEFICIT_IMPLIES_WALL_POWER_DEFICIT=true",
    "NAIVE_ROW_CRT_PRODUCT_MODULUS_AS_NEW_SAVING=false",
    "PARALLEL_PR1070_CANONICAL=false",
    "MAIN_HIGH_OCCUPANCY_PHYSICAL_MASS_DEFICIT_PROVED=false",
    "NEXT_DERIVED_ROUTE=27-20-r302j",
):
    require(i, token)

for text in (g, h, i):
    require(text, "STRICT_SUB_SQRT_UPPER_PROVED=false")
    require(text, "NEW_MU_LT_HALF_PROVED=false")
    require(text, "TRUE_N2_EXPONENT_IDENTIFIED=false")
    require(text, "ADVANCE_TO_CHECKPOINT50=false")

reg = json.loads(read(S27 / "27-20-r302g-i" / "batch-registry.json"))
assert reg["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"
assert reg["audit_status"] == "PENDING"
assert reg["merge_allowed"] is False
assert reg["advance_allowed"] is False
assert reg["fresh_reaudit_required"] is True
assert reg["claims"]["fixed_power_occupancy_l1_l2_tail_existence_equivalent"] is True
assert reg["claims"]["second_moment_reweighting_alone_new_saving"] is False
assert reg["claims"]["main_high_occupancy_physical_mass_deficit_proved"] is False
assert reg["claims"]["strict_sub_sqrt_upper_proved"] is False
assert reg["advance_to_checkpoint50"] is False
assert reg["next_derived_route"] == "27-20-r302j"
assert reg["next_audit_command"] == "Stage27-20-r302-audit"
assert reg["discarded_parallel_pr"] == 1070

sync = json.loads(read(S27 / "27-20-r302g-i" / "controller-sync-delta.json"))
assert sync["global_controller_rewritten"] is False
assert sync["base_main_sha"] == "2a0bb9ee116c0de7f9a5e20c4c56b8cd76134d75"
assert sync["stage20_delta"]["Stage27-20-r302d-f"]["status"] == "AUDITED_PASS_MERGED"
for route in ("Stage27-20-r302g", "Stage27-20-r302h", "Stage27-20-r302i"):
    assert sync["stage20_delta"][route]["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"
    assert sync["stage20_delta"][route]["audit_status"] == "PENDING"
assert sync["stage20_delta"]["merge_allowed"] is False
assert sync["stage20_delta"]["advance_allowed"] is False
assert sync["stage20_delta"]["fresh_reaudit_required"] is True
assert sync["stage20_delta"]["next_derived_route"] == "27-20-r302j"

print("Stage27-20-r302g-i pre-audit verification: PASS")
