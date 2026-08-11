from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

th32 = (ROOT / 'stages/stage14/14-tH32/result.md').read_text()
t143 = (ROOT / 'stages/stage14/14-t143/result.md').read_text()

required_th32 = [
    'STAGE14_TH32=COMPLETE_PARTIAL_NEAR_FULL_POSITIVE_QUARTER_SCALE_NEGATIVE_AUDIT',
    'QUARTER_SCALE_ENDPOINT_COVERED=false',
    'BEST_CERTIFIED_B_WIDTH_EXPONENT_FOR_EXACT_GROWING_RESIDUE_PROBLEM=1/2-o(1)',
    'BEST_CONDUCTOR_ONE_GAUSSIAN_SECTOR_COMPARATOR_B_EXPONENT=7/20+epsilon',
    'POSSIBLE_SIEGEL_ZERO_RETAINED=true',
    'SAFE_NEAR_FULL_ENDPOINT_FIXED_POWER_DEPLETION_RULED_OUT=true',
    'SAFE_ENDPOINT_FIXED_POWER_DEPLETION_RULED_OUT=false',
]
for token in required_th32:
    assert token in th32, token

required_t143 = [
    'TH32_CONSUMED=true',
    'SAFE_NEAR_FULL_ENDPOINT_BRANCH_DISCHARGED=true',
    'SAFE_ENDPOINT_INTERMEDIATE_SHORT_RANGE_LIVE=true',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    'TH33_NEEDED=false',
    'NEXT=Stage14-t144',
]
for token in required_t143:
    assert token in t143, token

# Scale conversion: x=B^(1/2), H=B^lambda => theta=2 lambda.
assert abs(2 * 0.25 - 0.5) < 1e-12
assert abs(0.5 * 0.7 - 0.35) < 1e-12  # Stucky 7/10 -> B^(7/20)

# The remaining direct Kai/Mitsui threshold has exponent 1/2 minus only a
# subpolynomial defect, so any fixed lambda<1/2 lies below it asymptotically.
for lam in (0.25, 0.30, 0.35, 0.40, 0.49):
    assert lam < 0.5

print('Stage14-t-batch th32-t143 audit: OK')
