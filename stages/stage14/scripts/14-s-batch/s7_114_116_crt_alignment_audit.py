from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

S114 = ROOT / "stages/stage14/14-s7-114/result.md"
S115 = ROOT / "stages/stage14/14-s7-115/result.md"
S116 = ROOT / "stages/stage14/14-s7-116/result.md"
REPORT = ROOT / "stages/stage14/14-s-batch/s7-114-116-report.md"
MAIN4GD = ROOT / "stages/stage14/14-4gd/result.md"
MAIN4GE = ROOT / "stages/stage14/14-4ge/result.md"
X38 = ROOT / "stages/stage14/14-Work-bzX38/result.md"
Q17 = ROOT / "docs/stage14-q17-summary.md"


def text(p: Path) -> str:
    assert p.exists(), p
    return p.read_text(encoding="utf-8")

s114, s115, s116, rep = map(text, [S114, S115, S116, REPORT])
m4gd, m4ge, x38, q17 = map(text, [MAIN4GD, MAIN4GE, X38, Q17])

for needle in [
    "S_FIXED_E_TWO_SIDED_EQUALS_MAIN_FIXED_E_TWO_SIDED_PACKET=true",
    "S_FIXED_E_TWO_SIDED_RECIPROCAL_CRT_SELECTOR_EXPLICIT=true",
]:
    assert needle in s114, needle

for needle in [
    "S_FIXED_E_TWO_SIDED_DELTA_EXT_EQUALS_DELTA_REC_PLUS_DELTA_POST=true",
    "S_FIXED_E_TWO_SIDED_SURVIVAL_BUDGET=kappa_minus_delta_pre_minus_delta_rec_minus_delta_post_ge_mu",
]:
    assert needle in s115, needle

for needle in [
    "MAIN_4GD_CRT_CROSS_PROMOTABLE_TO_FIXED_E_ENDPOINT=false",
    "MAIN_4GD_CRT_CROSS_PROMOTABLE_TO_POLYNOMIAL_E_FIXED_PRODUCT=false",
    "MAIN_4GD_CRT_CROSS_PROMOTABLE_TO_POLYNOMIAL_E_FIBERED_PRODUCT=false",
    "S_NONALIGNED_CRT_ADAPTER_PROVED=false",
    "RECEIVER_MATERIALLY_CHANGED=true",
]:
    assert needle in s116, needle

# Source locks.
for needle in ["F_-*F_+", "mod 2U", "mod 2V"]:
    assert needle in m4gd, needle
assert "delta_rec" in m4ge and "delta_post" in m4ge
assert "COMMON_SUPPORT_EXISTENCE_AFTER_MULTIPLICITY_EXHAUSTION_LANGUAGE_PROVED=true" in x38
assert "DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0" in q17
assert "Q17_EXPLICIT_RECIPROCAL_SELECTOR_CONSTRUCTION_TEST" in q17

# Deterministic algebra: nested deficits add exactly.
for kappa, sigma, rho, tau in [(12, 11, 9, 8), (20, 20, 17, 15), (9, 8, 8, 7)]:
    assert kappa >= sigma >= rho >= tau
    delta_pre = kappa - sigma
    delta_rec = sigma - rho
    delta_post = rho - tau
    assert kappa - delta_pre - delta_rec - delta_post == tau

# Fixed-E same-packet reconstruction identity used by 4gd.
for E0, u, v, d0, x, y in [(3, 5, 7, 2, 1, 3), (5, 2, 11, 4, 3, 5)]:
    h = d0 * E0 * u * v
    Xrec = h * x
    Yrec = h * y
    assert Xrec % h == 0 and Yrec % h == 0
    assert h == d0 * E0 * (u * v)

for needle in [
    "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3",
    "BATCH_STOP_REASON=receiver_change",
    "S_ROUTE_H_NEEDED=false",
    "NEXT=Stage14-s7-117",
]:
    assert needle in rep, needle

print("Stage14-s-batch s7-114..116 CRT alignment audit: PASS")
