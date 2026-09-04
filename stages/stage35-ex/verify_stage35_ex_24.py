#!/usr/bin/env python3
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "stages/stage35-ex/35ex-24/five-elliptic-isogeny-twist-compression.md"
CERT = ROOT / "stages/stage35-ex/35ex-24/isogeny-twist-certificate.json"
AUDIT = ROOT / "stages/stage35-ex/35ex-23/post-five-elliptic-breadth-audit.json"
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"

doc = DOC.read_text()
cert = json.loads(CERT.read_text())
audit = json.loads(AUDIT.read_text())
state = json.loads(STATE.read_text())

V23 = "STAGE35_EX_PESCH_E1_STATE_V23_POST_35EX24_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION"
assert state["schema"] == V23
assert state["stage"] == "35-EX"
assert state["status"] == "ACTIVE_RESEARCH_NO_CREDIT"
assert state["base_main_sha"] == "8c59c81bcf0bcd442705cfb7a3db297253b34679"

parent = state["parent_authority"]
assert parent["unit"] == "35EX-23"
assert parent["hostile_audit_verdict"] == "PASS"
assert parent["hostile_audit_review"] == 5111910947
assert parent["audited_head_sha"] == "77ff0a6cf51679bd64525a0be843fcd1eed77d8e"
assert parent["merged_main_sha"] == "c20ee71d91af850103fd7406f9b1072448a11fcf"
assert parent["audited_theorem_credit"] is False

