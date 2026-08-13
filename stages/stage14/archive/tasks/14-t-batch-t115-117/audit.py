from fractions import Fraction
from pathlib import Path

repo = Path(__file__).resolve().parents[3]
paths = {
    "t114": repo / "stages/stage14/14-t114/result.md",
    "t115": repo / "stages/stage14/14-t115/result.md",
    "t116": repo / "stages/stage14/14-t116/result.md",
    "t117": repo / "stages/stage14/14-t117/result.md",
    "batch": repo / "stages/stage14/14-t-batch-t115-117/result.md",
}
for name, path in paths.items():
    assert path.exists(), (name, path)
texts = {name: path.read_text() for name, path in paths.items()}

for token in [
    "COFACTOR_PRINCIPAL_WEIGHT_DEPENDS_ONLY_ON_NORM=true",
    "WEIGHTED_COFACTOR_CORE_NORM_FIBER_TOWER_EXACT=true",
    "OUTER_NORM_COORDINATE_REMAINS_POLYNOMIAL_SCALE=true",
    "NEXT=Stage14-t116",
]:
    assert token in texts["t115"], token

for token in [
    "EXCEPTIONAL_GENERIC_ORIENTATION_SPLIT_EXACT=true",
    "LOCAL_FIXED_PACKET_INTERACTIONS_CONFINED_TO_EXCEPTIONAL_SUPPORT=true",
    "GENERIC_ORIENTATION_GLOBAL_BOOLEAN_REMAINS=true",
    "EXCEPTIONAL_LOCAL_NORM_SUPPORT_MAY_STILL_BE_POWER_THIN=true",
    "NEXT=Stage14-t117",
]:
    assert token in texts["t116"], token

for token in [
    "WEIGHTED_CORE_DENSITY_FACTORIZATION_EXACT=true",
    "GENERIC_ORIENTATION_PRINCIPAL_CENTERED_SPLIT_EXACT=true",
    "FIXED_U_THREE_MECHANISM_SAVING_TRICHOTOMY_PROVED=true",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "TH29_NEEDED=false",
    "NEXT=Stage14-t118",
]:
    assert token in texts["t117"], token

for text in (texts["t115"], texts["t116"], texts["t117"], texts["batch"]):
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in text
    assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in text

# t115 exact tower identity on finite synthetic norm fibers.
A = {5: Fraction(3, 2), 13: Fraction(5, 3), 17: Fraction(7, 4)}
R = {5: 4, 13: 8, 17: 2}
C = {5: 1, 13: 6, 17: 0}
H = sum(A[n] * R[n] for n in A)
M = sum(A[n] * C[n] for n in A)
rho_avg = sum(A[n] * R[n] * Fraction(C[n], R[n]) for n in A) / H
assert rho_avg == M / H

# t116 exceptional/generic mixture identity.
# Two exceptional labels, each with a four-point generic cube.
sigmas = [Fraction(3, 4), Fraction(1, 4)]
locals_ = [1, 0]
rho = sum(Fraction(L) * s for L, s in zip(locals_, sigmas)) / len(sigmas)
accepted = 3
background = 8
assert rho == Fraction(accepted, background)

# t117 product factorization and exponent-split dichotomy.
for H0 in range(1, 33):
    for Hloc in range(0, H0 + 1):
        for Mcore in range(0, Hloc + 1):
            lam = Fraction(Hloc, H0)
            sig = Fraction(Mcore, Hloc) if Hloc else Fraction(0)
            mu = Fraction(Mcore, H0)
            assert lam * sig == mu

# Model B^{-delta/2}=1/16 and B^{-delta/4}=1/4.
small_mu = Fraction(1, 16)
threshold = Fraction(1, 4)
for q in range(1, 65):
    for a in range(q + 1):
        lam = Fraction(a, q)
        for b in range(a + 1):
            sig = Fraction(b, a) if a else Fraction(0)
            mu = lam * sig
            if mu <= small_mu:
                assert lam <= threshold or sig <= threshold

assert "BATCH_SUBSTANTIVE_STAGE_COUNT=3" in texts["batch"]
assert "BATCH_STOP_REASON=receiver_change" in texts["batch"]
assert "T_ROUTE_H_NEEDED=false" in texts["batch"]
assert "NEXT=Stage14-t118" in texts["batch"]

print("Stage14-t-batch t115-t117 audit: OK")
