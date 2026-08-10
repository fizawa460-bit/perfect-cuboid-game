from pathlib import Path

root = Path(__file__).resolve().parents[4]
au = (root / "stages/stage14/14-toolbox-au/result.md").read_text()
template = (root / "docs/stage14-toolbox/adapter-promotion-certificate-template.md").read_text()
cf = (root / "stages/stage14/14-4cf/result.md").read_text()
t57 = (root / "stages/stage14/14-t57/result.md").read_text()

required = [
    "STAGE14_TOOLBOX_AU=COMPLETE_ADAPTER_CERTIFICATE_TEMPLATES_AND_PROMOTION_CHECKLIST",
    "S_CURRENT_RECEIVER=BalancedFourHostGaussianSquareDivisorIncidence",
    "S_FIXED_HOST_DIVISOR_BOUND_SUFFICIENT=false",
    "FIXED_U_CURRENT_RECEIVER=SharedUPhysicalToroidalMellinCorrelation",
    "FIXED_U_KERNEL_CERTIFICATE_IMPORTED=true",
    "FIXED_U_PHYSICAL_SELECTOR_CORRELATION_REQUIRED=true",
    "PARTIAL_CERTIFICATE_PROMOTION_ALLOWED=false",
    "TOOLBOX_H_CONTINUATION_NEEDED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
]
for token in required:
    assert token in au, token

assert "BALANCED_FOUR_HOST_GAUSSIAN_SQUARE_DIVISOR_INCIDENCE_PROVED=false" in cf
assert "FIXED_HOST_BOUND_GLOBALIZES_TO_POWER_SAVING=false" in cf
assert "FIXED_U_ONE_FIELD_RANK1_KUMMER_CERTIFICATE_PROVED=true" in t57
assert "TWO_PRIME_KERNEL_SPECTRAL_REASSEMBLY_FIXED_POWER_LOSS=0" in t57
assert "SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED=false" in t57

for token in [
    "PROMOTION_READY=false",
    "FOUR_HOST_SIMULTANEITY_PRESERVED=false",
    "MOVING_HOST_UNIFORMITY_PROVED=false",
    "TOROIDAL_MELLIN_CORRELATION_PROVED=false",
    "MIXED_BRANCH_PROMOTION_READY=false",
]:
    assert token in template, token

print("Stage14-toolbox-au promotion-certificate audit: OK")
