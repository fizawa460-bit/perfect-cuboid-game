from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

S117 = ROOT / "stages/stage14/14-s7-117/result.md"
S118 = ROOT / "stages/stage14/14-s7-118/result.md"
S119 = ROOT / "stages/stage14/14-s7-119/result.md"
REPORT = ROOT / "stages/stage14/14-s-batch/s7-117-119-report.md"
WORK = ROOT / "stages/stage14/14-Work-caX39/result.md"
H = ROOT / "stages/stage14/14-4ghH/result.md"
X13 = ROOT / "stages/stage14/14-X13/result.md"
S100 = ROOT / "stages/stage14/14-s7-100/result.md"
S101 = ROOT / "stages/stage14/14-s7-101/result.md"


def text(path: Path) -> str:
    assert path.exists(), path
    return path.read_text(encoding="utf-8")

s117, s118, s119, report = map(text, [S117, S118, S119, REPORT])
work, hsrc, x13, s100, s101 = map(text, [WORK, H, X13, S100, S101])

# Merged-source locks.
assert "RESTRICTED_MAIN_S_FIXED_E_TWO_SIDED_ADAPTER_PROVED=true" in work
assert "MINIMAL_UNRESOLVED_EXTERNAL_GATE=UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment" in hsrc
assert "ROW_CRT_LIFT_INDEPENDENT_SUPPORT=false" in x13
assert "POST_COLUMN_ROW_RECONSTRUCTION_MULTIPLICITY=B^o(1)" in x13
assert "FIXED_M_BRANCH_XR_LINEAR_IN_E=true" in s100
assert "FIXED_E_ENDPOINT_ONE_DIMENSIONAL_SUPPORT=true" in s101

# New boundary locks.
for needle in [
    "S_FIXED_E_TWO_SIDED_BRANCH_PARKED=true",
    "S_ROUTE_GLOBALLY_BLOCKED_BY_MAIN_H=false",
    "S_NONALIGNED_REALIZATIONS_REMAIN_ACTIVE=true",
]:
    assert needle in s117, needle

for needle in [
    "S_ENDPOINT_X13_COLUMN_FIXED_SQUARECLASS=true",
    "S_FIXED_PRODUCT_X13_COLUMN_FIXED_SQUARECLASS=true",
    "S_POLYNOMIAL_PAIR_X13_COLUMN_FIXED_SQUARECLASS_IN_n=true",
    "POLYNOMIAL_PAIR_OUTER_MEASURE_COLLAPSED_TO_n=false",
]:
    assert needle in s118, needle

for needle in [
    "S_SQUARECLASS_REVERSE_WITNESS_SET_DEFINED=true",
    "S_SQUARECLASS_REVERSE_WITNESS_MULTIPLICITY=Bo1",
    "S_SQUARECLASS_REVERSE_EXISTENCE_AUTOMATIC=false",
    "S_SQUARECLASS_OUTER_MEASURE_COMMON=false",
    "RECEIVER_MATERIALLY_CHANGED=true",
]:
    assert needle in s119, needle

# Endpoint square-class identity.
alpha, beta, E0, r0 = 3, 5, 7, 2
r_ep, s_ep, eps_x, eps_k = 2, 3, 1, 1
for t in [1, 4, 9]:
    Xr = alpha * E0 * r0 * r0
    Yr = beta * E0 * t * t
    M = 4 * r_ep * s_ep * Xr * Yr * eps_x * eps_k
    M0 = 4 * r_ep * s_ep * (alpha * E0 * r0 * r0) * (beta * E0) * eps_x * eps_k
    assert M == M0 * t * t

# Fixed-product E square-class identity.
alpha, beta, u0, v0 = 2, 11, 3, 5
for E in [2, 7, 12]:
    Xr = alpha * u0 * u0 * E
    Yr = beta * v0 * v0 * E
    assert Xr * Yr == (alpha * beta * u0 * u0 * v0 * v0) * E * E

# Polynomial pair square-class host is n=Euv, without claiming outer-measure collapse.
alpha, beta = 7, 13
for E, u, v in [(2, 3, 5), (5, 4, 7), (9, 5, 8)]:
    n = E * u * v
    Xr = alpha * E * u * u
    Yr = beta * E * v * v
    assert Xr * Yr == alpha * beta * n * n

# One exact two-layer reverse factor-pair reconstruction example.
U, V = 1, 2
F2m, F2p = 4, 12
assert F2m * F2p == 48
cp = (F2p + F2m) // 2
_dq = (F2p - F2m) // 2
assert 2 * cp == F2p + F2m
assert 2 * _dq == F2p - F2m
c, p = 2, 4
d, q = 1, 4
assert c * p == cp and d * q == _dq
W1 = 4 * p * q
F1m, F1p = 4, 16
assert F1m * F1p == W1
assert (F1p + F1m) % (2 * U) == 0
assert (F1p - F1m) % (2 * V) == 0
a = (F1p + F1m) // (2 * U)
b = (F1p - F1m) // (2 * V)
assert (a * U - b * V) * (a * U + b * V) == W1

for needle in [
    "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3",
    "BATCH_STOP_REASON=receiver_change",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "S_ROUTE_H_NEEDED=false",
    "NEXT=Stage14-s7-120",
    "STAGE14_AUTOMATION_SAFE=true",
    "STAGE14_ROUTE=s",
]:
    assert needle in report, needle

print("STAGE14_S_BATCH_S7_117_119_AUDIT=PASS")
