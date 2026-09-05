#!/usr/bin/env python3
"""Verify 35EX-33 small goal 2: three literal endpoint Gaussian norm identities."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
G1=ROOT/'stages/stage35-ex/35ex-33/primitive-integral-endpoint-normalization.json'
ART=ROOT/'stages/stage35-ex/35ex-33/three-face-gaussian-norm-factorizations.json'

g1=json.loads(G1.read_text())
art=json.loads(ART.read_text())
assert g1['schema']=='STAGE35_EX_33_PRIMITIVE_INTEGRAL_ENDPOINT_NORMALIZATION_V1'
assert g1['credit_firewall']['primitive_integral_normalization_exact'] is True
assert art['schema']=='STAGE35_EX_33_THREE_FACE_GAUSSIAN_NORM_FACTORIZATIONS_V1'
assert art['stage']=='35-EX'
assert art['unit']=='35EX-33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'
assert art['small_goal']==2
assert art['status']=='PROVISIONAL_EXACT_IDENTITIES_NO_GCD_SUPPORT_CREDIT'
assert art['input_lock']['artifact']=='stages/stage35-ex/35ex-33/primitive-integral-endpoint-normalization.json'
assert art['definitions']=={
    'F_AB':'A+iB','F_AC':'A+iC','F_BC':'B+iC',
    'conj_F_AB':'A-iB','conj_F_AC':'A-iC','conj_F_BC':'B-iC',
}
assert art['exact_norm_factorizations']==[
    'F_AB*conj(F_AB)=A^2+B^2=D_AB^2',
    'F_AC*conj(F_AC)=A^2+C^2=D_AC^2',
    'F_BC*conj(F_BC)=B^2+C^2=D_BC^2',
]
assert len(art['non_consequences'])==5
assert 'square Gaussian norm alone does not imply the Gaussian integer is a square up to a unit' in art['non_consequences']
assert 'stop EQUIVALENT/BLOCKED' in art['historical_no_recharge_firewall']['next_legal_question']
for key in ('old_35EX13_Q_S_plus_reused_as_new','old_35EX17B_p_d_twist_reused_as_new','old_35EX18_relative_orientation_reused_as_new','old_35EX18_moving_c_q_reused_as_new'):
    assert art['historical_no_recharge_firewall'][key] is False, key
cf=art['credit_firewall']
assert cf['three_face_norm_identities_exact'] is True
for key in ('gaussian_element_square_claim','gaussian_gcd_support_classified','finite_squareclass_receiver_obtained','gaussian_compatibility_theorem_proved','E1_proved','stage35_closed','perfect_cuboid_nonexistence_proved'):
    assert cf[key] is False, key

# Literal Gaussian norm identity regression.
def norm(z:tuple[int,int])->int:
    return z[0]*z[0]+z[1]*z[1]
for A in range(1,8):
    for B in range(1,8):
        assert norm((A,B))==A*A+B*B

# Fail-close example: 5 has square norm 25, but is not a Gaussian square up to a unit.
units=((1,0),(-1,0),(0,1),(0,-1))
def mul(z,w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def sq(z):
    return mul(z,z)
assert norm((5,0))==25
candidates=set()
for a in range(-3,4):
    for b in range(-3,4):
        for u in units:
            candidates.add(mul(u,sq((a,b))))
assert (5,0) not in candidates

print('PASS STAGE35_EX_33_GOAL2_THREE_FACE_GAUSSIAN_NORM_FACTORIZATIONS')
