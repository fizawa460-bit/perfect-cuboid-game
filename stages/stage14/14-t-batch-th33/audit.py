from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    return (ROOT / rel).read_text()

target = text('stages/stage14/14-t157/th33-target.md')
res = text('stages/stage14/14-tH33/result.md')
matrix = text('stages/stage14/14-tH33/primary-source-matrix.md')

assert 'TARGET_FROZEN=true' in target
assert 'REQUESTED_OBJECT=SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio' in target
assert 'd^2 > exp(sqrt(log X)/C_K)' in target
assert 'R>=B^theta' in target

for tok in [
    'STAGE14_TH33=COMPLETE_NEGATIVE_UNRESOLVED_SUPER_KAI_INDIVIDUAL_RESIDUE_GATE_AUDIT',
    'DIRECT_THEOREM_APPLICABLE=false',
    'SUPER_KAI_INDIVIDUAL_RESIDUE_LONG_INTERVAL_COVERED=false',
    'BEST_CERTIFIED_INDIVIDUAL_MODULUS_RANGE=d^2_LE_exp_sqrtlogX_over_CK',
    'FIXED_POWER_HEADROOM_USED=true',
    'POSSIBLE_SIEGEL_ZERO_RETAINED=true',
    'AVERAGING_REQUIRED=true',
    'SUPER_KAI_LONG_FIXED_POWER_DEPLETION_RULED_OUT=false',
    'FIXED_U_H_COMPLETED=true',
    'FIXED_U_BLOCKED_BY_H=true',
    'NEXT_H_NEEDED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    'NEXT=UNRESOLVED_EXTERNAL_GATE:SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio',
]:
    assert tok in res, tok

for tok in [
    'DIRECT_FULL_TARGET_THEOREM_COUNT=0',
    'AVERAGED_BEYOND_KAI_RESULTS_CHARGEABLE=false',
    'LEAST_PRIME_OR_PRODUCT_EXISTENCE_SUFFICIENT=false',
    'UNRESOLVED_EXTERNAL_GATE=SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio',
]:
    assert tok in matrix, tok

# The target must be genuinely outside the completed direct range.
assert 'd^2 <= exp(sqrt(log X)/C_K)' in res
assert 'd^2 > exp(sqrt(log X)/C_K)' in res

print('Stage14-t-batch tH33 audit: OK')
