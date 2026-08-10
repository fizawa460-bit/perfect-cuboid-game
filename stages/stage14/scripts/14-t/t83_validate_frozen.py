#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
f = ROOT / "stages/stage14/data/14-t83/determinant_quotient_switch_frozen.json"
r = ROOT / "stages/stage14/14-t83/result.md"

data = json.loads(f.read_text())
b = data["boundary"]

assert data["stage"] == "14-t83"
assert data["gaussian_prime_vectors"] == 180
assert data["projective_norm_identity_checks"] == 52308
assert data["nonzero_determinant_checks"] == 52308
assert data["unit_companion_checks"] == 105834
assert data["determinant_quotient_budget_checks"] == 105834
assert data["full_disk_max_line_multiplicity"] == 2
assert b["DETERMINANT_QUOTIENT_SWITCH_PROVED"] is True
assert b["NONZERO_DETERMINANT_QUOTIENT_FORCED"] is True
assert b["TH23_CONSUMED"] is True
assert b["TH23_TARGET_REOPENED"] is False
assert b["TH24_NEEDED"] is False
assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"
assert b["STRICT_SUBSQRT_POWER_SAVING_PROVED"] is False
assert b["NEXT"] == "Stage14-t84"

text = r.read_text()
for lock in [
    "STAGE14_T83=COMPLETE_FIXED_U_DIVISOR_PROJECTIVE_INCIDENCE_TO_SHORT_NONZERO_DETERMINANT_QUOTIENT",
    "PURE_PROJECTIVE_INCIDENCE_EQUALS_INTEGER_DETERMINANT_DIVISIBILITY=true",
    "EXACT_INTEGER_PROJECTIVE_DIAGONAL_PHYSICAL=false",
    "DETERMINANT_QUOTIENT_SWITCH_PROVED=true",
    "DETERMINANT_QUOTIENT_PRODUCT_BUDGET=sqrt(2B/h)",
    "FIXED_DETERMINANT_QUOTIENT_COVER_MULTIPLICITY_AT_MOST=2",
    "SWITCHED_COMPANION_COORDINATE_UNIT_MOD_D=true",
    "FIXED_U_PACKET_POWER_SAVING_PROVED=false",
    "TH23_CONSUMED=true",
    "TH23_TARGET_REOPENED=false",
    "TH24_NEEDED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEXT=Stage14-t84",
]:
    assert lock in text, lock

print("Stage14-t83 frozen boundary validated")
