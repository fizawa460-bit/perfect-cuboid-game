from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    return (ROOT / rel).read_text()

t155 = text('stages/stage14/14-t155/result.md')
t156 = text('stages/stage14/14-t156/result.md')
t157 = text('stages/stage14/14-t157/result.md')
target = text('stages/stage14/14-t157/th33-target.md')

assert 'NEXT=Stage14-t156' in t155

for tok in [
    'KAI_INADMISSIBLE_LONG_FORCES_PSEUDOPOLYNOMIAL_MODULUS_LOWER_BOUND=true',
    'KAI_INADMISSIBLE_SPARSE_LONG_PRINCIPAL_MODULUS_CUBE_CAP=true',
    'KAI_INADMISSIBLE_AREA_LONG_PRINCIPAL_MODULUS_FIFTH_POWER_CAP=true',
    'RECEIVER_MATERIALLY_CHANGED=false',
    'TH33_NEEDED=false',
    'NEXT=Stage14-t157',
]:
    assert tok in t156, tok

for tok in [
    'SPARSE_AREA_LONG_SHARE_SAME_POINTWISE_PRIME_THEOREM=true',
    'TH33_TARGET_MATERIALLY_NARROWER_THAN_TH30=true',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'T_ROUTE_H_NEEDED=true',
    'T_ROUTE_H_REQUEST=SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio',
    'TH33_NEEDED=true',
    'TH33_EXECUTED=false',
    'NEXT=Stage14-tH33',
]:
    assert tok in t157, tok

for tok in [
    'TARGET_FROZEN=true',
    'REQUESTED_OBJECT=SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio',
    'd^2 > exp(sqrt(log X)/C_K)',
    'R>=B^theta',
    'T(X;d,beta_*) >= B^(-o(1)) M(X;d)',
    'POSSIBLE_SIEGEL_ZERO_RETAINED',
]:
    assert tok in target, tok

# Algebraic compatibility exponents from t156.
# sparse: d^3 <= B^(1/2+o(1)) -> d <= B^(1/6+o(1))
assert abs(0.5/3 - 1/6) < 1e-12
# area: d^5 <= B^(1/2+o(1)) -> d <= B^(1/10+o(1))
assert abs(0.5/5 - 1/10) < 1e-12

print('Stage14-t-batch t156-t157 audit: OK')
