from fractions import Fraction
from math import gcd
from pathlib import Path

repo = Path(__file__).resolve().parents[4]
paths = {
    "ey": repo / "stages/stage14/14-4ey/result.md",
    "ez": repo / "stages/stage14/14-4ez/result.md",
    "fa": repo / "stages/stage14/14-4fa/result.md",
    "report": repo / "stages/stage14/14-4-batch/4ey-4fa-report.md",
    "s29": repo / "stages/stage14/14-s7-29/result.md",
    "s46": repo / "stages/stage14/14-s7-46/result.md",
    "ex": repo / "stages/stage14/14-4ex/result.md",
}
for name, path in paths.items():
    assert path.exists(), (name, path)
texts = {name: path.read_text() for name, path in paths.items()}

for token in [
    "XI_AGREEMENT_PRODUCT_RECONSTRUCTED_FROM_K_AND_Z=true",
    "FIXED_K_Z_TO_U_V_MULTIPLICITY=Bo1",
    "NEXT=Stage14-4ez",
]:
    assert token in texts["ey"], token

for token in [
    "D_OVER_G_DIVIDES_RAD_Z=true",
    "AGREEMENT_KERNEL_OVERLAP_EXPONENT_LOWER_BOUND=4phi-1/2",
    "UNIFORM_AGREEMENT_KERNEL_OVERLAP_LOWER_BOUND=1/3",
    "NEXT=Stage14-4fa",
]:
    assert token in texts["ez"], token

for token in [
    "LARGE_G_COMMON_CORE_ROOT_LINE_FIBER=Bo1",
    "HEAVY_RAY_PRIMITIVE_AGREEMENT_PAIR_POLYNOMIAL_FREEDOM_REMOVED=true",
    "UNIFORM_FIXED_AGREEMENT_RADIAL_SCALE_COUNT_MAX=B^(1/24+o(1))",
    "HEAVY_RAY_CLOSED=false",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "NEXT=Stage14-4fb",
]:
    assert token in texts["fa"], token

assert "gcd(C,oddpart(R*J))=1" in texts["s29"]
assert "U*V=oddpart(R*J)" in texts["s46"]
assert "pairwise coprime and squarefree" in texts["s46"]
assert "RADIAL_H_TO_MOVING_PRODUCT_T_INJECTIVE=true" in texts["ex"]

# Exponent identities on the full square-root band.
phis = [Fraction(5, 24), Fraction(11, 48), Fraction(1, 4)]
for phi in phis:
    chi = 2 * phi - Fraction(1, 4)
    d_exp = 2 * phi
    z_exp = Fraction(1, 2) - 2 * phi
    g_min = d_exp - z_exp
    residual_rootline = d_exp - g_min - chi
    h_exp = z_exp / 2
    assert g_min == 4 * phi - Fraction(1, 2)
    assert g_min >= Fraction(1, 3)
    assert residual_rootline == Fraction(3, 4) - 4 * phi
    assert residual_rootline <= Fraction(-1, 12)
    assert h_exp == Fraction(1, 4) - phi
    assert h_exp <= Fraction(1, 24)

# Finite squareclass sanity: if D=sf(K*Z), then D/gcd(D,K) divides rad(Z).
def sf(n: int) -> int:
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p += 1
    if n > 1:
        out *= n
    return out

def rad(n: int) -> int:
    out = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            out *= p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out *= n
    return out

for K in range(1, 80):
    if sf(K) != K:
        continue
    for Z in range(1, 120):
        D = sf(K * Z)
        G = gcd(D, K)
        assert rad(Z) % (D // G) == 0

assert "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3" in texts["report"]
assert "BATCH_STOP_REASON=receiver_change" in texts["report"]
assert "NEXT=Stage14-4fb" in texts["report"]

print("Stage14-4 batch 4ey-4fa audit: OK")
