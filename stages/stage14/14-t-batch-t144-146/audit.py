from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def text(rel):
    return (ROOT / rel).read_text()


t143 = text('stages/stage14/14-t143/result.md')
t144 = text('stages/stage14/14-t144/result.md')
t145 = text('stages/stage14/14-t145/result.md')
t146 = text('stages/stage14/14-t146/result.md')
t65 = text('stages/stage14/14-t65/result.md')
t82 = text('stages/stage14/14-t82/result.md')
t140 = text('stages/stage14/14-t140/result.md')

# Predecessor / frozen boundary locks.
assert 'NEXT=Stage14-t144' in t143
# t65 writes the exact relation in LaTeX, not ASCII variable names.
assert 'hk=\\varepsilon m' in t65
assert 'D_Ubeta <= m/2' in t82
assert 'Y/(h*k0)+1' in t140

# t144 host provenance.
for token in [
    'SELECTOR_MODULUS_HOSTED_BY_FIXED_U=true',
    'HK0_EQUALS_ETA_EPSILON_M=true',
    'ENDPOINT_SELECTOR_HEIGHT_COUPLING_EXACT=true',
    'BEYOND_MITSUI_ENDPOINT_FORCES_LARGE_FIXED_U_NORM=true',
    'RECEIVER_MATERIALLY_CHANGED=false',
    'NEXT=Stage14-t145',
]:
    assert token in t144, token

# t145 refined capacity.
for token in [
    'HOST_NORMALIZED_ENDPOINT_CAPACITY_EXACT=true',
    'ENDPOINT_CAPACITY_EXPONENT=max(2lambda-rho,lambda)',
    'BEYOND_MITSUI_HOST_CAPACITY_FIXED_POWER_SAVING=false',
    'RECEIVER_MATERIALLY_CHANGED=false',
    'NEXT=Stage14-t146',
]:
    assert token in t145, token

# Algebraic exponent audit: max(2lambda-rho,lambda)>=1/2 is necessary.
def capacity_exp(lam, rho):
    return max(2*lam-rho, lam)

# Below both thresholds: cannot carry sqrt-scale principal mass.
assert capacity_exp(0.34, 0.20) < 0.5
# Host-normalized threshold lambda=1/4+rho/2.
rho = 0.20
lam = 0.25 + rho/2
assert abs((2*lam-rho)-0.5) < 1e-12
# Near-full alternative can reach 1/2 independently of host term.
assert capacity_exp(0.50, 0.40) >= 0.5

# t146 material receiver change and H decision.
for token in [
    'ENDPOINT_PRINCIPAL_CAPACITY_DICHOTOMY_PROVED=true',
    'HOST_NORMALIZED_WIDTH_FLOOR=BsQuarterTimesSqrtHK0',
    'BEYOND_MITSUI_ENDPOINT_PSEUDOPOLYNOMIAL_WIDTH_GAIN_PROVED=true',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    'T_ROUTE_H_NEEDED=false',
    'TH33_NEEDED=false',
    'NEXT=Stage14-t147',
]:
    assert token in t146, token

print('Stage14-t-batch t144-t146 audit: OK')
