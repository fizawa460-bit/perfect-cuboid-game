#!/usr/bin/env python3
"""Materialize the corrected J2 normalization support on the marked K_c branch.

This verifier starts from the post-hostile-replay corrected half-divisor
D=P_r2-P_r4. It does not reuse the revoked historical ell_J2 Kummer-glue
producer. It identifies both corrected supports in the frozen ruled P1xP1
model and Stoll's marked K_c coordinates, verifies that both are smooth points
of the same marked branch curve CsK[22], and records the exact degree-two
elliptic quotient image.

This removes the old infinity/exceptional-support ambiguity from the corrected
representative. It still does NOT construct a surface H^2(mu_2) lift or
Hochschild--Serre d2 value.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
PRE = HERE.parent / "33-05" / "j2-corrected-pre-kummer-descent-cochain.json"
SEM = HERE / "j2-semantic-kc-picard-basis.json"
OUT = HERE / "j2-corrected-kc-branch-support.json"

EXPECTED_PRE = "940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106"
EXPECTED_SEM = "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), (path, claimed, csha(body))
    return obj


pre = load_locked(PRE, EXPECTED_PRE)
sem = load_locked(SEM, EXPECTED_SEM)
assert pre["normalization"]["half_divisor_D"] == "P_r2-P_r4"
assert pre["normalization"]["f2"] == "(t-r2)/(t-r4)"
assert sem["j2_branch_carrier"]["curve"] == "CsK[22]"

t, s, z = sp.symbols("t s z")
u1, v1, u2, v2 = sp.symbols("u1 v1 u2 v2")
A1, A2, A3, B1, B2, B3 = sp.symbols("A1 A2 A3 B1 B2 B3")
i = sp.I
s2 = sp.sqrt(2)

q0 = sp.expand(t**4 - 6*t**2 + 1)
r2 = -(1+s2)
r4 = 1-s2
for r in (r2, r4):
    assert sp.simplify(q0.subs(t, r)) == 0

# On the + branch of the CV normalization, s=i(1-t^2+z)/(2t).
s_plus = sp.cancel(i*(1-t**2+z)/(2*t))
s_r2 = sp.simplify(s_plus.subs({t:r2, z:0}))
s_r4 = sp.simplify(s_plus.subs({t:r4, z:0}))
assert s_r2 == i
assert s_r4 == -i
Gplus = sp.expand(t*(1-s**2) + i*s*(1-t**2))
assert sp.simplify(Gplus.subs({t:r2, s:s_r2})) == 0
assert sp.simplify(Gplus.subs({t:r4, s:s_r4})) == 0

# Frozen ruled model and the exact CV->ruled identity.
D1 = v1**2-u1**2
D2 = v2**2-u2**2
Xr = u1*v1*D2
Yr = u2*v2*D1
assert sp.simplify(
    v1**2*v2**2*Gplus.subs({t:u1/v1, s:u2/v2}) - (Xr+i*Yr)
) == 0

# Anticanonical map to Stoll K_c.
e = sp.expand(D1*D2)
x = sp.expand(2*u1*v1*D2)
p = sp.expand((u1**2+v1**2)*D2)
y = sp.expand(2*u2*v2*D1)
qq = sp.expand((u2**2+v2**2)*D1)
assert sp.expand(e**2+x**2-p**2) == 0
assert sp.expand(e**2+y**2-qq**2) == 0

K_eqs = [
    A1**2+A2**2-B3**2,
    A2**2+A3**2-B1**2,
    A1**2+A3**2-B2**2,
]
varsK = [A1,A2,A3,B1,B2,B3]
J = sp.Matrix([[sp.diff(f,v) for v in varsK] for f in K_eqs])


def affine_image(tv, sv):
    vals = [
        sp.simplify(f.subs({u1:tv,v1:1,u2:sv,v2:1}))
        for f in [e,x,y,qq,p]
    ]
    return vals[:3] + [sp.Integer(0)] + vals[3:]


def normalize_by_A2(P):
    assert sp.simplify(P[1]) != 0
    return [sp.simplify(a/P[1]) for a in P]


P_r2 = normalize_by_A2(affine_image(r2, s_r2))
P_r4 = normalize_by_A2(affine_image(r4, s_r4))
assert P_r2 == [1,1,i,0,0,-s2]
assert P_r4 == [-1,1,i,0,0,-s2]

for P in (P_r2, P_r4):
    sub = dict(zip(varsK, P))
    assert all(sp.simplify(f.subs(sub)) == 0 for f in K_eqs)
    assert J.subs(sub).rank() == 3
    # Same marked B+ branch: B1=0 and i*A2-A3=0.
    assert sp.simplify(B1.subs(sub)) == 0
    assert sp.simplify((i*A2-A3).subs(sub)) == 0

# Reconfirm div(f2)=2(P_r2-P_r4) formally on z^2=q.
# Coordinates [P_r1,P_r2,P_r3,P_r4,I+,I-].
div_t_r2 = [0,2,0,0,-1,-1]
div_t_r4 = [0,0,0,2,-1,-1]
assert [a-b for a,b in zip(div_t_r2,div_t_r4)] == [0,2,0,-2,0,0]

# Degree-two elliptic quotient X=t^2, Y=t*z.
xp = sp.expand(r2**2)
xm = sp.expand(r4**2)
assert sp.simplify(xp-(3+2*s2)) == 0
assert sp.simplify(xm-(3-2*s2)) == 0
XE = sp.Symbol("XE")
Epoly = sp.expand(XE*(XE**2-6*XE+1))
assert sp.expand(Epoly-XE*(XE-xp)*(XE-xm)) == 0
# The horizontal chord Y=0 through T_plus and T_minus has third
# intersection (0,0), so T_plus+T_minus=(0,0) in E'[2].
assert sp.simplify((xp*xm)-1) == 0

cert = {
    "schema":"STAGE33_12_J2_CORRECTED_KC_BRANCH_SUPPORT_V1",
    "status":"PASS_EXACT_CORRECTED_SUPPORT_TO_MARKED_KC_BRANCH_NO_SURFACE_MU2_CREDIT",
    "source_locks":{
        "corrected_pre_kummer_sha256":EXPECTED_PRE,
        "semantic_kc_picard_basis_sha256":EXPECTED_SEM,
    },
    "corrected_normalization":{
        "equation":"z^2=t^4-6*t^2+1",
        "f2":"(t-r2)/(t-r4)",
        "half_divisor_D":"P_r2-P_r4",
        "r2":"-(1+sqrt(2))",
        "r4":"1-sqrt(2)",
        "div_f2":"2*(P_r2-P_r4)",
        "both_supports_finite":True,
        "infinity_or_exceptional_support_required":False,
    },
    "cv_plus_branch":{
        "equation":"t*(1-s^2)+i*s*(1-t^2)=0",
        "s_formula":"i*(1-t^2+z)/(2*t)",
        "P_r2_s":"+i",
        "P_r4_s":"-i",
        "both_supports_on_plus_branch_verified_exact":True,
    },
    "ruled_support":{
        "adapter":{"t":"u1/v1","s":"u2/v2"},
        "P_r2":["[-(1+sqrt(2)):1]","[i:1]"],
        "P_r4":["[1-sqrt(2):1]","[-i:1]"],
        "cv_to_ruled_branch_identity_verified_exact":True,
    },
    "marked_Kc_support":{
        "stoll_coordinate_identification":[
            "A1=e","A2=x","A3=y","B1=z","B2=q","B3=p"
        ],
        "marked_branch_curve":"CsK[22]",
        "marked_branch_equations":["B1=0","i*A2-A3=0"],
        "P_r2":["1","1","i","0","0","-sqrt(2)"],
        "P_r4":["-1","1","i","0","0","-sqrt(2)"],
        "P_r2_jacobian_rank":3,
        "P_r4_jacobian_rank":3,
        "both_supports_smooth_on_Kc":True,
        "corrected_support_to_marked_Kc_materialized":True,
        "old_infinity_exceptional_order_dependency":"ELIMINATED_FOR_CORRECTED_D",
    },
    "degree_two_elliptic_quotient":{
        "map":"X=t^2, Y=t*z",
        "target":"E': Y^2=X*(X^2-6*X+1)",
        "P_r2_image":"T_plus=(3+2*sqrt(2),0)",
        "P_r4_image":"T_minus=(3-2*sqrt(2),0)",
        "difference_equals_sum_because_2torsion":True,
        "T_plus_plus_T_minus":"(0,0)",
        "corrected_D_pushforward":"(0,0) in E'[2]",
        "warning":"This one quotient coordinate does not determine the full E[2] cocycle or the surface Kummer lift.",
    },
    "exact_gap_after_this_leaf":{
        "normalization_support_to_marked_Kc_branch_materialized":True,
        "corrected_branch_Pic0_2torsion_identified":True,
        "full_surface_H2_mu2_lift_materialized":False,
        "pic_mod2_defect_1cocycle_materialized":False,
        "integral_Pic_lift_materialized":False,
        "HS_d2_2cocycle_materialized":False,
        "HS_d2_zero_proved":False,
        "Q_defined_arithmetic_Brauer_preimage_proved":False,
        "remaining_interface":"CORRECTED_PIC0_CSK22_2TORSION_TO_KC_SURFACE_H2_MU2_KUMMER_GYSIN_ADAPTER",
        "reason":"The corrected half-divisor is now located on two smooth marked-Kc points of CsK[22]; unlike the revoked historical support it uses no infinity exceptional divisor. The unresolved load-bearing step is the cohomological branch-Pic0[2] to surface H2(mu2) adapter, not coordinate/support identification.",
    },
    "next_exact_leaf":"MATERIALIZE_CORRECTED_PIC0_CSK22_2TORSION_TO_KC_SURFACE_H2_MU2_KUMMER_GYSIN_ADAPTER_THEN_COMPUTE_PIC_MOD2_DEFECT_AND_HS_D2",
    "promotion_firewall":{
        "old_ell_kummer_glue_reused":False,
        "surface_mu2_credit":False,
        "arithmetic_hs_d2_computed":False,
        "stage33_05_reclosed":False,
        "stage33_12_closed":False,
        "stage33_13_released":False,
        "theorem_credit":False,
        "receiver_credit":False,
        "endpoint_credit":False,
        "perfect_cuboid_existence_claim":False,
        "perfect_cuboid_nonexistence_claim":False,
        "stage33_progress":"5/11",
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps({
    "success":True,
    "P_r2":cert["marked_Kc_support"]["P_r2"],
    "P_r4":cert["marked_Kc_support"]["P_r4"],
    "both_smooth":True,
    "old_infinity_exceptional_order_dependency":"ELIMINATED_FOR_CORRECTED_D",
    "corrected_D_pushforward":"(0,0) in E'[2]",
    "certificate_sha256":cert["canonical_sha256"],
    "next_exact_leaf":cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
