#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S27 = ROOT / "stages" / "stage27"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(text: str, token: str) -> None:
    assert token in text, f"missing marker: {token}"


# Parent lifecycle gate.
r301z_audit = read(S27 / "27-20-r301z" / "audit.md")
for token in ("AUDIT_VERDICT=PASS", "ADVANCE_ALLOWED=true", "FRESH_REAUDIT_REQUIRED=false"):
    require(r301z_audit, token)

# Frozen mathematics and non-claims.
a = read(S27 / "27-20-r302a" / "result.md")
b = read(S27 / "27-20-r302b" / "result.md")
c = read(S27 / "27-20-r302c" / "result.md")
for token in (
    "WALL_SLAB_MAIN_FIRST_MOMENT_SPECIALIZATION_DERIVED=true",
    "MAIN_NESTED_DIVISOR_SYSTEM_RETAINED=true",
    "MAIN_TWO_SIMULTANEOUS_ROOT_CONGRUENCES_RETAINED=true",
    "STAGE14_LOCAL_ROOT_LEDGER_RECHARGED=false",
    "WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false",
):
    require(a, token)
for token in (
    "HOST_TO_Q1_WALL_SUPPORT_MONOTONE_TRANSFER_PROVED=true",
    "GLOBAL_DEFICIT_IF_R302_WFM=Delta=min(delta,2eta0,1/16)",
    "WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false",
):
    require(b, token)
for token in (
    "PHYSICALLY_WEIGHTED_EXCEPTIONAL_CELL_DICHOTOMY_DERIVED=true",
    "UNWEIGHTED_EXCEPTIONAL_CELL_COUNT_SUFFICIENT=false",
    "BAD_CELL_PHYSICAL_HOST_MASS_DEFICIT_REQUIRED=true",
    "BAD_CELL_FIXED_POWER_MASS_DEFICIT_PROVED=false",
):
    require(c, token)
for text in (a, b, c):
    require(text, "STRICT_SUB_SQRT_UPPER_PROVED=false")
    require(text, "NEW_MU_LT_HALF_PROVED=false")
    require(text, "TRUE_N2_EXPONENT_IDENTIFIED=false")

# Fresh audit is now merged and closed at checkpoint40.
audit = read(S27 / "27-20-r302a-c" / "audit.md")
for token in (
    "AUDIT_VERDICT=PASS",
    "MATHEMATICAL_AUDIT=PASS",
    "CI_AUDIT=PASS",
    "INTEGRATION_AUDIT=PASS_AFTER_MERGE",
    "PR_MERGED=true",
    "PR_MERGE_COMMIT=2e479836fcb0caa21b62f3dd50748a02eb235832",
    "MERGE_ALLOWED=true",
    "ADVANCE_ALLOWED=true",
    "ADVANCE_TO_CHECKPOINT50=false",
    "NEXT_DERIVED_ROUTE=27-20-r302d",
):
    require(audit, token)

reg = json.loads(read(S27 / "27-20-r302a-c" / "batch-registry.json"))
assert reg["status"] == "AUDITED_PASS_MERGED"
assert reg["audit_status"] == "PASS"
assert reg["merge_allowed"] is True
assert reg["advance_allowed"] is True
assert reg["fresh_reaudit_required"] is False
assert reg["merge_commit"] == "2e479836fcb0caa21b62f3dd50748a02eb235832"
assert reg["advance_to_checkpoint50"] is False
assert reg["claims"]["strict_sub_sqrt_upper_proved"] is False
assert reg["next_derived_route"] == "27-20-r302d"

sync = json.loads(read(S27 / "27-20-r302a-c" / "controller-sync-delta.json"))
assert sync["global_controller_rewritten"] is False
assert sync["post_merge_main_sha"] == "2e479836fcb0caa21b62f3dd50748a02eb235832"
for route in ("Stage27-20-r302a", "Stage27-20-r302b", "Stage27-20-r302c"):
    assert sync["stage20_delta"][route]["status"] == "AUDITED_PASS_MERGED"
    assert sync["stage20_delta"][route]["advance_allowed"] is True
assert sync["stage20_delta"]["advance_to_checkpoint50"] is False

print("Stage27-20-r302a-c audited merged verification: PASS")
