from pathlib import Path
from math import gcd, isqrt

repo = Path(__file__).resolve().parents[3]
paths = {
    "t117": repo / "stages/stage14/14-t117/result.md",
    "t118": repo / "stages/stage14/14-t118/result.md",
    "t119": repo / "stages/stage14/14-t119/result.md",
    "t120": repo / "stages/stage14/14-t120/result.md",
    "work": repo / "stages/stage14/14-Work-boX27/result.md",
}
for name, path in paths.items():
    assert path.exists(), (name, path)
texts = {name: path.read_text() for name, path in paths.items()}

for token in [
    "EXCEPTIONAL_NORM_FACTOR_DEFINED_AS_EU_SMOOTH_MULTIPLIER=true",
    "EXCEPTIONAL_LOCAL_PREDICATE_DEPENDS_ONLY_ON_EXCEPTIONAL_MULTIPLIER=true",
    "LOCAL_ADMISSIBLE_NORM_SUPPORT_IS_EXACT_MULTIPLIER_CYLINDER_UNION=true",
    "NEXT=Stage14-t119",
]:
    assert token in texts["t118"], token

for token in [
    "EXCEPTIONAL_MULTIPLIER_FAMILY_SIZE=Bo1",
    "EXCEPTIONAL_MULTIPLIER_RANKIN_BOUND_PROVED=true",
    "EXCEPTIONAL_MULTIPLIER_MAY_BE_FROZEN_AT_BO1_COST=true",
    "GENERIC_SCALAR_NORM_IS_ONLY_REMAINING_POLYNOMIAL_COFACTOR_COORDINATE=true",
    "NEXT=Stage14-t120",
]:
    assert token in texts["t119"], token

for token in [
    "GENERIC_NORM_SUPPORT_RELOCATION_APPLIED=true",
    "ORIENTATION_DENSITY_AS_INDEPENDENT_POWER_SOURCE_SUPERSEDED=true",
    "EXCEPTIONAL_LOCAL_DENSITY_AS_INDEPENDENT_POWER_SOURCE_SUPERSEDED=true",
    "GENERIC_PHYSICAL_NORM_SUPPORT_IS_POLYNOMIAL_OUTER_RECEIVER=true",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "NEXT=Stage14-t121",
]:
    assert token in texts["t120"], token

assert "SUBPOLYNOMIAL_FIBER_SUPPORT_RELOCATION_LEMMA_PROVED=true" in texts["work"]
assert "FIXED_U_THREE_MECHANISM_SAVING_TRICHOTOMY_PROVED=true" in texts["t117"]

for text in (texts["t118"], texts["t119"], texts["t120"]):
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in text
    assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in text
    assert "T_ROUTE_H_NEEDED=false" in text

# Exact exceptional/generic factorization on small synthetic samples.
def prime_factors(n):
    out = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out

E_primes = {5, 13}
for n in range(1, 400):
    m = 1
    g = n
    for p in E_primes:
        while g % p == 0:
            m *= p
            g //= p
    assert n == m * g
    assert gcd(g, 5 * 13) == 1
    assert prime_factors(m) <= E_primes

# Support-relocation finite guard: accepted outer support weight never exceeds accepted mass.
weights = {1: 3, 2: 5, 3: 2, 4: 7}
fibers = {
    1: [0, 1],
    2: [0, 0, 0],
    3: [1],
    4: [0, 1, 1],
}
M = sum(weights[g] * sum(fibers[g]) for g in weights)
S_weight = sum(weights[g] for g in weights if any(fibers[g]))
assert S_weight <= M

print("Stage14-t-batch t118-t120 audit: OK")
