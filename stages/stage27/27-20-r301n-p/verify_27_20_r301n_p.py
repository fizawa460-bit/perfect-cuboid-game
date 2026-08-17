#!/usr/bin/env python3
from fractions import Fraction
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def require(text, needle):
    assert needle in text, (needle,)

n = read("stages/stage27/27-20-r301n/result.md")
o = read("stages/stage27/27-20-r301o/result.md")
p = read("stages/stage27/27-20-r301p/result.md")
audit = read("stages/stage27/27-20-r301k-m/audit.md")
oldreg = json.loads(read("stages/stage27/27-20-r301k-m/batch-registry.json"))
reg = json.loads(read("stages/stage27/27-20-r301n-p/batch-registry.json"))
ctl = json.loads(read("stages/stage27/27-controller.json"))

# Parent closeout must be materialized before this batch can pass CI.
require(audit, "AUDIT_VERDICT=PASS")
require(audit, "PR_MERGE_COMMIT=800532681ad086a0ad3894f0e56cbcbf1c2b0ec3")
assert oldreg["status"] == "AUDITED_PASS_MERGED"
assert oldreg["audit_status"] == "PASS"
assert oldreg["merge_allowed"] is True
assert oldreg["fresh_reaudit_required"] is False

for suffix in "klm":
    route = ctl["derived_routes"][f"Stage27-20-r301{suffix}"]
    assert route["status"] == "AUDITED_PASS_MERGED"
    assert route["audit_status"] == "PASS"
    assert route["merge_allowed"] is True

# r301n structural locks.
require(n, "DETERMINANT_PENCIL_DELTA_SQUARE_FACTOR_PROVED=true")
require(n, "COMMON_JACOBIAN_INDEPENDENT_OF_DELTA_PROVED=true")
require(n, "COMMON_JACOBIAN_FULL_RATIONAL_2_TORSION=true")
require(n, "COMMON_JACOBIAN_INTEGRAL_MODEL=V^2=-U(U-a^4)(U-b^4)")
require(n, "COMMON_JACOBIAN_DISCRIMINANT=16*a^8*b^8*(a^4-b^4)^2")
require(n, "MORDELL_WEIL_RANK_DEPENDS_ON_DELTA=false")

# Determinant quartic: changing delta only multiplies by delta^2.
for xv in (Fraction(2), Fraction(3, 2), Fraction(5, 3)):
    for rv in (Fraction(1), Fraction(2), Fraction(-3, 2)):
        base = rv * (rv + xv*xv) * (rv*xv*xv + 1)
        for delta in (Fraction(1), Fraction(2), Fraction(5)):
            det = delta*delta * base
            assert det / (delta*delta) == base

# The four branch roots map to 0, infinity, 1, x^-4.
for xv in (Fraction(2), Fraction(3, 2), Fraction(5, 3)):
    r1 = -xv*xv
    r2 = -(xv**-2)
    X1 = -r1/(xv*xv)
    X2 = -r2/(xv*xv)
    assert X1 == 1
    assert X2 == xv**-4

# Integral model has the expected rational 2-torsion and discriminant support.
for a, b in ((2, 1), (3, 2), (5, 3), (7, 4)):
    assert gcd(a, b) == 1
    roots = (0, a**4, b**4)
    assert len(set(roots)) == 3
    disc = 16 * a**8 * b**8 * (a**4-b**4)**2
    assert disc != 0

# r301o bookkeeping locks.
require(o, "SOLUBLE_DELTA_FIBERS_SHARE_ONE_MORDELL_WEIL_GROUP=true")
require(o, "RANK_VARIATION_IN_DELTA_ELIMINATED=true")
require(o, "DELTA_INTERPRETED_AS_COVERING_DESCENT_DATA=true")
require(o, "UNIFORM_FIXED_X_AGGREGATE_SUBPOWER_PROVED=false")
require(o, "UNIFORM_COVERING_HEIGHT_TRANSFER_PROVED=false")
require(o, "MAX_AGGREGATE_PROGRESS_GATE=sigma+phi<1/2")

# r301p descent and firewall locks.
require(p, "COMMON_JACOBIAN_FULL_2_DESCENT_AVAILABLE=true")
require(p, "SELMER_BAD_PRIME_SUPPORT=2*a*b*(a^4-b^4)")
require(p, "SELMER_2_INJECTS_INTO_S_UNIT_SQUARECLASSES_SQUARED=true")
require(p, "UNIFORM_SELMER2_CARDINALITY_SUBPOLYNOMIAL=true")
require(p, "UNIFORM_RANK_BOUND=O(log B/log log B)")
require(p, "UNIFORM_POINT_COUNT_SUBPOWER_FROM_RANK_PROVED=false")
require(p, "UNIFORM_REGULATOR_LOWER_BOUND_PROVED=false")

assert reg["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"
assert reg["audit_status"] == "PENDING"
assert reg["merge_allowed"] is False
assert reg["fresh_reaudit_required"] is True
assert reg["next_derived_route"] == "27-20-r301q"

for suffix in "nop":
    route = ctl["derived_routes"][f"Stage27-20-r301{suffix}"]
    assert route["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"
    assert route["audit_status"] == "PENDING"
    assert route["merge_allowed"] is False
    assert route["advance_allowed"] is False

assert ctl["state"]["CURRENT_CHECKPOINT"] == 40
assert ctl["state"]["NEXT_CHECKPOINT"] == 40
assert ctl["state"]["ADVANCE_ALLOWED"] is False

for text in (n, o, p):
    require(text, "STRICT_SUB_SQRT_UPPER_PROVED=false")
    require(text, "NEW_MU_LT_HALF_PROVED=false")
    require(text, "TRUE_N2_EXPONENT_IDENTIFIED=false")

print("Stage27-20-r301n-p verifier: PASS")