assert audit["schema"] == "STAGE35_EX_23B_POST_FIVE_ELLIPTIC_FRESH_BREADTH_AUDIT_V1"
assert audit["authority"]["hostile_audit_review"] == 5111910947
assert audit["blind_rediscovery"]["generation_input"].startswith("only the exact 35EX-23 equations")
assert audit["arsenal_comparison"]["performed_after_blind_generation"] is True
assert audit["selection"]["selected_candidate"] == "E1-FIVE-ELLIPTIC-ISOGENY-TWIST-COMPRESSION"
assert audit["selection"]["selected_next_unit"] == "35EX-24_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_OR_INDEPENDENT_CHANNEL_BLOCKER"
assert audit["cycle_exit"]["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert audit["cycle_exit"]["CYCLE_BLIND_REDISCOVERY"] is True
assert audit["cycle_exit"]["CYCLE_LIVE_CANDIDATES"] == 1
assert audit["cycle_exit"]["CYCLE_UNTESTED_CANDIDATES"] == 4
assert audit["arsenal_comparison"]["S31-W01"]["blob_sha"] == "122a6c1c5c871c1c7b797017e854de8ec55e7c50"
assert audit["arsenal_comparison"]["S34-W03"]["blob_sha"] == "1d5275321f42768a6414d4610ac912c63be43f96"
assert audit["arsenal_comparison"]["S34-W02"]["blob_sha"] == "13d41be776fcd2edcd258f11bd28c5a6596de45b"
assert audit["arsenal_comparison"]["S31-WF01"]["blob_sha"] == "feb9a0581d378beccd1dc58cf9dd20e6c41347bc"

assert cert["schema"] == "STAGE35_EX_24_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_V1"
assert cert["status"] == "PROVISIONAL_EXACT_NO_CREDIT"
assert cert["authority"]["hostile_audit_review"] == 5111910947
assert cert["authority"]["audited_head_sha"] == "77ff0a6cf51679bd64525a0be843fcd1eed77d8e"
assert cert["authority"]["merged_main_sha"] == "c20ee71d91af850103fd7406f9b1072448a11fcf"

# General symmetric quartic -> cubic adapter.
r, s, y, V = sp.symbols("r s y V", nonzero=True)
d = r*s
c = r**2+s**2
U = 2*d*(V+d)/y**2
T = U+c
D = U**2-4*d**2
Y = y*D/(2*d)
quartic_rel = V**2-(y**2+r**2)*(y**2+s**2)
q_rhs = T*(T-(r+s)**2)*(T-(r-s)**2)
num = sp.factor(sp.together(Y**2-q_rhs).as_numer_denom()[0])
assert sp.rem(sp.Poly(sp.expand(num), V), sp.Poly(quartic_rel, V)).as_expr() == 0

# Exact inverse on the stated open.
T0, Y0 = sp.symbols("T0 Y0", nonzero=True)
D0 = (T0-(r+s)**2)*(T0-(r-s)**2)
y_inv = 2*d*Y0/D0
V_inv = (T0-c)*y_inv**2/(2*d)-d
assert sp.factor(y_inv.subs({T0:T, Y0:Y}, simultaneous=True)-y) == 0
assert sp.factor(V_inv.subs({T0:T, Y0:Y}, simultaneous=True)-V) == 0

# Kernel-(0,0) quotient: verify equation and invariance under translation by the kernel.
Z, W = sp.symbols("Z W", nonzero=True)
source_rhs = Z*(Z+r**2)*(Z+s**2)
Ti = Z+c+d**2/Z
Yi = W*(d**2-Z**2)/Z**2
iso_num = sp.factor(sp.together(Yi**2 - Ti*(Ti-(r+s)**2)*(Ti-(r-s)**2)).as_numer_denom()[0])
assert sp.rem(sp.Poly(sp.expand(iso_num), W), sp.Poly(W**2-source_rhs, W)).as_expr() == 0
Ztau = d**2/Z
Wtau = -d**2*W/Z**2
assert sp.factor(Ti.subs({Z:Ztau, W:Wtau}, simultaneous=True)-Ti) == 0
assert sp.factor(Yi.subs({Z:Ztau, W:Wtau}, simultaneous=True)-Yi) == 0
assert cert["kernel_two_isogeny"]["degree"] == 2
assert cert["kernel_two_isogeny"]["proved"] is True

# Specialize the three pair quotients.
a, x, p = sp.symbols("a x p", nonzero=True)
# E12 source L12 equals the -1 twist of translated Eplus under Z=-t.
t = sp.symbols("t")
L12_rhs = Z*(Z+1)*(Z+a)
Eplus_twist_rhs = -t*(t-1)*(t-a)
assert sp.expand(Eplus_twist_rhs.subs(t, -Z)-L12_rhs) == 0

# E23 source is exactly isomorphic to the -1 twist of F on the displayed open.
z = sp.symbols("z", nonzero=True)
U23 = -a*z/(z+1)
scale = a/(z+1)**2
Ftw_rhs = -z*(z+1)*(z+1+a)
L23_rhs = U23*(U23+a)*(U23+1+a)
assert sp.factor(L23_rhs-scale**2*Ftw_rhs) == 0

spec = cert["specializations"]
assert spec["E12"]["fixed_twist_minus_one_required"] is True
assert spec["E13"]["fixed_twist_minus_one_required"] is False
assert spec["E23"]["fixed_twist_minus_one_required"] is True
assert "Eplus^(-1)" in spec["E12"]["relation"]
assert spec["E13"]["relation"] == "E13 is K-2-isogenous to F"
assert "F^(-1)" in spec["E23"]["relation"]

# Three representative j-shapes are exact and nonconstant.
def j_leg(lam):
    return sp.factor(256*(1-lam+lam**2)**3/(lam**2*(1-lam)**2))

jplus = j_leg(a)
jF = j_leg(-a)
jminus = sp.factor(256*(a**4-a**2+1)**3/(a**4*(a-1)**2*(a+1)**2))
expected = {"Eplus": jplus, "F": jF, "Eminus": jminus}
for name, expr in expected.items():
    stated = sp.sympify(
        cert["representative_j_invariants"][name].replace("^", "**"),
        locals={"a": a},
    )
    assert sp.factor(expr-stated) == 0
    assert sp.factor(sp.diff(expr, a)) != 0

comp = cert["jacobian_compression"]
assert comp["over_K"] == "Jac(C) ~ Eplus * Eplus^(-1) * F * F^(-1) * Eminus"
assert comp["over_Ki"] == "Jac(C)_(K(i)) ~ Eplus^2 * F^2 * Eminus"
assert comp["Ki_multiplicities"] == [2,2,1]
assert comp["three_representative_compression_proved"] is True
assert comp["three_representatives_pairwise_nonisogenous_all_degrees_proved"] is False

u24 = state["completed_units"]["35EX-24"]
assert u24["status"] == "PROVISIONAL_EXACT_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_NO_CREDIT"
assert u24["jacobian_K_twist_pair_compression"] is True
assert u24["jacobian_Ki_three_representative_compression"] is True
assert u24["Ki_multiplicity_pattern"] == [2,2,1]
assert u24["fresh_breadth_audit_required_after_hostile_pass"] is True
assert u24["audited_theorem_credit"] is False
assert state["current"]["unit"] == "35EX-24_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_OR_INDEPENDENT_CHANNEL_BLOCKER"
assert state["current"]["status"] == "PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT"

for marker in (
    "PAIR_QUARTIC_EXACT_WEIERSTRASS_ADAPTER=true",
    "PAIR_QUARTIC_STANDARD_KERNEL_2_ISOGENY=true",
    "E12_K_2_ISOGENOUS_TO_MINUS1_TWIST_EPLUS=true",
    "E13_K_2_ISOGENOUS_TO_F=true",
    "E23_K_2_ISOGENOUS_TO_MINUS1_TWIST_F=true",
    "JACOBIAN_K_TWIST_PAIR_COMPRESSION=true",
    "JACOBIAN_KI_THREE_REPRESENTATIVE_COMPRESSION=true",
    "KI_MULTIPLICITY_PATTERN=2,2,1",
    "ALL_THREE_REPRESENTATIVE_J_FUNCTIONS_NONCONSTANT=true",
    "FIXED_ELLIPTIC_CURVE_REDUCTION_UNLOCKED=false",
    "UNIFORM_MW_CLOSURE_UNLOCKED=false",
    "FRESH_BREADTH_AUDIT_REQUIRED_AFTER_HOSTILE_PASS=true",
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
    if key in state["claims"]:
        assert state["claims"][key] is False

print("PASS STAGE35_EX_24_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_V1")
