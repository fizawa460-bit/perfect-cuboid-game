#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[4]
ar = (root / "stages/stage14/14-toolbox-ar/result.md").read_text()
s719 = (root / "stages/stage14/14-s7-19/result.md").read_text()
t55 = (root / "stages/stage14/14-t55/result.md").read_text()
shortlist = (root / "docs/stage14-toolbox/current-receiver-theorem-shortlist.md").read_text()
result = (root / "stages/stage14/14-toolbox-as/result.md").read_text()

for token in [
    "S_CURRENT_RECEIVER=LargeSwitchPrimitivePythagoreanTwoLegIncidence",
    "FIXED_U_CURRENT_RECEIVER=SharedUInvisibleCenteredProjectiveSelectorDispersion",
    "RECEIVER_CROSS_PROMOTION_ALLOWED=false",
    "COMPLETE_TRACE_IMPLIES_PHYSICAL_SELECTOR_DISPERSION=false",
]:
    assert token in ar, f"missing ar certificate: {token}"

for token in [
    "LARGE_SWITCH_PRIMITIVE_PYTHAGOREAN_TWO_LEG_INCIDENCE_POWER_SAVING_PROVED=false",
    "NEXT=Stage14-s7-20",
]:
    assert token in s719, f"missing s7-19 boundary: {token}"

for token in [
    "SHARED_U_INVISIBLE_COMPLETE_PROJECTIVE_TRACE_PROVED=true",
    "SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED=false",
]:
    assert token in t55, f"missing t55 boundary: {token}"

for token in [
    "No candidate below is `DIRECT`.",
    "Wilson, Jacobi bilinear forms over hyperbolic regions",
    "Ping Xi, bilinear forms with trace functions over arbitrary sets",
    "No additional toolbox-H line is needed",
]:
    assert token in shortlist, f"missing shortlist gate: {token}"

required = [
    "STAGE14_TOOLBOX_AS=COMPLETE_THEOREM_SOURCE_SHORTLIST_AND_ADAPTER_GATES",
    "DIRECT_IMPORTABLE_THEOREM_COUNT=0",
    "S_WILSON_DIRECT_IMPORT_VALID=false",
    "S_EXACT_JACOBI_ADAPTER_PROVED=false",
    "FIXED_U_PING_XI_DIRECT_IMPORT_VALID=false",
    "FIXED_U_ONE_FIELD_TRACE_SHEAF_CERTIFICATE_PROVED=false",
    "POST_SQUARECLASS_QUADRATIC_LARGE_SIEVE_NONCIRCULAR=false",
    "DIRECT_FI_GAUSSIAN_SYMBOL_TRANSFER_VALID=false",
    "COMPLETE_TRACE_IMPLIES_SPARSE_SELECTOR_DISPERSION=false",
    "RECEIVER_CROSS_PROMOTION_ALLOWED=false",
    "S_AND_FIXED_U_ADAPTERS_PARALLEL_SAFE=true",
    "TOOLBOX_H_CONTINUATION_NEEDED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
]
for token in required:
    assert token in result, f"missing as guard: {token}"

for forbidden in [
    "DIRECT_IMPORTABLE_THEOREM_COUNT=1",
    "S_WILSON_DIRECT_IMPORT_VALID=true",
    "FIXED_U_PING_XI_DIRECT_IMPORT_VALID=true",
    "POST_SQUARECLASS_QUADRATIC_LARGE_SIEVE_NONCIRCULAR=true",
    "RECEIVER_CROSS_PROMOTION_ALLOWED=true",
]:
    assert forbidden not in result, f"forbidden promotion: {forbidden}"

print("stage14-toolbox-as theorem shortlist audit: PASS")
