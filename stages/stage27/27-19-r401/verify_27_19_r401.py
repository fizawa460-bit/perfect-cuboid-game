#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parents[3]


def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding="utf-8")


def data(rel):
    return json.loads(text(rel))


r501 = text("stages/stage25/25-50/r501-parametric-positive-power.md")
r507 = text("stages/stage25/25-60/r507-primitive-height-rigidity.md")
r502 = text("stages/stage25/25-60/r502-primitive-height-no-upgrade.md")
r505 = text("stages/stage25/25-60/r505-common-core-gate.md")
s19 = text("stages/stage19/post-stage25-50-supersession.md")
res = text("stages/stage27/27-19-r401/result.md")
reg = data("stages/stage27/27-19-r401/lower-family-registry.json")
ctl = data("stages/stage27/27-controller.json")
status = text("docs/00_CURRENT_RESEARCH_STATUS.md")

# Authoritative current Stage19 lower, not the historical constant floor.
assert "CURRENT_LOWER=N2(B)>>B^(1/4)" in s19
assert "UNBOUNDEDNESS_PROVED=true" in s19
assert "TRUE_TARGET_EXPONENT_IDENTIFIED=false" in s19

# Known audited lower families: exact count/height ledger and saturation.
assert "HEIGHT_DEGREE=8" in r501
assert "PARAMETER_COUNT_DEGREE=2" in r501
assert "R501_EXACT_FAMILY_GROWTH=Theta(B^(1/4))" in r507
assert "R501_HIDDEN_GCD_EXPONENT_UPGRADE=false" in r507
assert "R502_PRIMITIVE_HEIGHT_DEGREE=8" in r502
assert "R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))" in r502
assert "R502_HIDDEN_GCD_EXPONENT_UPGRADE=false" in r502

# Prior common-core audit already identifies the correct stronger-lower species.
assert "R505_EXACT_TARGET_RECEIVER=true" in r505
assert "R505_SPACE_CONDITION=sf(A)=sf(B)" in r505
assert "R505_REMAINING_GATE=WHOLE_FAMILY_PHYSICAL_HEIGHT_UNIFORMITY_OR_GENUINELY_NEW_PARAMETRIC_FAMILY" in r505

# Exact exponent calculus.
assert Fraction(2, 8) == Fraction(1, 4)
for lam, q, should_cross in [
    (Fraction(1, 4), Fraction(1, 2), True),
    (Fraction(1, 8), Fraction(1, 2), False),
    (Fraction(1, 2), Fraction(2, 1), False),
    (Fraction(3, 4), Fraction(2, 1), True),
]:
    crosses = Fraction(2, 1) + lam > Fraction(1, 4) * (Fraction(8, 1) + q)
    assert crosses == (4 * lam > q)
    assert crosses == should_cross

# Check the normalized toric identities on exact rational samples.
for m, n, r, s in [(5, 2, 7, 3), (7, 3, 4, 1), (9, 2, 5, 4)]:
    x = Fraction(m, n)
    y = Fraction(r, s)
    A = m*m*r*r + n*n*s*s
    B = m*m*s*s + n*n*r*r
    scale = n*n*s*s
    assert Fraction(A, scale) == x*x*y*y + 1
    assert Fraction(B, scale) == x*x + y*y

for marker in [
    "LOWER_FAMILY_EXPONENT_CALCULUS_PROVED=true",
    "LOWER_PROGRESS_GATE=kappa/h>1/4",
    "COUPLED_OUTER_PARAMETER_GATE=4*lambda>q",
    "MASTER_SPACE_RECEIVER_DERIVED=true",
    "MASTER_SPACE_RECEIVER=x^2*y^2+1=z^2*(x^2+y^2)",
    "MASTER_SURFACE_DOMINANT_RATIONAL_PARAMETRIZATION_PROVED=false",
    "LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false",
    "FINITE_DATA_USED_AS_PROOF=false",
    "NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit",
]:
    assert marker in res, marker

assert reg["current_beta"] == "1/4"
assert reg["exponent_calculus"]["progress_gate"] == "kappa/h>1/4"
assert reg["exponent_calculus"]["outer_leaf_progress_gate"] == "4*lambda>q"
assert reg["master_space_receiver"]["condition"] == "x^2*y^2+1=z^2*(x^2+y^2)"
assert reg["master_space_receiver"]["dominant_rational_parametrization_proved"] is False
assert reg["lower_exponent_above_one_quarter_proved"] is False

# Lifecycle: 40ae is audited+merged; lower reentry is pending hostile audit.
ae = ctl["derived_routes"]["Stage27-40ae"]
lr = ctl["derived_routes"]["Stage27-19-r401"]
assert ae["status"] == "INTERMEDIATE_AUDITED_PASS_MERGED"
assert ae["audit_status"] == "PASS"
assert ae["pr"] == 1030
assert ae["merge_commit"] == "2b2bfb0768006e2fe66969726486ac765c589bbc"
assert lr["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
assert lr["route_kind"] == "LOWER_REENTRY"
assert lr["lower_exponent_above_one_quarter_proved"] is False
assert lr["audit_status"] == "PENDING"
assert ctl["state"]["CURRENT_CHECKPOINT"] == 40
assert ctl["state"]["AUDIT_STATUS"] == "PENDING"
assert ctl["state"]["MERGE_ALLOWED"] is False
assert ctl["next_expected_command"] == "Stage27-19-r401-audit"
assert "CURRENT_STAGE=Stage27-19-r401-SUBMITTED-PENDING-FRESH-AUDIT" in status
assert "STAGE27_40AE_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1030" in status
assert "STAGE27_19_R401_STATUS=LOWER_REENTRY_SUBMITTED_PENDING_FRESH_AUDIT" in status

print("STAGE27_19_R401_CURRENT_LOWER=PASS")
print("STAGE27_19_R401_QUARTER_SATURATION=PASS")
print("STAGE27_19_R401_EXPONENT_CALCULUS=PASS")
print("STAGE27_19_R401_MASTER_RECEIVER=PASS")
print("STAGE27_19_R401_LIFECYCLE=PASS")
