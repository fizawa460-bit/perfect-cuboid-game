#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S27 = ROOT / "stages" / "stage27"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(text: str, token: str) -> None:
    assert token in text, f"missing marker: {token}"

parent_audit = read(S27 / "27-20-r302a-c" / "audit.md")
for token in (
    "AUDIT_VERDICT=PASS",
    "INTEGRATION_AUDIT=PASS_AFTER_MERGE",
    "PR_MERGED=true",
    "ADVANCE_ALLOWED=true",
):
    require(parent_audit, token)

for route in ("27-20-r302d", "27-20-r302e", "27-20-r302f"):
    text = read(S27 / route / "result.md")
    require(text, "STRICT_SUB_SQRT_UPPER_PROVED=false")
    require(text, "NEW_MU_LT_HALF_PROVED=false")
    require(text, "TRUE_N2_EXPONENT_IDENTIFIED=false")
    require(text, "ADVANCE_TO_CHECKPOINT50=false")

f = read(S27 / "27-20-r302f" / "result.md")
require(f, "NEXT_DERIVED_ROUTE=27-20-r302g")
require(f, "CURRENT_IMPORTED_WEIGHTED_THEOREM_CLOSES_MAIN_WALL=false")

audit = read(S27 / "27-20-r302d-f" / "audit.md")
for token in (
    "AUDIT_VERDICT=PASS",
    "MATHEMATICAL_AUDIT=PASS",
    "CI_AUDIT=PASS",
    "INTEGRATION_AUDIT=PASS_AFTER_MERGE",
    "AUDIT_PR=1069",
    "AUDIT_CLOSEOUT_PR=1071",
    "AUDITED_CONTENT_COMMIT=15357b59efc5dfc0f995c8ceef177f0374850168",
    "PR_MERGED=true",
    "PR_MERGE_COMMIT=2a0bb9ee116c0de7f9a5e20c4c56b8cd76134d75",
    "MERGE_ALLOWED=true",
    "ADVANCE_ALLOWED=true",
    "FRESH_REAUDIT_REQUIRED=false",
    "NEXT_DERIVED_ROUTE=27-20-r302g",
):
    require(audit, token)

reg = json.loads(read(S27 / "27-20-r302d-f" / "batch-registry.json"))
assert reg["status"] == "AUDITED_PASS_MERGED"
assert reg["audit_status"] == "PASS"
assert reg["merge_allowed"] is True
assert reg["advance_allowed"] is True
assert reg["fresh_reaudit_required"] is False
assert reg["audit_pr"] == 1069
assert reg["audit_closeout_pr"] == 1071
assert reg["merge_commit"] == "2a0bb9ee116c0de7f9a5e20c4c56b8cd76134d75"
assert reg["parallel_same_serial_pr"] == 1070
assert reg["parallel_same_serial_disposition"] == "CLOSED_UNMERGED_NOT_CANONICAL"
assert reg["advance_to_checkpoint50"] is False
assert reg["next_derived_route"] == "27-20-r302g"

sync = json.loads(read(S27 / "27-20-r302d-f" / "controller-sync-delta.json"))
assert sync["global_controller_rewritten"] is False
assert sync["base_main_sha"] == "2a0bb9ee116c0de7f9a5e20c4c56b8cd76134d75"
for route in ("Stage27-20-r302d", "Stage27-20-r302e", "Stage27-20-r302f"):
    assert sync["stage20_delta"][route]["status"] == "AUDITED_PASS_MERGED"
    assert sync["stage20_delta"][route]["audit_status"] == "PASS"
assert sync["stage20_delta"]["merge_commit"] == "2a0bb9ee116c0de7f9a5e20c4c56b8cd76134d75"
assert sync["stage20_delta"]["advance_allowed"] is True
assert sync["stage20_delta"]["parallel_same_serial_disposition"] == "CLOSED_UNMERGED_NOT_CANONICAL"

print("Stage27-20-r302d-f merged lifecycle verification: PASS")
