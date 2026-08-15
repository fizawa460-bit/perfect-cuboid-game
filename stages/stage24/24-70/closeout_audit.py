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
        "POSITIVE_POWER_LOWER_BOUND_PROVED=false",
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
for name, body in text.items():
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

# Submission controller lock.
if controller.get("stage") != "Stage24":
    raise SystemExit("controller stage mismatch")
if controller.get("checkpoint_status", {}).get("70") != "SUBMITTED_FOR_FRESH_AUDIT":
    raise SystemExit("controller checkpoint70 not submitted for fresh audit")
state = controller.get("state", {})
expected = {
    "CURRENT_CHECKPOINT": 70,
    "AUDIT_STATUS": "PENDING",
    "ADVANCE_ALLOWED": False,
    "NEXT_CHECKPOINT": 70,
    "MERGE_ALLOWED": False,
}
for key, value in expected.items():
    if state.get(key) != value:
        raise SystemExit(f"controller {key}: expected {value!r}, got {state.get(key)!r}")

cp70 = controller.get("checkpoint70", {})
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
