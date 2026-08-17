#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def read(rel):
    return (ROOT / rel).read_text()


def require(text, needle):
    assert needle in text, needle

k = read("stages/stage27/27-20-r301k/result.md")
l = read("stages/stage27/27-20-r301l/result.md")
m = read("stages/stage27/27-20-r301m/result.md")
audit = read("stages/stage27/27-20-r301g-j/audit.md")
oldreg = json.loads(read("stages/stage27/27-20-r301g-j/batch-registry.json"))
reg = json.loads(read("stages/stage27/27-20-r301k-m/batch-registry.json"))
ctl = json.loads(read("stages/stage27/27-controller.json"))

require(audit, "AUDIT_VERDICT=PASS")
require(audit, "PR_MERGE_COMMIT=d53f4a4bb74e86c9e0ea38a0e12124c9b3bab30c")
assert oldreg["status"] == "AUDITED_PASS_MERGED"
assert oldreg["audit_status"] == "PASS"
assert oldreg["merge_allowed"] is True
assert oldreg["fresh_reaudit_required"] is False

for suffix in "ghij":
    key = f"Stage27-20-r301{suffix}"
    route = ctl["derived_routes"][key]
    assert route["status"] == "AUDITED_PASS_MERGED", (key, route["status"])
    assert route["audit_status"] == "PASS", (key, route["audit_status"])
    assert route["merge_allowed"] is True

require(k, "J_INVARIANT_FORMULA_PROVED=true")
require(k, "DELTA_GEOMETRIC_TWIST_ONLY=true")
require(k, "PHYSICAL_J_FIBER_MULTIPLICITY_LE_2=true")
require(k, "J_MAP_SUPPORT_SAVING_PROVED=false")

for xv in (Fraction(2), Fraction(3, 2), Fraction(5, 3)):
    lam = xv ** -4
    j_leg = 256 * (1 - lam + lam * lam) ** 3 / (lam * lam * (1 - lam) ** 2)
    j_x = 256 * (xv**8 - xv**4 + 1) ** 3 / (xv**8 * (xv**4 - 1) ** 2)
    assert j_leg == j_x

require(l, "ODD_TWIST_PRIME_SUPPORT_SUBSET_DEGENERATION_SUPPORT=true")
require(l, "MINIMAL_WEIERSTRASS_MODEL_AUDITED=false")
require(l, "CONDUCTOR_EQUALITY_PROVED=false")
require(l, "TWO_ADIC_CONDUCTOR_CLASSIFIED=false")

require(m, "Q1_AND_J_SUPPORT_EXPONENTS_EQUAL=true")
require(m, "SQUARECLASS_MULTIPLICITY_PER_J_SUBPOWER=true")
require(m, "MODULI_MAX_FIBER_PROGRESS_GATE=sigma+phi<1/2")
require(m, "MODULI_SECOND_MOMENT_PROGRESS_GATE=sigma+eta<1")
require(m, "HEIGHT_ONLY_MODULI_SUPPORT_ROUTE_CLOSED=true")
require(m, "MODULI_REPARAMETRIZATION_FIXED_POWER_SAVING_PROVED=false")

assert reg["status"] == "AUDITED_PASS_MERGED"
assert reg["audit_status"] == "PASS"
assert reg["merge_allowed"] is True
assert reg["fresh_reaudit_required"] is False
assert reg["next_derived_route"] == "27-20-r301n"

for suffix in "klm":
    key = f"Stage27-20-r301{suffix}"
    route = ctl["derived_routes"][key]
    assert route["status"] == "AUDITED_PASS_MERGED"
    assert route["audit_status"] == "PASS"
    assert route["merge_allowed"] is True
    assert route["advance_allowed"] is True

assert ctl["state"]["CURRENT_CHECKPOINT"] == 40
assert ctl["state"]["NEXT_CHECKPOINT"] == 40
assert ctl["state"]["ADVANCE_ALLOWED"] is False

for text in (k, l, m):
    require(text, "STRICT_SUB_SQRT_UPPER_PROVED=false")
    require(text, "NEW_MU_LT_HALF_PROVED=false")
    require(text, "TRUE_N2_EXPONENT_IDENTIFIED=false")

print("Stage27-20-r301k-m verifier: PASS")
