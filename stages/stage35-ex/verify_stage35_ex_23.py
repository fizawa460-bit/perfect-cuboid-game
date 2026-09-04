#!/usr/bin/env python3
import json
from pathlib import Path
from itertools import combinations
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "stages/stage35-ex/35ex-23/genus5-character-quotient-uniformity-blocker.md"
CERT = ROOT / "stages/stage35-ex/35ex-23/character-quotient-certificate.json"
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"

doc = DOC.read_text()
cert = json.loads(CERT.read_text())
state = json.loads(STATE.read_text())

V21 = "STAGE35_EX_PESCH_E1_STATE_V21_POST_35EX22_OBVIOUS_BRAUER_SYMBOL_BLOCKER"
V22 = "STAGE35_EX_PESCH_E1_STATE_V22_POST_35EX23_GENUS5_CHARACTER_QUOTIENT_UNIFORMITY_BLOCKER"
assert state["schema"] in {V21, V22}
assert state["stage"] == "35-EX"
assert state["status"] == "ACTIVE_RESEARCH_NO_CREDIT"
assert state["base_main_sha"] in {
    "378096fa313b582b63553b395ec85a5c86de2685",
    "2e07dde92fdf270fff1233635a7cb4cea1427080",
}

assert cert["schema"] == "STAGE35_EX_23_GENUS5_CHARACTER_QUOTIENT_CERTIFICATE_V1"
assert cert["authority"]["hostile_reaudit_review"] == 5111539148
assert cert["authority"]["audited_head_sha"] == "f4276680239bb2b84687f8ba8ac8964de0613552"
assert cert["authority"]["merged_main_sha"] == "2e07dde92fdf270fff1233635a7cb4cea1427080"
assert cert["generic_fiber"]["genus"] == 5
assert cert["generic_fiber"]["deck_group"] == "(Z/2)^3"

# Seven nontrivial characters and their generic quotient genera.
subsets = []
for k in (1, 2, 3):
    subsets.extend(combinations((1, 2, 3), k))
assert len(subsets) == 7
genera = [len(I)-1 for I in subsets]
assert genera.count(0) == 3
assert genera.count(1) == 3
assert genera.count(2) == 1
assert cert["character_quotients"]["nontrivial_count"] == 7
assert cert["character_quotients"]["genus_counts"] == {"0":3,"1":3,"2":1}

# Exact quotient-product identities.
y, q, z, w, a = sp.symbols("y q z w a")
f1, f2, f3 = y**2+1, y**2+a, y**2+1+a
rels = {q**2:f1, z**2:f2, w**2:f3}
for lhs, rhs in [
    ((q*z)**2, f1*f2),
    ((q*w)**2, f1*f3),
    ((z*w)**2, f2*f3),
    ((q*z*w)**2, f1*f2*f3),
]:
    assert sp.expand(lhs.subs(rels) - rhs) == 0

# Genus-two quotient -> two elliptic quotients.
X, H = sp.symbols("X H")
sextic = (y**2+1)*(y**2+a)*(y**2+1+a)
plus_rhs = (X+1)*(X+a)*(X+1+a)
minus_rhs = X*(X+1)*(X+a)*(X+1+a)
assert sp.expand(plus_rhs.subs(X, y**2) - sextic) == 0
assert sp.expand(minus_rhs.subs(X, y**2) - y**2*sextic) == 0
assert cert["genus_two_split"]["proved"] is True
assert cert["full_differential_accounting"]["dimension"] == 5

# Differential eigenspace accounting: three pair characters plus two parities
# inside the 123 character.  These five labels are pairwise distinct.
eigen_labels = [
    ((1,1,0),0),
    ((1,0,1),0),
    ((0,1,1),0),
    ((1,1,1),0),
    ((1,1,1),1),
]
assert len(set(eigen_labels)) == 5
assert cert["full_differential_accounting"]["proved"] is True
assert cert["full_differential_accounting"]["generic_fiber_jacobian_five_elliptic_isogeny"] is True

