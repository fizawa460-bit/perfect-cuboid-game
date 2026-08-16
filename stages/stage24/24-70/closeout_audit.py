#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

FILES = {
    "final": ROOT / "stages/stage24/final.md",
    "result": ROOT / "stages/stage24/24-70/result.md",
    "ledger": ROOT / "stages/stage24/24-70/aggressive-search-ledger.md",
    "manifest": ROOT / "stages/stage24/manifest-r01.md",
    "arsenal": ROOT / "docs/stage24-arsenal-promotion.md",
    "controller": ROOT / "stages/stage24/24-controller.json",
}

for name, path in FILES.items():
    if not path.exists():
        raise SystemExit(f"missing required artifact: {name}: {path}")

text = {name: path.read_text(encoding="utf-8") for name, path in FILES.items() if name != "controller"}
controller = json.loads(FILES["controller"].read_text(encoding="utf-8"))

required_everywhere = {
    "final": [
        "STAGE24_CLASS=THIN_BUT_INFINITE",
        "POSITIVE_POWER_LOWER_BOUND_PROVED=false",
        "MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false",
        "TRUE_TARGET_EXPONENT_IDENTIFIED=false",
        "PERFECT_CUBOID_CONCLUSION=NONE",
        "SYNTHESIS_STOP_RULE_SATISFIED=YES",
        "FRESH_HOSTILE_REVIEW=PENDING",
    ],
    "result": [
        "STAGE24_CLASS=THIN_BUT_INFINITE",
        "POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=false",
        "MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false",
        "TRUE_TARGET_EXPONENT_IDENTIFIED=false",
        "SYNTHESIS_STOP_RULE_SATISFIED=YES",
        "NEXT_EXPECTED_COMMAND=Stage24-audit",
    ],
    "manifest": [
        "STAGE24_CLASS=THIN_BUT_INFINITE",
        "TARGET_UNBOUNDEDNESS=true",
        "POSITIVE_POWER_LOWER_BOUND_PROVED=false",
        "PERFECT_CUBOID_CONCLUSION=NONE",
        "CHECKPOINT70=PENDING_FRESH_AUDIT",
    ],
    "arsenal": [
        "TRANSITION_CLASS=THIN_BUT_INFINITE",
        "POSITIVE_POWER_LOWER_BOUND_PROVED=true",
        "CURRENT_POSITIVE_POWER_LOWER_BOUND=N2(B)>>B^(1/4)",
        "C17_STATUS=PARKED_PARITY_EXAMPLE_SUPERSEDED_AS_GLOBAL_LOWER",
        "TRUE_TARGET_EXPONENT_IDENTIFIED=false",
        "PERFECT_CUBOID_CONCLUSION=NONE",
    ],
    "ledger": [
        "FRESH_UPPER_SURGEON_EXECUTED=true",
        "FRESH_LOWER_SURGEON_EXECUTED=true",
        "INTERACTION_DOUBLE_CHARGE_AUDIT_EXECUTED=true",
        "SYNTHESIS_STOP_RULE_SATISFIED=YES",
    ],
}

for name, markers in required_everywhere.items():
    for marker in markers:
        if marker not in text[name]:
            raise SystemExit(f"{name}: missing marker {marker}")

# The core theorem species must be printed in both proof-facing artifacts.
for name in ("final", "result"):
    for snippet in (
        "sqrt{\\log B}",
        "B^{-1}(\\log B)^{-9/2}",
        "B^{-1/2+\\varepsilon}(\\log B)^{-5}",
    ):
        if snippet not in text[name]:
            raise SystemExit(f"{name}: missing theorem snippet {snippet}")

# Reject accidental overclaims in closeout text.
for name in ("final", "result", "manifest", "ledger"):
    body = text[name]
    forbidden = [
        "POSITIVE_POWER_LOWER_BOUND_PROVED=true",
        "MATCHING_HALF_POWER_LOWER_BOUND_PROVED=true",
        "TRUE_TARGET_EXPONENT_IDENTIFIED=true",
        "HALF_POWER_INTRINSIC_PROVED=true",
        "PERFECT_CUBOID_CONCLUSION=EXISTS",
        "PERFECT_CUBOID_CONCLUSION=NONEXISTENT",
    ]
    for marker in forbidden:
        if marker in body:
            raise SystemExit(f"{name}: forbidden overclaim marker {marker}")

# Controller lock: accept either the pre-audit submission state or the
# post-audit certified state. This keeps the same verifier useful after the
# fresh audit is durably persisted on the PR branch.
if controller.get("stage") != "Stage24":
    raise SystemExit("controller stage mismatch")

cp70_status = controller.get("checkpoint_status", {}).get("70")
state = controller.get("state", {})
cp70 = controller.get("checkpoint70", {})

if cp70_status == "SUBMITTED_FOR_FRESH_AUDIT":
    expected = {
        "CURRENT_CHECKPOINT": 70,
        "AUDIT_STATUS": "PENDING",
        "ADVANCE_ALLOWED": False,
        "NEXT_CHECKPOINT": 70,
        "MERGE_ALLOWED": False,
    }
    for key, value in expected.items():
        if state.get(key) != value:
            raise SystemExit(f"submission controller {key}: expected {value!r}, got {state.get(key)!r}")
    if cp70.get("fresh_hostile_review") != "PENDING":
        raise SystemExit("submission checkpoint70 fresh_hostile_review is not PENDING")
elif cp70_status == "PROVED_AUDITED_PASS":
    expected = {
        "CURRENT_CHECKPOINT": 70,
        "MAIN_STATUS": "COMPLETE",
        "AUDIT_STATUS": "PASS",
        "ADVANCE_ALLOWED": True,
        "NEXT_CHECKPOINT": "",
        "MERGE_ALLOWED": True,
    }
    for key, value in expected.items():
        if state.get(key) != value:
            raise SystemExit(f"audited controller {key}: expected {value!r}, got {state.get(key)!r}")
    if controller.get("status") != "CLOSED_PENDING_MERGE":
        raise SystemExit("audited controller top-level status is not CLOSED_PENDING_MERGE")
    if cp70.get("audit") != "PASS" or cp70.get("fresh_hostile_review") != "PASS":
        raise SystemExit("audited checkpoint70 does not record PASS")
    audit_path = ROOT / cp70.get("audit_path", "")
    if not audit_path.exists():
        raise SystemExit(f"audited checkpoint70 missing audit record: {audit_path}")
    if controller.get("discovery_audit", {}).get("verdict") != "PASS":
        raise SystemExit("audited discovery_audit verdict is not PASS")
    if controller.get("audit_persistence", {}).get("unsynced_audit_state") != "NONE":
        raise SystemExit("audited controller has unsynced audit state")
else:
    raise SystemExit(f"unsupported checkpoint70 controller status: {cp70_status!r}")

for key in (
    "self_contained_bundle_materialized",
    "arsenal_promotion_materialized",
    "aggressive_search_ledger_materialized",
    "synthesis_stop_rule_satisfied",
):
    if cp70.get(key) is not True:
        raise SystemExit(f"controller checkpoint70 {key} is not true")

print("STAGE24_70_CLOSEOUT_AUDIT=PASS")
print("THEOREM_STATUS_SYNC=PASS")
print("OVERCLAIM_FIREWALL=PASS")
print("ARTIFACT_CONTRACT=PASS")
print(f"CONTROLLER_STATE={cp70_status}")
