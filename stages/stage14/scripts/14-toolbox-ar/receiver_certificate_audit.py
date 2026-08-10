#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[4]
aq = (root / "stages/stage14/14-toolbox-aq/result.md").read_text()
t55 = (root / "stages/stage14/14-t55/result.md").read_text()
doc = (root / "docs/stage14-toolbox/receiver-ready-import-certificate.md").read_text()
result = (root / "stages/stage14/14-toolbox-ar/result.md").read_text()

for token in [
    "COMMON_ENVELOPE_IS_ESTIMATE=false",
    "RECEIVER_CROSS_PROMOTION_ALLOWED=false",
]:
    assert token in aq

for token in [
    "SHARED_U_INVISIBLE_COMPLETE_PROJECTIVE_TRACE_PROVED=true",
    "SHARED_U_CONSTANT_DENSITY_MEAN_CLOSED=true",
    "SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED=false",
]:
    assert token in t55

for token in [
    "LargeSwitchPrimitivePythagoreanTwoLegIncidence",
    "SharedUInvisibleCenteredProjectiveSelectorDispersion",
    "Missing labels, masks, centering, scale, or supersession metadata force",
]:
    assert token in doc

required = [
    "STAGE14_TOOLBOX_AR=COMPLETE_RECEIVER_READY_IMPORT_CERTIFICATES_AND_STALE_CONTRACT_GUARD",
    "MERGED_S7_19_IMPORTED=true",
    "MERGED_T55_IMPORTED=true",
    "PRIME_PAIR_PROJECTIVE_SLOPE_DISPERSION_CURRENT=false",
    "SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED=false",
    "RECEIVER_CERTIFICATE_MISSING_FIELD_DEFAULTS_READY=false",
    "STALE_RECEIVER_IMPORT_ALLOWED=false",
    "COMPLETE_TRACE_IMPLIES_PHYSICAL_SELECTOR_DISPERSION=false",
    "RECEIVER_CROSS_PROMOTION_ALLOWED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
    "TOOLBOX_H_CONTINUATION_NEEDED=false",
]
for token in required:
    assert token in result, f"missing ar guard: {token}"

assert "STALE_RECEIVER_IMPORT_ALLOWED=true" not in result
assert "COMPLETE_TRACE_IMPLIES_PHYSICAL_SELECTOR_DISPERSION=true" not in result
print("stage14-toolbox-ar receiver certificate audit: PASS")