# Derive the pair-quartic j formula from the four branch points +/-u, +/-v.
u, v = sp.symbols("u v", nonzero=True)
lam = ((u-v)/(u+v))**2
j_leg = sp.factor(256*(1-lam+lam**2)**3/(lam**2*(1-lam)**2))
j_pair_uv = 16*(u**4+14*u**2*v**2+v**4)**3/(u**2*v**2*(u**2-v**2)**4)
assert sp.factor(j_leg-j_pair_uv) == 0

j12 = 16*(a**2+14*a+1)**3/(a*(a-1)**4)
j13 = 16*(a**2+16*a+16)**3/(a**4*(a+1))
j23 = 16*(16*a**2+16*a+1)**3/(a*(a+1))

# Eplus: finite roots -1,-a,-1-a; one Legendre parameter is -a/(1-a).
lam_plus = -a/(1-a)
jplus = sp.factor(256*(1-lam_plus+lam_plus**2)**3/(lam_plus**2*(1-lam_plus)**2))
assert sp.factor(jplus - 256*(a**2-a+1)**3/(a**2*(a-1)**2)) == 0

# Eminus: branch points 0,-1,-a,-1-a.
e1,e2,e3,e4 = 0,-1,-a,-1-a
lam_minus = sp.factor(((e1-e3)*(e2-e4))/((e1-e4)*(e2-e3)))
jminus = sp.factor(256*(1-lam_minus+lam_minus**2)**3/(lam_minus**2*(1-lam_minus)**2))
assert sp.factor(jminus - 256*(a**4-a**2+1)**3/(a**4*(a-1)**2*(a+1)**2)) == 0

expected = {
    "E12": j12,
    "E13": j13,
    "E23": j23,
    "Eplus": jplus,
    "Eminus": jminus,
}
for name, expr in expected.items():
    stated = sp.sympify(cert["j_invariants"][name].replace("^", "**"))
    assert sp.factor(expr-stated) == 0
    assert sp.factor(sp.diff(expr, a)) != 0

assert cert["uniformity"]["all_five_elliptic_factors_nonisotrivial"] is True
assert cert["uniformity"]["fixed_elliptic_curve_reduction_from_character_quotients"] is False
assert cert["uniformity"]["uniform_fixed_MW_computation_unlocked"] is False
assert cert["uniformity"]["all_elliptic_surface_or_compatibility_arguments_ruled_out"] is False
assert cert["uniformity"]["fresh_breadth_audit_required"] is True
assert cert["arsenal"]["S31_W01"]["blob_sha"] == "122a6c1c5c871c1c7b797017e854de8ec55e7c50"
assert cert["arsenal"]["S34_W02_unlocked"] is False

for marker in (
    "GENUS5_NONTRIVIAL_CHARACTER_QUOTIENTS=7",
    "GENUS0_CHARACTER_QUOTIENTS=3",
    "GENUS1_CHARACTER_QUOTIENTS=3",
    "GENUS2_CHARACTER_QUOTIENTS=1",
    "GENUS2_BIELLIPTIC_SPLIT_PROVED=true",
    "TOTAL_ELLIPTIC_FACTORS_AFTER_SPLIT=5",
    "FULL_GENUS5_DIFFERENTIAL_ACCOUNTING=true",
    "GENERIC_FIBER_JACOBIAN_FIVE_ELLIPTIC_ISOGENY=true",
    "ALL_FIVE_ELLIPTIC_FACTORS_NONISOTRIVIAL=true",
    "FIXED_ELLIPTIC_CURVE_REDUCTION_FROM_CHARACTER_QUOTIENTS=false",
    "UNIFORM_FIXED_MW_COMPUTATION_UNLOCKED=false",
    "FRESH_BREADTH_AUDIT_REQUIRED=true",
    "E1_PROVED=false",
):
    assert marker in doc

for key in (
    "new_theorem_credit",
    "global_surface_rational_points_classified",
    "E1_proved",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert cert["claims"][key] is False

print("PASS STAGE35_EX_23_GENUS5_CHARACTER_QUOTIENT_UNIFORMITY_BLOCKER")
